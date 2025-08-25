import pandas as pd

# Load the dataset
df = pd.read_excel("Supermarket-Sales-Sample-Data.xlsx")
print("Original Dataset Shape:", df.shape)

# Convert 'Order_Date' column to datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# Fill missing values where applicable
df['Customer_Name'].fillna("Unknown", inplace=True)

# Ensure numeric columns are correct
numeric_cols = ['Total(USD)', 'Tax(USD)', 'Retail_Price(USD)', 'Order_Quantity']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col].fillna(0, inplace=True)

# Drop rows with critical missing information
# df.dropna(subset=['Branch', 'Invoice ID'], inplace=True)

# Add new column: total_retail_price = retail_price * quantity
df['total_retail_price'] = df['Retail_Price(USD)'] * df['Order_Quantity']

# Export cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned dataset saved as cleaned_sales_data.csv")
