# Hiring-Challenge-E-Commerce-Customer-Segmentation
Customer segmentation using RFM analysis on the UCI Online Retail dataset to identify top customers and at-risk high spenders for targeted marketing campaigns.

---

## Project Overview

The goal of this project is to help a marketing team identify two important customer segments based on purchasing behaviour:

- **Champions** – the most valuable customers who buy frequently, spend a lot, and purchased recently.
- **At-Risk High Spenders** – customers who historically spent a lot but have not purchased recently.

The segmentation is based on **RFM analysis**, a widely used method in marketing analytics for understanding customer value.

---

## Dataset

The dataset used is the **Online Retail Dataset** from the UCI Machine Learning Repository.

Dataset source:  
https://archive.ics.uci.edu/dataset/352/online+retail

---

## Repository Structure

**data_cleaning.ipynb** and **business_insights.ipynb**  
Jupyter notebook containing the full workflow of the analysis, including data exploration, RFM calculation, and customer segmentation.

**functions.py**  
Python functions used in the project, including data cleaning, RFM metric calculation (Recency, Frequency, Monetary), and the identification of Champions and At-Risk High Spenders.

**champions.csv**  
CSV file containing the Customer IDs of the top 50 Champions (customers who spend the most, buy frequently, and purchased recently).

**at_risk_high_spenders.csv**  
CSV file containing the Customer IDs of the 50 At-Risk High Spenders (customers who historically spent a lot but have not purchased recently).

**PROMPT_DIARY.md**  
Short document describing how AI tools were used during the development of this project.

**README.md**  
Overview of the repository and explanation of the project structure.
