# Tourism
# 🧭 Smart Tourism Data Intelligence System

A full-stack data analytics project that collects, cleans, stores, and visualizes tourism-related data such as hotel prices, ratings, and weather patterns. This system empowers travelers, analysts, and tourism boards with real-time, data-driven insights using a command-line interface and interactive Power BI dashboards.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Modules](#modules)
- [How to Run](#how-to-run)
- [Dashboards](#dashboards)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📖 About the Project

> The tourism industry is rich in data but lacks accessible tools for insight extraction. This project solves that by integrating Python, MySQL, and Power BI to create an automated and insightful travel analytics platform.

---

## ✨ Features

- 🌐 Scrape hotel data (name, price, rating, amenities) from travel websites
- 🌦️ Integrate historical weather data via OpenWeatherMap API
- 🗃️ Store and manage structured data in MySQL
- 📊 Visualize trends using Power BI dashboards
- 🧹 Clean and standardize raw data using Python and Pandas
- ⏲️ Automate the pipeline with Linux cron jobs

---

## 🛠️ Tech Stack

| Technology     | Purpose                              |
|----------------|--------------------------------------|
| **Linux**      | Automation & CLI Environment         |
| **Python**     | Scraping, Data Cleaning, ETL         |
| **MySQL**      | Structured Data Storage               |
| **Power BI**   | Interactive Dashboard Visualization   |
| **Pandas**     | Data Transformation & Cleaning        |
| **Selenium / BeautifulSoup** | Web Scraping Tools     |
| **OpenWeatherMap API** | Weather Data Integration     |

---

## 🏗️ System Architecture

```plaintext
+------------+     +----------------+     +----------+     +-------------+
| Linux Cron | --> | Python Scraper | --> | MySQL DB | --> | Power BI 📊 |
+------------+     +----------------+     +----------+     +-------------+
                               |
                     +------------------+
                     | Weather API (OWM)|
                     +------------------+
