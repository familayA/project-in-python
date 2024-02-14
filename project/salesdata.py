import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
class FileOperation:
    def __init__(self,path:str):
        self.path_file = path

    def read_excel(self):
      print(self.path_file)
      self.data = pd.read_csv(self.path_file)
      return self.data


    def save_excel(self,data1,file_name:str):
        data_frame=pd.DataFrame(data1);
        data_frame.to_excel(file_name,index=False);
class SalesData:
    def __init__(self,path_name):
        data = FileOperation(path_name)
        data = data.read_excel()
        self.data_frame = pd.DataFrame(data);
        self.data_frame['Date'] = pd.to_datetime(self.data_frame['Date'], format='%d.%m.%Y', errors='coerce')
        self.data_frame['Month'] = self.data_frame['Date'].dt.strftime('%Y-%m')
    def eliminate_duplicates(self):
        self.data_frame=self.data_frame.drop_duplicates().dropna();
    def calculate_total_sales(self):
        result = self.data_frame.groupby('Product').agg({'Total': 'sum', 'Quantity': 'sum'}).reset_index()
        sum1 = result['Total'].sum()
        return sum1
    def calculate_total_sales_per_month(self):
        self.data_frame['Date'] = pd.to_datetime(self.data_frame['Date'], format='%d.%m.%Y', errors='coerce')
        self.data_frame['Month'] = self.data_frame['Date'].dt.strftime('%Y-%m')
        result = self.data_frame.groupby('Month').agg({'Total': 'sum', 'Quantity': 'sum'}).reset_index()
        return result

    def calculate_cumulative_sales(self):

        self.data_frame['Date'] = pd.to_datetime(self.data_frame['Date'], format='%d.%m.%Y', errors='coerce')
        self.data_frame['Month'] = self.data_frame['Date'].dt.strftime('%Y-%m')
        result = self.data_frame.groupby('Product').agg({'Total': 'sum', 'Quantity': 'sum'}).reset_index()
        return result
    def identify_best_selling_product(self):
        return self.data_frame.groupby('Product')['Quantity'].sum().idxmax();
    def identify_month_with_highest_sales(self):
        return self.data_frame.groupby('Month')['Total'].sum().idxmax();
    def identify_minimal_selling_product(self):
        return self.data_frame.groupby('Product')['Quantity'].sum().idxmin();
    def calculate_average_sales(self):
        return self.data_frame['Total'].mean();
    def analyze_sales_data(self,results_dicta=None):
        if results_dicta is None:
            results_dicta={};
        results_dicta['best_selling_product'] = self.identify_best_selling_product();
        results_dicta['month_with_highest_sales'] = self.identify_month_with_highest_sales();
        results_dicta['minimal_selling_product'] = self.identify_minimal_selling_product();
        results_dicta['average_sales'] = self.calculate_average_sales();
        return results_dicta;
    def add_90percents_values_column(self):
        self.data_frame['percent'] = (self.data_frame['Quantity'] / 100) * 90

    def bar_chart_category_sum(self):
        category_sum = self.data_frame.groupby('Product')['Quantity'].sum().reset_index()
        print(category_sum)

        sns.set(style="whitegrid")  # Use one of the predefined styles
        sns.set_theme(font_scale=1.2)  # Customize additional theme parameters
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Product', y='Quantity', data=category_sum.head(10), palette='viridis')
        plt.xticks(rotation=5, ha='right')  # Adjust rotation angle as needed
        plt.title('Sum of Quantities Sold for Each Product')
        plt.xlabel('Product')
        plt.ylabel('Sum of Quantity Sold')
        plt.show()
    def calculate_mean_quantity(self):
        total_array=self.data_frame['Total'].values();
        mean_total=np.mean(total_array);
        median_total=np.median(total_array);
        second_max_total=np.partition(total_array,-2)[-2];
    def filter_by_selling_or_and(self):
        all_products=self.data_frame.groupby('Product')['Price']['Quantity'].sum().reset_index();
        condition_1 = (all_products['Quantity'] > 5) | (all_products['Quantity'] == 0)
        condition_2 = (all_products['Price'] > 300) & (all_products['Quantity'] < all_products['Price']/2);
        filtered_data = [condition_1 | condition_2]

    def divide_by_2(self):
        # Check if data is available
        if self.data_frame.empty:
            print("No data available. Load or collect data first.")
            return
        # Iterate over columns and apply division only to numeric columns
        for column in self.data_frame.columns:
            if pd.api.types.is_numeric_dtype(self.data_frame[column]):
                self.data_frame['BlackFridayPrice'] = self.data_frame[column] / 2

    def calculate_stats(self, columns: str = None):
        if self.data_frame.empty:
            print("No data available. Load or collect data first.")
            return {}

        # If columns is None, apply operations to all columns
        if columns is None:
            columns = self.data_frame.columns

        # Initialize an empty dictionary to store statistics
        w = {}

        # Iterate over specified columns
        for column in columns:
            if column not in self.data_frame.columns:
                print(f"Column '{column}' not found in the DataFrame.")
                continue

            # Check if the column has data before calculating statistics
            if not self.data_frame[column].empty:
                if self.data_frame[column].dtype == 'datetime64[ns]':
                    min_date = self.data_frame[column].min()
                    max_date = self.data_frame[column].max()

                    # Update the dictionary with the calculated statistics for datetime columns
                    w[column] = {
                        'min_date': min_date,
                        'max_date': max_date,
                    }
                elif pd.api.types.is_numeric_dtype(self.data_frame[column]):
                    # For numeric columns, calculate other statistics
                    max_value = self.data_frame[column].max()
                    sum_value = self.data_frame[column].sum()
                    absolute_values = self.data_frame[column].abs()
                    cumulative_max = self.data_frame[column].cummax()

                    # Update the dictionary with the calculated statistics
                    w[column] = {
                        'max_value': max_value,
                        'sum_value': sum_value,
                        'absolute_values': absolute_values,
                        'cumulative_max': cumulative_max,
                    }
                else:
                    print(f"Column '{column}' has non-numeric or string values. Skipping.")

        return w


