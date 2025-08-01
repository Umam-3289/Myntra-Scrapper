🛍️ Myntra Scrapper
A Python-based web scraper to extract product details from Myntra — one of India’s leading fashion and lifestyle e-commerce platforms. This project allows you to collect structured data such as product titles, brands, prices, ratings, reviews, images, and more.

📌 Features
🔎 Scrapes product listings from specific categories or search queries

🏷️ Extracts product names, brands, prices (MRP, discounted), and discounts

⭐ Gathers customer ratings and review counts

🖼️ Captures product image links and product page URLs

🧹 Cleaned and structured data output (CSV/JSON/DataFrame)

📦 Easily pluggable into machine learning pipelines or price tracking apps

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Umam-3289/Myntra-Scrapper.git
cd Myntra-Scrapper
2. Install Dependencies
Make sure Python 3.7+ is installed.

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Scraper
bash
Copy
Edit
python myntra_scraper.py
You can modify the script to target different search keywords, categories, or pagination ranges.

🗃️ Output Format
The scraper exports data in a tabular format with the following columns:

Product Name

Brand

Original Price

Discounted Price

Discount Percentage

Rating

Number of Reviews

Product URL

Image URL

📊 Use Cases
🧠 Train price prediction or recommendation models

📈 Build trend analysis dashboards for fashion products

🔍 Competitor analysis or market research

📥 Create personal product wishlists or alerts

🛠️ Built With
requests – For sending HTTP requests

BeautifulSoup – For parsing HTML content

pandas – For data structuring and export

Streamlit (optional) – For building a UI to view or filter products

📷 Streamlit App
Try out the hosted version here:
🌐 Myntra Scraper App

⚠️ Disclaimer
This project is intended for educational and personal use only. Scraping large volumes or violating Myntra's terms of service may lead to IP bans or legal action. Please respect the website's policies.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

📧 Contact
For queries or collaboration:

Umam Khan
📩 umamkhan9931@gmail.com
🔗 umam-khan-7213aa261


