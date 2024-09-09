# Guard's Eye - Dark Patterns Buster Hackathon

## Overview

We are proud to have participated in the grand finale of the **Dark Patterns Buster Hackathon** hosted by the **Department of Consumer Affairs, Government of India**, at **IIT BHU, Varanasi**. The hackathon provided a unique platform to contribute to the fight against deceptive practices in online spaces. Our project, **Guard’s Eye**, is a state-of-the-art browser extension aimed at promoting transparency and fairness in e-commerce platforms.

The hackathon reinforced the importance of ethical digital practices and the power of teamwork in driving meaningful change in the digital landscape.

## Project: Guard's Eye

### Abstract

**Guard's Eye** is a browser extension designed to improve online shopping experiences by tackling common issues such as **Fake Reviews**, **User Interface Deception**, and **Misleading Product Information**. The extension leverages **machine learning** and **image recognition** technologies to provide users with comprehensive tools to verify the authenticity of product-related information. It also safeguards users from deceptive practices like **Fake Urgency**, **Privacy Intrusion**, and **Subscription Trickery**, while ensuring transparency in **Data Governance** policies.

### Features

1. **Misleading Product Information & UI Deception**  
   - Comprehensive product analysis by cross-referencing images, descriptions, and reviews.
   - Identification of discrepancies to ensure trustworthy information.

2. **Fake Reviews**  
   - Detection and filtering of fake reviews using advanced tools.
   - Assigns credibility scores to reviews for better decision-making.

3. **Fake Urgency**  
   - Compares current prices with historical data to validate time-sensitive offers.
   - Provides context to determine if urgency is real or artificially created.

4. **User Interface Deception**  
   - Identifies UI elements that mislead or hide crucial information from users.

5. **Data Governance**  
   - Evaluates websites for compliance with data privacy regulations (e.g., GDPR).
   - Provides simplified overviews of data handling for better transparency.

6. **Privacy Intrusion**  
   - Scrutinizes website data practices and ensures compliance with privacy laws.
   - Simplifies privacy policies for user clarity.

7. **Subscription Trickery**  
   - Detects misleading subscription offers and complex cancellation procedures.
   - Helps users navigate subscription services confidently.

### Additional Feature

**Price History Graph**  
A dynamic feature allowing users to view historical price data for products on e-commerce platforms. It helps users identify genuine discounts and avoid deceptive pricing tactics.

- **Graphical Representation**: Displays price trends over time with interactive features.
- **Time Range Flexibility**: Users can choose time frames (1 month, 3 months, 6 months, or year-to-date) to analyze price movements.

### Process Flow

1. **Data Scraping**  
   - Utilizes **Beautiful Soup** and **Selenium** to scrape product data (images, reviews, text) from e-commerce websites.

2. **Machine Learning Model**  
   - Analyzes scraped data for dark patterns, fake reviews, privacy policy compliance, and subscription trickery.

3. **Dark Pattern Detection**  
   - Highlights deceptive tactics identified during analysis, empowering users to avoid manipulative practices.

4. **Fake Review Identification**  
   - Detects fake reviews and provides a credibility score for each.

5. **User-Friendly Interface**  
   - Delivers a clear and concise analysis of dark patterns, making it easy for users to make informed decisions.

### The Model

- **Blip Image Captioning**: Generates captions for product images, enhancing visual content analysis.
- **Pytesseract OCR**: Extracts text from product images for detailed analysis.
- **roBERTa Classifier**: Detects and filters fake reviews from the dataset.
- **Distill roBERTa+ Classifier**: Analyzes textual content from e-commerce websites to identify dark patterns.
- **Mistral LLM Model**: Integrates analysis from image captions, extracted text, and reviews, ensuring data integrity. It also evaluates privacy policies and subscription tricks against legal standards.

### Poster 

![Guard's Eye Poster](./Poster/DPBH poster.png)

## Conclusion

**Guard's Eye** represents a robust solution to tackle various dark patterns in e-commerce. Through teamwork and cutting-edge technology, we aim to empower users to make informed choices and protect themselves from manipulative practices online.

---

## Links
[LinkedIn Post](https://www.linkedin.com/posts/santhosh-kumar-santhanam_darkpatterns-transparency-hackathonfinals-activity-7199670814168764416-j9jL?utm_source=share&utm_medium=member_desktop)
