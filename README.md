# End-to-End Customer Segmentation for Targeted Marketing Optimization

## 1. Executive Summary

This project builds a complete end-to-end customer segmentation pipeline using unsupervised machine learning to identify high-value customer groups and enable targeted marketing strategies.

Using KMeans clustering on demographic and purchasing behavior data, I identified four distinct customer segments with significantly different revenue contribution patterns, engagement levels, and campaign responsiveness.

The final model was deployed using Streamlit and is publicly accessible for interactive predictions.

🔗 **Live App:**  
https://end-to-end-customer-segmentation.onrender.com

This project simulates a real-world business scenario where data science directly supports marketing, growth, and revenue optimization teams.

---

## 2. Business Problem

Marketing budgets are limited.

Companies cannot treat every customer the same. Without segmentation:

- High-value customers are not properly nurtured  
- Low-engagement customers are not reactivated  
- Marketing spend is inefficient  
- Revenue opportunities are missed  

The objective of this project is to:

- Identify high-value customer segments  
- Understand revenue contribution by segment  
- Detect at-risk or low-engagement customers  
- Enable personalized marketing strategies  
- Improve ROI through data-driven targeting  

---

## 3. Methodology

### Data Overview

- 2,240 customers  
- 29 original features  
- After cleaning: 2,216 usable records  

Features include:

- Demographics (Age, Education, Marital Status)
- Income
- Product spending across categories
- Purchase channels (Web, Store, Catalog)
- Campaign response history
- Recency (days since last purchase)

---

### Data Cleaning & Feature Engineering

- Removed missing income values  
- Capped extreme income outliers at 99th percentile  
- Converted date columns to datetime  
- Created new features:
  - `Age`
  - `total_children`
  - `total_spending`
  - `customer_since`
  - `AcceptedAny` (binary campaign response)

---

### Exploratory Data Analysis

Key findings:

- Strong correlation between Income and Total Spending (~0.81)
- Education level influences average spending
- Digital purchase behavior varies significantly
- Campaign response differs across customer groups

---

### Clustering Approach

- Algorithm: KMeans  
- Scaling: StandardScaler  
- Model pipeline built using Scikit-learn  
- Optimal K selected using:
  - Elbow Method  
  - Silhouette Score  

Final number of clusters: **4**

Silhouette Score: ~0.19  
(Moderate separation but strong business interpretability)

---

### Deployment

- Model serialized using `joblib`  
- Deployed via Streamlit  
- Hosted on Render  

Users can input customer details and receive predicted segment along with segment descriptions.

---

## 4. Skills Demonstrated

- Data Cleaning & Feature Engineering  
- Exploratory Data Analysis (EDA)  
- Correlation Analysis  
- Unsupervised Learning (KMeans)  
- Model Evaluation (Silhouette Score, Elbow Method)  
- Scikit-learn Pipelines  
- PCA for visualization  
- Business Insight Generation  
- Model Deployment with Streamlit  
- Production-level ML workflow  

---

## 5. Results & Business Recommendations

### Identified Segments

1. **Digital-First High-Value Shoppers**
   - Highest income
   - Highest spending
   - Strong online and store engagement
   - Revenue Contribution: ~55%

2. **Premium Loyal Customers**
   - High income
   - High campaign acceptance
   - Revenue Contribution: ~34%

3. **Price-Sensitive Occasional Buyers**
   - Low income
   - Low spending
   - Revenue Contribution: ~4–5%

4. **Low-Engagement Budget Customers**
   - Lower income
   - High recency (at risk)
   - Weak campaign response
   - Revenue Contribution: ~5%

---

### Key Business Insight

Approximately 20–25% of customers generate nearly 90% of revenue.

This indicates strong revenue concentration and the need for strategic targeting.

---

### Business Recommendations

- Create VIP loyalty programs for Digital-First High-Value Shoppers  
- Offer personalized rewards and early access for Premium Loyal Customers  
- Run discount-based reactivation campaigns for Price-Sensitive customers  
- Launch targeted re-engagement campaigns for Low-Engagement customers  
- Allocate marketing budget proportionally to revenue-driving segments  

Segmentation-driven targeting would significantly improve marketing ROI compared to broad campaigns.

---

## 6. Next Steps

- Compare KMeans with Hierarchical Clustering  
- Evaluate cluster stability across different feature sets  
- Improve feature selection using statistical techniques  
- Add automated dashboard metrics  
- Add A/B testing simulation for campaign performance  

---


## 7. Deployment

🔗 Live Application:  
https://end-to-end-customer-segmentation.onrender.com

---

## Conclusion

This project demonstrates how data science can move beyond analysis and directly influence strategic business decisions.

It connects:

Data → Insights → Machine Learning → Deployment → Business Value
