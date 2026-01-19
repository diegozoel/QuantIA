import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

# Global configuration constants
SEED = 42           # Fixed seed for reproducibility
NUM_SKUS = 50       # Number of synthetic products to generate
DAYS_HISTORY = 365  # Number of days to simulate in the past
OUTPUT_PATH = "data/raw" # Directory for output CSV files

def init_generator():
    """Initializes the random seed to ensure data consistency."""
    np.random.seed(SEED)
    print(f"[{datetime.now()}]) Generator Engine Initialized. Seed: {SEED}")

def generate_skus(n=NUM_SKUS):
    """
    Generates a catalog of synthetic products (Master Data).
    
    Args:
        n (int): Number of SKUs to generate.

    Returns:
        pd.DataFrame: A table containing SKU_ID, Cost, Price, and Lead Time.
    """
    # 1. Generate IDs (e.g., SKU-001, SKU-002...)
    ids = [f"SKU-{i:03d}" for i in range(1, n + 1)]
    
    # 2. Simulate Costs (Log-Normal distribution to simulate real-world pricing skew)
    # Most items are low cost, few are high cost.
    costs = np.random.lognormal(mean=3.0, sigma=0.5, size=n).round(2)
    
    # 3. Calculate Unit Price (Cost + Margin between 20% and 60%)
    margins = np.random.uniform(1.2, 1.6, size=n)
    prices = (costs * margins).round(2)
    
    # 4. Assign Supplier Lead Times (Days)
    # Probabilistic choice: 30% take 7 days, 10% take 45 days, etc.
    lead_times = np.random.choice([3, 7, 14, 30, 45], size=n, p=[0.1, 0.3, 0.3, 0.2, 0.1])

    # 5. Build the DataFrame
    df_skus = pd.DataFrame({
        "sku_id": ids,
        "unit_cost": costs,
        "unit_price": prices,
        "avg_lead_time": lead_times,
        "safety_stock_target": np.random.randint(10, 100, size=n) # Static placeholder
    })
    
    return df_skus

def generate_demand_history(df_skus, days=DAYS_HISTORY):
    """
    Simulates daily sales data using Poisson distribution.
    
    Args:
        df_skus (pd.DataFrame): The product master table.
        days (int): Number of days to simulate into the past.
        
    Returns:
        pd.DataFrame: Transactional sales data (Fact Table).
    """
    print(f"[{datetime.now()}] Simulating {days} days of demand for {len(df_skus)} SKUs...")
    
    # Define date range (Today backwards)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    records = [] # Buffer list to store temporary dataframes
    
    # Loop: Process each product in the catalog
    for _, row in df_skus.iterrows():
        sku = row['sku_id']
        
        # Define product "Velocity" (Average Daily Sales) using Gamma distribution
        avg_daily_sales = np.random.gamma(shape=2.0, scale=2.0)
        
        # Generate base sales (Poisson is ideal for discrete count data)
        daily_sales = np.random.poisson(lam=avg_daily_sales, size=len(date_range))
        
        # Inject "Noise" (Simulate Stockouts or Viral Spikes)
        # 10% chance of 0 sales (Stockout), 85% Normal, 5% Spike (5x sales)
        noise = np.random.choice([0, 1, 5], size=len(date_range), p=[0.1, 0.85, 0.05])
        final_sales = daily_sales * noise
        
        # Create temporary dataframe for this specific SKU
        temp_df = pd.DataFrame({
            "date": date_range,
            "sku_id": sku,
            "qty_sold": final_sales
        })
        records.append(temp_df)
    
    # Concatenate all temporary dataframes into one Master Fact Table
    df_demand = pd.concat(records, ignore_index=True)
    
    # Data Cleaning: Remove days with 0 sales to save space (Sparse Data)
    df_demand = df_demand[df_demand['qty_sold'] > 0]
    
    return df_demand

def main():
    """Main execution pipeline."""
    # 0. Setup
    init_generator()
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    
    # 1. Generate Master Data (Dimensions)
    df_catalog = generate_skus()
    file_skus = f"{OUTPUT_PATH}/dim_skus.csv"
    df_catalog.to_csv(file_skus, index=False)
    print(f"Master Data Generated: {file_skus} ({len(df_catalog)} records)")
    
    # 2. Generate Transactional Data (Facts)
    df_sales = generate_demand_history(df_catalog)
    file_sales = f"{OUTPUT_PATH}/fact_sales.csv"
    df_sales.to_csv(file_sales, index=False)
    print(f"Transaction History Generated: {file_sales} ({len(df_sales)} records)")

if __name__ == "__main__":
    main()