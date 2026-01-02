# Next-Gen Commerce & Logistics – Executive Analytics Dashboard

##  Project Overview
This project focuses on analyzing e-commerce logistics performance and customer experience using real-world commerce data.  
The goal is to identify delivery efficiency, SLA adherence, regional bottlenecks, and the impact of delivery delays on customer satisfaction.

The project follows an **industry-style end-to-end analytics pipeline**:
Python → SQL Server → Power BI.

---

##  Tools & Technologies
- Python (Pandas, NumPy)
- SQL Server (KPI analysis & validation)
- Power BI (Dashboard & visualization)
- GitHub (Version control & documentation)

---

##  Key Business Metrics
- Total Orders
- Average Delivery Time
- Late Delivery Percentage (SLA breach)
- Average Customer Review Score
- City-level delivery performance
- Payment method performance

---

##  Key Insights
- Late deliveries have a significant negative impact on customer review scores.
- Certain cities consistently show higher average delivery times, indicating last-mile logistics challenges.
- Over 90% of orders are delivered on time, but delayed deliveries disproportionately affect customer satisfaction.
- Payment type analysis helps understand revenue contribution and order behavior.

---

##  Feature Engineering
The following features were engineered in Python:
- Delivery Time (days)
- Delivery Delay (days)
- SLA flag (`is_late`)
- Cleaned and validated timestamps
- Delivered-order filtering for business relevance

---

##  Dashboard Highlights
- Executive KPI cards for quick decision-making
- On-Time vs Late delivery analysis
- Top cities by average delivery time
- Impact of delivery delays on customer reviews
- Interactive slicers for city, delivery status, and payment type

---

##  Project Workflow
1. Data Cleaning & Feature Engineering (Python)
2. Exploratory Data Analysis (Python)
3. KPI Validation & Business Analysis (SQL Server)
4. Interactive Dashboard Creation (Power BI)

---

##  Repository Structure
Next-Gen-Commerce-Logistics
│
├── Data/
│ └── cleaned_olist_commerce_data.zip
│
├── Python/
│ ├── data_cleaning.py
│ ├── exploratory_data_analysis.py
│ └── python_to_sql_connector.py
│
├── Sql/
│ ├── table_creation.sql
│ └── kpi_analysis.sql
│
├── PowerBi/
│ ├── executive_dashboard.pbix
│ └── dashboard_preview.png
│
└── README.md



---

##  How to Use
1. Review Python scripts for data preparation and feature engineering  
2. Run SQL scripts for KPI analysis  
3. Open the Power BI file to explore the interactive dashboard  

---

##  Contact
If you’d like to discuss this project or provide feedback, feel free to connect with me on LinkedIn.
