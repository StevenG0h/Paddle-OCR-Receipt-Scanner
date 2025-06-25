## Receipt-Based Expense Tracking System

This system is designed to assist users in tracking their expenses by extracting essential data from shopping receipts. 

Through a simple **Gradio** interface, users can upload an image of their receipt. Once the image is uploaded, the system uses the **PaddleOCR** model to process the receipt and extract relevant financial information, such as individual prices and the total amount spent.

The extracted data is stored in a **database**, allowing users to build a history of their spending over time. Although the system does not extract detailed item names or purchase dates, it focuses on capturing numerical data accurately to simplify expense tracking.
