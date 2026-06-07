# WEB-SCRAPING-PROJECT-BATCH4
Final Capstone Project

## 📱 WinMobileWorld E-Commerce Scraper

An automated Python web scraper designed to crawl, extract, and compile product catalogs from the WinMobileWorld e-commerce store. It automatically handles pagination, dynamically strips formatting from price data, detects stock anomalies, and archives everything into localized Excel datasets.

## 🚀 Features
* Dynamic Pagination Tracking: Automatically detects the maximum number of pages from the homepage.

* Smart Price Extraction: Correctly isolates promotional or markdown prices vs. normal retail prices.

* Automatic Status Tracking: Flags items as Out of stock based on page badges, defaulting cleanly to Instock otherwise.

* Safe Incremental Backups: Saves individual Excel spreadsheets page-by-page to prevent data loss if your connection drops mid-scrape, before compiling everything into one master file.

* Progress Visualization: Uses tqdm to display a live, visual progress bar in your terminal.

## 🛠️ Prerequisites & Installation

1. Initialize Your Environment

Clone or download this workspace environment, then ensure you are operating inside your root project directory:

	cd your-repository-name
2. Deploy Dependencies

Install the required upstream packaging frameworks along with openpyxl (the background workbook generator engine used by Pandas):

	pip install -r requirements.txt

## 💻 How To Run

Simply execute the script file from your terminal, command line prompt, or chosen IDE environment (such as Thonny, VS Code, or IDLE):

	python Main.py

## 📊 Data Output Schema
The final generated compilation file features an analysis-ready matrix containing three core data columns:

| Product Name  | Product Price | Status 
| :--- | :---: | :---: |
| **Honor X6b (4/128GB)** | 339900 | Instock |
| **Xiaomi Redmi 13 (8/128GB)** | 489900 | Out of stock | 
| **Samsung Galaxy A15 (8/256GB)** | 619900 | Instock | 
...

📌 Data Cleaning Note: String commas (,) and legal tender notation values (MMK) are systematically stripped out during runtime cleaning cycles to yield clean integers optimized for active analytical manipulation.

## 📜 Disclaimer & Ethics

⚠️ Fair Use & Educational Scraping Directive

This repository is developed and distributed strictly for educational benchmarks, self-research, and analytical evaluation. It is not meant for aggressive data harvesting or commercial monetization pipelines.
