# 🛒 D2C E-commerce Analytics & Business Intelligence Pipeline

## 📌 Project Overview
An end-to-end data analytics and business intelligence pipeline built using the **Olist Brazilian E-commerce dataset**. This project simulates a real-world enterprise reporting setup, transforming raw multi-relational data into actionable executive insights.

---

## 🛠️ Tech Stack & Architecture
* **Python (Pandas, SQLite):** Automated data ingestion, cleaning, and local relational database construction (`ecommerce_analytics.db`).
* **Power BI Desktop:** Enterprise-grade Star Schema modeling, advanced DAX measures, and interactive executive reporting.
* **SQL:** Relational database querying and data modeling.

---

## 📊 Data Model & Star Schema
The pipeline models a classic **One-to-Many Star Schema** centered around the `order_items` fact table, connected seamlessly to:
* `customers` (Demographics & Geographic State mapping)
* `orders` (Order timestamps, status, fulfillment tracking)
* `products` (Product categories and physical dimensions)
* `payments` (Payment types and installment structures)
* `sellers` (Merchant location metrics)

---

## 📈 Key Dashboard Highlights (Page 1: Executive Summary)
* **High-Level KPIs:** Real-time tracking of `Total Revenue`, `Total Orders`, and `Average Order Value (AOV)`.
* **Revenue Trend Analysis:** Time-series growth curves tracking performance over historical periods.
* **Product Category Performance:** Ranked bar charts highlighting top revenue drivers (e.g., *health_beauty*, *watches_gifts*).
* **Geographical Mapping:** Interactive map visualization displaying regional customer distribution and state-wise revenue concentration.

---

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Olist_Ecommerce_Analytics_Pipeline.git](https://github.com/YOUR_USERNAME/Olist_Ecommerce_Analytics_Pipeline.git)
