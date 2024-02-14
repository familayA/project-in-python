import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from salesdata import *
import os






data = SalesData("C:\\Users\\user1\\pythonProject\\pythonProject1\\project\\YafeNof.csv")

# Read Excel file using the default path


# Display the data
print(data.data_frame)

# implement Functions
product_total = data.calculate_cumulative_sales()
plt.title("all products and Total in second it's product and quantity")
plt.xlabel("product")
plt.subplot(1,2,1)
plt.plot(np.array(product_total['Product']),np.array(product_total['Total']))
plt.subplot(1,2,2)
plt.plot(np.array(product_total['Product']),np.array(product_total['Quantity']))
plt.show()


month_total = data.calculate_total_sales_per_month()
xpoints = month_total['Month']
ypoints = month_total['Total']
plt.plot(xpoints,ypoints)
plt.show()



# Assuming your dataset is named 'data'
try:
    plt.figure(figsize=(10, 6))

    sns.boxplot(data=data.data_frame, x='Product', y='Total')

    plt.title('Boxplot of Product Orders')

    plt.xlabel('Product')

    plt.ylabel('Value')

    plt.grid(True)

    plt.show()

except Exception as e:

    print("An error occurred while plotting box plot with Seaborn:", e)


try:

    # Plot violin plot using Seaborn

    plt.figure(figsize=(10, 6))

    sns.violinplot(data=data.data_frame, x='Product', y='Quantity', inner=None)

    plt.title('Distribution of Units Ordered')

    plt.xlabel('Product')

    plt.ylabel('Number of Units')

    plt.grid(True)

    plt.show()

except Exception as e:

    print("An error occurred while plotting violin plot with Seaborn:", e)


try:

    # Plot violin plot using Seaborn

    plt.figure(figsize=(10, 6))

    sns.barplot(data=data.data_frame, x='Quantity', y='Total')

    plt.title('quantity to total')

    plt.xlabel('quantity')

    plt.ylabel('totaal')

    plt.grid(True)

    plt.show()

except Exception as e:

    print("An error occurred while plotting violin plot with Seaborn:", e)

try:

    # Plot violin plot using Seaborn

    plt.figure(figsize=(10, 6))

    sns.barplot(data=data.data_frame, x='Product', y='Total')

    plt.title('product to total')

    plt.xlabel('product')

    plt.ylabel('total')

    plt.grid(True)

    plt.show()

except Exception as e:

    print("An error occurred while plotting violin plot with Seaborn:", e)

# Grouping by month and calculating total sales for each month
monthly_sales = data.data_frame.groupby('Month')['Total'].sum().reset_index()
# Sorting the data by month
monthly_sales = monthly_sales.sort_values(by='Month')
# sales for each month
# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', edgecolor='black')
plt.title('Total Sales for Each Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout for better appearance
plt.show()

# average sales for each month

average_sales = data.data_frame.groupby('Month')['Total'].mean().reset_index()

# Sorting the data by month
average_sales = average_sales.sort_values(by='Month')
# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(average_sales['Month'], average_sales['Total'], color='skyblue', edgecolor='black')
plt.title('Average Sales for Each Month')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout for better appearance
plt.show()

# amount of sales of a product for each month
# Choose a specific product
selected_product = 'Gmara'
# Filter the data for the selected product
product_data = data.data_frame[data.data_frame['Product'] == selected_product]
product_monthly_sales = product_data.groupby('Month')['Quantity'].sum().reset_index()
product_monthly_sales = product_monthly_sales.sort_values(by='Month')
# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(product_monthly_sales['Month'], product_monthly_sales['Quantity'], marker='o', color='skyblue', linestyle='-')
plt.title(f'Sales of {selected_product} for Each Month (quantity)')
plt.xlabel('Month')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout for better appearance
plt.grid()
plt.show()
print(data.data_frame['Month'])

monthly_quantity = data.data_frame.groupby('Month')['Quantity'].sum().reset_index()
monthly_quantity = monthly_quantity.sort_values(by='Month')
#  Quantity over Date
plt.plot(monthly_quantity['Month'], monthly_quantity['Quantity'])
plt.title('Quantity over Month')
plt.xlabel('Month')
plt.ylabel('Quantity')
plt.show()




# Filter data for the last month
sales_data = data.data_frame
sales_data['Month'] = pd.to_datetime(sales_data['Month'])
# Get the last month
last_month = sales_data['Month'].max().replace(day=1) - pd.DateOffset(months=1)
# Filter data for the last month
last_month_data = sales_data[sales_data['Month'] > last_month]
quantity_sold_last_month = last_month_data.groupby('Product')['Quantity'].sum().reset_index()
label_product = np.array(quantity_sold_last_month['Product'])
plt.pie(quantity_sold_last_month['Quantity'],labels=label_product )
plt.title(f'Quantity sold of each product in the last month after {last_month}')
plt.show()


# Scatter Plot: Price vs Quantity

plt.plot(data.data_frame['Product'], data.data_frame['Price'],linestyle = 'dotted')
plt.title('Price to Product')
plt.xlabel('Product')
plt.ylabel('Price')
plt.show()

# Bar Plot: Total Sales per Product
total_sales_per_product = data.data_frame.groupby('Product')['Quantity'].sum()
total_sales_per_product.plot(kind='bar')
plt.title('Bar Plot: Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Histogram: Distribution of Prices
plt.hist(data.data_frame['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram: Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()




# Seaborn Line Plot: Quantity over Date
sns.displot(data.data_frame['Month'],label = 'Month')
plt.title('Quantity over Date')
plt.show()

# Seaborn Scatter Plot: Price vs Quantity
sns.scatterplot(x='Price', y='Quantity', data=data.data_frame)
plt.title('Seaborn Scatter Plot: Price vs Quantity')
plt.show()

# Seaborn Bar Plot: Total Sales per Product
sns.barplot(x='Product', y='Quantity', data=data.data_frame, estimator=sum)
plt.title('Seaborn Bar Plot: Total Sales per Product')
plt.show()

# Seaborn Box Plot: Distribution of Prices
sns.boxplot(x=data.data_frame['Price'])
plt.title('Seaborn Box Plot: Distribution of Prices')
plt.xlabel('Price')
plt.show()