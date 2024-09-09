import ast
import requests
import json



text = '''
HomeMobiles & AccessoriesMobilesApple Mobiles
Apple iPhone 15 (Black, 128 GB)

Compare
Share
Apple iPhone 15 (Black, 128 GB)
4.613,060 Ratings & 888 Reviews
Extra ₹10901 off
₹66,999₹79,90016% off
i
+ ₹99 Secured Packaging Fee
Available offers

Bank Offer10% off on BOBCARD Transactions, up to ₹750 on orders of ₹10,000 and aboveT&C

Bank Offer10% off on BOBCARD EMI Transactions, up to ₹1,250 on orders of ₹10,000 and aboveT&C

Bank Offer10% off on Citi-branded Credit Card EMI Transactions, up to ₹1,500 on orders of ₹7,500 and aboveT&C

Special PriceGet extra ₹10901 off (price inclusive of cashback/coupon)T&C

View 19 more offers
Buy without Exchange
₹66,999
Buy with Exchange
up to ₹55,000 off

1 Year Warranty for Phone and 6 Months Warranty for In-Box AccessoriesKnow More
Color

2 more
Storage
128 GB
256 GB
512 GB
Delivery
600008
ChangeCheck pincode✕
Delivery in2 Days, Tuesday|Free₹40?
if ordered before 4:35 PM
View Details
Highlights
128 GB ROM
15.49 cm (6.1 inch) Super Retina XDR Display
48MP + 12MP | 12MP Front Camera
A16 Bionic Chip, 6 Core Processor Processor
Easy Payment Options
EMI starting from ₹2,356/month
Net banking & Credit/ Debit/ ATM card
View Details
Seller
TREASURE HAUL ONLINE5
7 Days Service Center Replacement/Repair?
GST invoice available?
See other sellers

Protect your product
Protect+ with AppleCare Services for iPhone 15
Protect+ with AppleCare Services for iPhone 15
Unlimited incidents of accidental damage protection, iCloud+ with 50GB of storage, Battery and hardware coverage, Pickup and delivery service, Same-day screen repair, Apple-certified repairs with genuine Apple parts at Apple Stores, Priority access to Apple Support.Know More
Brand authorised repair & Customer support Paperless seamless Hassel free transation
₹8,499₹9,99915% off
Extended Warranty 1 Year
Extended Warranty 1 Year
Get brand authorised repairs with free pickup and drop. Absolutely no hidden charges!Know More
Extend the life of your Mobile with safety and convenience
₹1,099
1 Item
Added
2 Add-ons
₹9,598
Total
₹9,598
ADD 2 ITEMS TO CART
Description
Experience the iPhone 15 – your dynamic companion. Dynamic Island ensures you stay connected, bubbling up alerts seamlessly while you're busy. Its durable design features infused glass and aerospace-grade aluminum, making it dependable and resistant to water and dust. Capture life with precision using the 48 MP Main Camera, perfect for any shot. Powered by the A16 Bionic Processor, it excels in computational photography and more, all while conserving battery life. Plus, it's USB-C compatible, simplifying your charging needs. Elevate your tech game with the iPhone 15 – innovation at your fingertips. Goodbye cable clutter, hello convenience.

Product Description

Dynamic Island
Dynamic Island bubbles up alerts and Live Activities — so you don’t miss them while you’re doing something else. You can track your next ride, see who’s calling, check your flight status, and so much more.


Highly Durable
The innovative new design features back glass that has color infused throughout the material. A custom dual ion-exchange process for the glass, and an aerospace-grade aluminum enclosure, help make the iPhone 15 incredibly durable. Dependably durable. The Ceramic Shield front is tougher than any smartphone glass. Moreover, the iPhone is splash, water, and dust resistant. What a relief.

View all features'''
# output = query({
#     "inputs": "whoa this is a really interesting article, I'm going to share it with my friends!",
# })


lines = text.split("\n")
# Remove empty strings
lines = [line for line in lines if line]

# for txt in lines:
#     output = query({
#         "inputs": txt,
#     })
#     print(output)

#     # Assuming output is your prediction result

#     try:
#         for prediction in output[0]:
#             label = prediction['label']
#             score = prediction['score']
#             if label == 'Dark_Pattern' and score > 0.50:
#                 print(txt,end=": ")
#                 print("Dark Pattern")
#     except Exception as e:
#         print("An error occurred:", e)

def funcc():
    url = "https://6507-34-87-66-11.ngrok-free.app/llama"
    print(lines)
    sting_list = []
    for txt in lines:
        input_data = {
            'Query': txt,
        }
        response = requests.post(url, json=input_data)
        start = response.text.find('{') + 1  # +1 to exclude the ':' itself
        end = response.text.rfind(':') + 1  # +1 to include the '}' itself
        sliced = response.text  [start:end]
        print(sliced,":",txt)
        if (json.loads(response.text)[0]) == 'Dark_Pattern':
            sting_list.append(txt)
            
    return sting_list

    
