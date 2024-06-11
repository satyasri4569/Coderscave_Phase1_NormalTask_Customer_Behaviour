
Open In Colab
Dataset


import pandas as pd
import matplotlib.pyplot as plt

# Load all datasets
try:
    ideal_data = pd.read_csv('/content/Hackathon_Ideal_Data.csv')
    mapping_data = pd.read_csv('/content/Hackathon_Mapping_File.csv')
    validation_data = pd.read_csv('/content/Hackathon_Validation_Data.csv')
    working_data = pd.read_csv('/content/Hackathon_Working_Data.csv')
    sample_submission = pd.read_csv('/content/Sample Submission.csv')
except FileNotFoundError as e:
    print("One or more files not found. Please check file paths and try again.")
    raise e

     

# Display basic information about the datasets
datasets = {
    'Ideal Data': ideal_data,
    'Mapping Data': mapping_data,
    'Validation Data': validation_data,
    'Working Data': working_data,
    'Sample Submission': sample_submission
}

for name, data in datasets.items():
    print(f"\n{name}:")
    if data is not None:
        print("Shape:", data.shape)
        print("Columns:", data.columns)
        print("Head:")
        print(data.head())
    else:
        print("Dataset not available.")

     
Ideal Data:
Shape: (14260, 10)
Columns: Index(['MONTH', 'STORECODE', 'QTY', 'VALUE', 'GRP', 'SGRP', 'SSGRP', 'CMP',
       'MBRD', 'BRD'],
      dtype='object')
Head:
  MONTH STORECODE  QTY  VALUE                GRP               SGRP  \
0    M1        P1   25     83  HAIR CONDITIONERS  HAIR CONDITIONERS   
1    M1        P1    6     22  HAIR CONDITIONERS  HAIR CONDITIONERS   
2    M1        P1    4     15  HAIR CONDITIONERS  HAIR CONDITIONERS   
3    M1        P1   15     60  HAIR CONDITIONERS  HAIR CONDITIONERS   
4    M1        P2    0      0  HAIR CONDITIONERS  HAIR CONDITIONERS   

               SSGRP                         CMP         MBRD  \
0  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE   
1  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE   
2  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE   
3  HAIR CONDITIONERS               L'OREAL INDIA      GARNIER   
4  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED  CLINIC PLUS   

                     BRD  
0  DOVE HAIR FALL RESCUE  
1    DOVE INTENSE REPAIR  
2   DOVE OXYGEN MOISTURE  
3                FRUCTIS  
4            CLINIC PLUS  

Mapping Data:
Shape: (24, 3)
Columns: Index(['File Name', 'Column Name', 'Column Description'], dtype='object')
Head:
              File Name Column Name           Column Description
0  Hackathon_Ideal_Data       MONTH        Month ID (M1, M2, M3)
1                   NaN   STORECODE  STORE CODE (P1, P2, …, P10)
2                   NaN         QTY                   Sales Unit
3                   NaN       VALUE                  Sales Value
4                   NaN         GRP                     Category

Validation Data:
Shape: (2430, 4)
Columns: Index(['ID', 'STORECODE', 'MONTH', 'GRP'], dtype='object')
Head:
        ID STORECODE MONTH                       GRP
0  1112535        N1    M1       AFTER SHAVE LOTIONS
1  1112539        N1    M1    AGARBATTI & DHOOPBATTI
2  1112543        N1    M1  ALL AIR FRESHNERS(01/03)
3  1112547        N1    M1          ALL IODISED SALT
4  1112551        N1    M1                  ANTACIDS

Working Data:
Shape: (18099, 14)
Columns: Index(['MONTH', 'STORECODE', 'DAY', 'BILL_ID', 'BILL_AMT', 'QTY', 'VALUE',
       'PRICE', 'GRP', 'SGRP', 'SSGRP', 'CMP', 'MBRD', 'BRD'],
      dtype='object')
Head:
  MONTH STORECODE  DAY BILL_ID  BILL_AMT  QTY  VALUE  PRICE  \
0    M1        N1    4    T375     225.0  1.0  225.0  225.0   
1    M1        N1    4    T379      95.0  1.0   95.0   95.0   
2    M1        N1    4    T381      10.0  1.0   10.0   10.0   
3    M1        N1    4    T382     108.0  1.0  108.0  108.0   
4    M1        N1    4    T384      19.0  1.0   19.0   19.0   

                       GRP                     SGRP                    SSGRP  \
0     BUTTER MARGR  (4/94)                   BUTTER                   SALTED   
1  CONFECTIONERY - ECLAIRS  CONFECTIONERY - ECLAIRS  CONFECTIONERY - ECLAIRS   
2                CHOCOLATE         CHOCOLATE PANNED         CHOCOLATE PANNED   
3             PACKAGED TEA               MAIN PACKS               MAIN PACKS   
4         ALL IODISED SALT            POWDERED SALT            POWDERED SALT   

                      CMP           MBRD                 BRD  
0               G C M M F           AMUL                AMUL  
1             PARLE PRODS         MELODY    MELODY CHOCOLATY  
2  MONDELEZ INTERNATIONAL  CADBURY SHOTS       CADBURY SHOTS  
3      GUJ TEA PROCESSORS     WAGH BAKRI  WAGH BAKRI INSTANT  
4               TATA CHEM           TATA           TATA SALT  

Sample Submission:
Shape: (9, 2)
Columns: Index(['ID', 'TOTALVALUE'], dtype='object')
Head:
        ID  TOTALVALUE
0  1112535           0
1  1112539           1
2  1112543           2
3  1112547           3
4  1112551           4

# Print column names to verify
print("Working Data Columns:", working_data.columns)

# Assuming 'MONTH' has values like 'M1', 'M2', etc. and 'BILL_AMT' represents sales
month_column = 'MONTH'
sales_column = 'BILL_AMT'
year = 2024  # Use a fixed year if year information is not available

# Mapping for month names
month_mapping = {'M1': 1, 'M2': 2, 'M3': 3, 'M4': 4, 'M5': 5, 'M6': 6,
                 'M7': 7, 'M8': 8, 'M9': 9, 'M10': 10, 'M11': 11, 'M12': 12}

# Visualize total sales over time from working data
if working_data is not None and month_column in working_data.columns and sales_column in working_data.columns:
    # Convert month names to numerical month
    working_data['Month_Num'] = working_data[month_column].map(month_mapping)

    # Create a 'Date' column using the assumed year and the numerical month
    working_data['Date'] = pd.to_datetime(working_data['Month_Num'].apply(lambda x: f'{year}-{x:02d}'), format='%Y-%m')

    # Group by the new 'Date' column and sum sales
    monthly_sales = working_data.groupby(working_data['Date'].dt.to_period('M'))[sales_column].sum()

    # Plot the data
    monthly_sales.plot(kind='line', marker='o', figsize=(10, 6))
    plt.title('Monthly Sales Over Time (Working Data)')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.show()
else:
    print("Working data or necessary columns not available for visualization.")

     
Working Data Columns: Index(['MONTH', 'STORECODE', 'DAY', 'BILL_ID', 'BILL_AMT', 'QTY', 'VALUE',
       'PRICE', 'GRP', 'SGRP', 'SSGRP', 'CMP', 'MBRD', 'BRD'],
      dtype='object')


# Ensure the necessary columns are present
product_column = 'GRP'
sales_column = 'BILL_AMT'
month_column = 'MONTH'
year = 2024  # Use a fixed year if year information is not available

# Mapping for month names
month_mapping = {'M1': 1, 'M2': 2, 'M3': 3, 'M4': 4, 'M5': 5, 'M6': 6,
                 'M7': 7, 'M8': 8, 'M9': 9, 'M10': 10, 'M11': 11, 'M12': 12}

if product_column in working_data.columns and sales_column in working_data.columns and month_column in working_data.columns:
    # Convert month names to numerical month
    working_data['Month_Num'] = working_data[month_column].map(month_mapping)

    # Create a 'Date' column using the assumed year and the numerical month
    working_data['Date'] = pd.to_datetime(working_data['Month_Num'].apply(lambda x: f'{year}-{x:02d}'), format='%Y-%m')

    # Group by 'Date' and 'Product' to sum sales
    product_sales_over_time = working_data.groupby([working_data['Date'].dt.to_period('M'), product_column])[sales_column].sum().unstack()

    # Plot the data
    product_sales_over_time.plot(kind='line', marker='o', figsize=(14, 8))
    plt.title('Product Sales Growth Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.legend(title='Product Category')
    plt.grid(True)
    plt.show()
else:
    print(f"Necessary columns not available in working data: {product_column}, {sales_column}, {month_column}")

     


# Visualize distribution of sales amounts
if sales_column in working_data.columns:
    working_data[sales_column].plot(kind='hist', bins=50, figsize=(10, 6), edgecolor='black')
    plt.title('Distribution of Sales Amounts')
    plt.xlabel('Sales Amount')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
else:
    print(f"Column '{sales_column}' not available in working data.")

     


# Ensure the necessary columns are present
product_column = 'GRP'
sales_column = 'BILL_AMT'
month_column = 'MONTH'
year = 2024  # Use a fixed year if year information is not available

# Mapping for month names
month_mapping = {'M1': 1, 'M2': 2, 'M3': 3, 'M4': 4, 'M5': 5, 'M6': 6,
                 'M7': 7, 'M8': 8, 'M9': 9, 'M10': 10, 'M11': 11, 'M12': 12}

if product_column in working_data.columns and sales_column in working_data.columns and month_column in working_data.columns:
    # Convert month names to numerical month
    working_data['Month_Num'] = working_data[month_column].map(month_mapping)

    # Create a 'Date' column using the assumed year and the numerical month
    working_data['Date'] = pd.to_datetime(working_data['Month_Num'].apply(lambda x: f'{year}-{x:02d}'), format='%Y-%m')

    # Group by 'Date' and 'Product' to sum sales
    product_sales_over_time = working_data.groupby([working_data['Date'].dt.to_period('M'), product_column])[sales_column].sum().unstack().fillna(0)

    # Plot histograms for each product category
    product_sales_over_time.plot(kind='hist', bins=20, figsize=(14, 8), alpha=0.7, edgecolor='black')
    plt.title('Histogram of Monthly Sales Amounts by Product Category')
    plt.xlabel('Total Sales')
    plt.ylabel('Frequency')
    plt.legend(title='Product Category')
    plt.grid(True)
    plt.show()
else:
    print(f"Necessary columns not available in working data: {product_column}, {sales_column}, {month_column}")

     


# Calculate and visualize average sales per transaction
if 'BILL_ID' in working_data.columns:
    avg_sales_per_transaction = working_data.groupby('BILL_ID')[sales_column].mean()
    avg_sales_per_transaction.plot(kind='hist', bins=50, figsize=(10, 6), edgecolor='black')
    plt.title('Average Sales per Transaction')
    plt.xlabel('Average Sales Amount')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
else:
    print("Column 'BILL_ID' not available in working data.")

     
