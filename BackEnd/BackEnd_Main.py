from flask import Flask, request, jsonify
import requests
import json
from PIL import Image, ImageEnhance
import pytesseract
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import openai
from bs4 import BeautifulSoup
import pandas as pd
import re
from DBPH_Hackathon.Extension.PParakurom.Testing.dark_pattern import funcc
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def dark_pattern_detect():
    output = funcc()
    return output


def fake_review_api(review_dict):

    temp_dict = {}

    def api_call(review_str):
        url = "https://77cf-34-125-136-248.ngrok-free.app/llama"
        input_data = {
            'Query': review_str,
        }
        # print(input_data['File'])
        # input_data = json.dumps(input_data)
        response = requests.post(url, json=input_data)
        # print(response.text)
        return round(float(response.text.replace('"', '')), 2)

    for key, value in review_dict["Review"].items():
        combined_string = f"{key}: {value}"
        # Replace with the actual function you want to use
        response = api_call(combined_string)
        temp_dict[key] = response

    return temp_dict


def Scarper_review_product(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the dates are inside span elements, adjust the selector accordingly
    share_elements = soup.find_all('span')
    div_elements = soup.find_all('div', class_='_2c2kV-')

    date = []
    text_data = []

    if div_elements:  # Check if there are elements in div_elements
        for div in div_elements:
            # Replace <br> tags with spaces in the text content
            text_content = div.get_text(separator=' ')
            if "Report Abuse" in text_content:
                reviews = text_content.split("Report Abuse")
                # Separate reviews before/after "Report Abuse"
                text_data.extend(reviews)
            else:
                text_data.append(text_content)

    for share_element in share_elements:
        date.append(share_element.text)

    df = pd.DataFrame({'date': date})

    # Find the index of the third occurrence of "Share"
    index_third_share = df[df['date'] == 'Share'].index[2]

    # Extract only the line after the third "Share"
    df_final = df.iloc[index_third_share + 1: index_third_share + 2]
    df_final.columns = [""]

    # src_arr = []
    # images_tag2 = soup.find_all('img', class_='q6DClP')
    # for image in images_tag2:
    #     src_arr.append(image['src'] if image else None)

    texts_from_class = []
    elements_with_class = soup.find_all(
        'div', class_='_3dtsli')  # Adjust selector if needed
    if elements_with_class:
        for element in elements_with_class:
            # Remove extra whitespace
            text = element.get_text(strip=True, separator=' ')
            texts_from_class.append(text)

    data_dict = {}

    # Find all elements with class '_2-N8zT'
    for _2_N8zT_element in soup.find_all(class_='_2-N8zT'):
        # Get the text inside class '_2-N8zT'
        key = _2_N8zT_element.get_text(strip=True)

        # Get the next sibling with class 't-ZTKy'
        t_ZTKy_element = _2_N8zT_element.find_next(class_='t-ZTKy')

        # Check if the next sibling exists
        if t_ZTKy_element:
            # Get the text inside class 't-ZTKy' and remove "READ MORE"
            value = t_ZTKy_element.get_text(
                strip=True, separator=' ').replace('READ MORE', ' ')

            # Add to the dictionary
            data_dict[key] = value

    # print("Texts from class _1AtVbE col-12-12:", texts_from_class)
    # print(image_url)
    # print(df_final)
    # result_json = df_final.to_json(orient='records')

    # Your scraping logic here

    # Replace with the actual result you want to return
    return {'Review': data_dict, 'Product': texts_from_class[0]}


# summa
# @app.route('/get-text-to-highlight', methods=['GET'])
# def get_text_to_highlight():
#     # This could be any text you want to highlight.
#     text_to_highlight = "samsung"
#     return jsonify({"textToHighlight": text_to_highlight})


@app.route('/receive-data', methods=['POST'])
def receive_data():

    print('Received data')
    print(request)
    data = request.get_json()
    print(data)
    url = data['url']

    src_array = scrape_images(url)
    # print("Image URLs scraped.")

    # #Process images using Image Captioning and OCR
    Img_Cap_OCR = process_images(src_array)
    # print("Images processed.")

    Reviews_Product = Scarper_review_product(url)
    # for i in range(10, 0, -1):
    #     print(i)
    #     time.sleep(1)

    # print(Reviews_Product)
    print("Reviews scraped and tested.")
    # # temp = Reviews_Product['Review']

    # Fake_review_result = fake_review_api(temp)
    # print(Fake_review_result)
    print("Fake review results obtained.")
    # print(Fake_review_result)
    # print(Reviews_Product == Fake_review_result)

    # filtered_reviews = [k for k,v in Reviews_Product['Review'].items() if Fake_review_result[k] > 0.50]
    # print(filtered_reviews)
    filtered_reviews =  list(filtered_reviews.values())
    # print("Reviews filtered.", filtered_reviews)

    dark_pattern_output = dark_pattern_detect()

    combined_string = f"Image Captioning: {Img_Cap_OCR}\nProduct Description: {Reviews_Product['Product']}\nReviews: {json.dumps(filtered_reviews)}"
    # print("Combined string created.")

    result = Llama(combined_string)
    print("LLM response obtained.")


    # print(result.text)
    # print(filtered_reviews,highlight)
    # process the data
    return jsonify({"status": "success", "processedReviews": filtered_reviews, "textsToHighlight": result.text, "darkPattern": dark_pattern_output})


def Llama(input_text):

    url = "https://ebd3-35-225-233-164.ngrok-free.app/llama"

    input_data = {
        'Query': "Find any differences if present in product description and image description given in the file. and Consider if there exist any negative reviews as well",
        'File': input_text
    }
    # print(input_data['File'])
    # input_data = json.dumps(input_data)

    response = requests.post(url, json=input_data)

    return response


def scrape_images(url):
    path = Service(
        r'C:\Users\santosh kumar\Documents\Works\Hackathons\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=path)
    driver.get(url)

    src_array = []

    try:
        while True:
            elements = driver.find_elements(By.CLASS_NAME, 'q6DClP')
            if not elements:
                break

            for i in range(len(elements) - 1, -1, -1):
                try:
                    elements[i].click()
                    time.sleep(2)

                    img_element = driver.find_element(
                        By.XPATH, '//img[@class="_396cs4 _2amPTt _3qGmMb"]')
                    img_src = img_element.get_attribute('src')
                    src_array.append(img_src)

                except StaleElementReferenceException:
                    driver.back()
                    driver.refresh()
                    time.sleep(2)
                    elements = driver.find_elements(By.CLASS_NAME, 'q6DClP')

                except NoSuchElementException:
                    print("Image element not found on this page.")

            driver.back()

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

    return src_array


def process_images(src_array):
    dummy = ''
    for Image_path in src_array:
        img = Image.open(BytesIO(requests.get(Image_path).content))
        img.save('output.jpg')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(img)

        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        headers = {
            "Authorization": "Bearer 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"}

        def query(filename):
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query('output.jpg')

        dummy = dummy + output[0]['generated_text']+text+"\n"

    return dummy


# @app.route('/get-reviews', methods=['GET'])
# def get_reviews():
#     global filtered_reviews
#     if filtered_reviews:
#         temp = filtered_reviews
#         filtered_reviews = []
#         print("Filtered reviews sent.")
#         print(filtered_reviews)
#         return jsonify({"status": "success", "processedReviews": temp})
#     else:
#         return jsonify({"status": "no data"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
