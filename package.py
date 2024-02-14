import numpy as np
import pandas as pd
import random

class FileOperation:
    def read_excel(self, file_path: str):

        try:
            data = pd.read_excel(file_path)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading Excel file: {e}")

    def save_to_excel(self, data, file_name:str):
        """
        Save the provided data to a new Excel file with the given file name.

        Parameters:
        - data: The data to be saved (can be a DataFrame or any object that Pandas supports).
        - file_name (str): The name of the Excel file to be created or overwritten.

        Returns:
        - None
        """
        try:
            data.to_excel(file_name)
            print(f"Data successfully saved to {file_name}")
        except Exception as e:
            print(f"Error saving data to Excel file: {e}")

class SalesData:
    def __init__(self, data):
        self.data = data

    def eliminate_duplicates(self):
        self.data = self.data.drop_duplicates().dropna()

    def calculate_total_sales(self):
        self.data['Total_Sales'] = self.data.groupby('Product')['Sales'].transform('sum')

    def _calculate_total_sales_per_month(self):
        self.data['Total_Sales_Per_Month'] = self.data.groupby('Month')['Sales'].transform('sum')

    def _identify_best_selling_product(self):
        best_selling_product = self.data.groupby('Product')['Sales'].sum().idxmax()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        month_with_highest_sales = self.data.groupby('Month')['Sales'].sum().idxmax()
        return month_with_highest_sales

    def analyze_sales_data(self):
        self.eliminate_duplicates()
        self.calculate_total_sales()
        self._calculate_total_sales_per_month()

        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()

        minimest_selling_product = self.data.groupby('Product')['Sales'].sum().idxmin()
        average_sales = self.data['Sales'].mean()

        analysis_result = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales,
            'minimest_selling_product': minimest_selling_product,
            'average_sales': average_sales
        }

        return analysis_result
# Example usage:
if __name__ == "__main__":
    # Creating an instance of the FileOperation class
    file_operation = FileOperation()

    # Reading data from an Excel file
    read_data = file_operation.read_excel("C:\\Users\\user1\\pythonProject\\pythonProject1\\data.xlsx")
    print("Data read from Excel file:")
    print(read_data)

    # Saving data to a new Excel file
    # Assuming 'some_data' is a Pandas DataFrame or any other object supported by Pandas
    some_data = pd.DataFrame({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})
    file_operation.save_to_excel(some_data, "C:\\Users\\user1\\pythonProject\\pythonProject1\\data.xlsx")
data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'],
    'Sales': [100, 150, 120, 80, 200, 90]
}

sales_data = SalesData(pd.DataFrame(data))
result = sales_data.analyze_sales_data()
print(result)