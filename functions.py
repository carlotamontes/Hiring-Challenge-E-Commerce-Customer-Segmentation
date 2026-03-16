import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from torch import negative


def data_cleaning(excel_file):
    # Remove any rows that have missing CustomerIDs 
    # Remove any rows with cancelled orders (negative values)
    # Remove any rows that have a Quantity less than or equal to 0
    # Remove any rows that have a InvoiceNo that starts with "C" (Cancelled orders)

    excel_file = excel_file.dropna(subset=["CustomerID"])
    excel_file = excel_file[excel_file["Quantity"] > 0].copy()
    excel_file = excel_file[excel_file["UnitPrice"] > 0].copy()
    excel_file = excel_file[~excel_file["InvoiceNo"].astype(str).str.startswith("C")].copy()

    return excel_file

def calculate_recency(excel_file):
    # how many days have passed since the last purchase of each customer 
    # add column with days since last purchase for each customer

    excel_file["InvoiceDate"] = pd.to_datetime(excel_file["InvoiceDate"], dayfirst=True)
    today_date = excel_file["InvoiceDate"].max() # maximum date in the dataset 
    last_purchase = excel_file.groupby("CustomerID")["InvoiceDate"].max()
    
    recency = (today_date - last_purchase).dt.days

    recency_data = recency.reset_index()
    recency_data.columns = ["CustomerID", "Recency"]

    return recency_data


def calculate_frequency(excel_file):
    # Separate invoices/orders a costumer has made 
    # Same InvoiceNo = Same Transaction = One purchase 
    frequency = excel_file.groupby("CustomerID")["InvoiceNo"].nunique()

    frequency_data = frequency.reset_index()
    frequency_data.columns = ["CustomerID", "Frequency"]

    return frequency_data


def calculate_monetary(excel_file):
    # Total amount of money a customer has spent 
    # TotalPrice = Quantity * UnitPrice
    excel_file["TotalPrice"] = excel_file["Quantity"] * excel_file["UnitPrice"]

    monetary = excel_file.groupby("CustomerID")["TotalPrice"].sum()

    monetary_data = monetary.reset_index()
    monetary_data.columns = ["CustomerID", "Monetary"]

    return monetary_data


def clean_rfm_data(rfm_data):
    # Remove customers with Monetary value of 0
    rfm_data = rfm_data[rfm_data["Monetary"] > 0].copy()

    return rfm_data


# ascending=True   → 1,2,3,4,5
# ascending=False  → 5,4,3,2,1

def find_champions(rfm_data):

    # Find the top 50 customers based on the RFM score
    # Best costumers have low recency, high frequency and high monetary value
    # Main feature is monetary 

    champions = rfm_data.sort_values(["Monetary", "Frequency", "Recency"], ascending=[False, False, True]).head(50) 

    return champions

def find_risk_high_spenders(rfm_data):

    # Find the top 50 customers who have spent a lot of money but have not bought for a long time
    # Costumers have high recency, low frequency and high monetary value
    # Need to define a filter for high monetary value
    # Then choose those high spenders that have high recency and low frequency

    high_spenders = rfm_data[rfm_data["Monetary"] > rfm_data["Monetary"].quantile(0.80)]

    risk_high_spenders = high_spenders.sort_values(["Recency", "Frequency"], ascending=[False, True]).head(50) 

    return risk_high_spenders
