import logging
import math
import random
import platform
from datetime import datetime
import csv
import pandas as pd
from docx import Document
from project.read_file_interface import ReadFile


def handle_error(error_msg):
    timestamp = f"<Chani , {datetime.now()}>"
    print(f"{timestamp} {error_msg} ,<Chani>")
    logging.error(f"{timestamp} {error_msg}")

class Read(ReadFile):

    def read_file(self,file_path: str):
        try:
            file_extension = file_path.split('.')[-1].lower()

            if file_extension == 'txt':
                with open(file_path, 'r') as file:
                    content = file.read()
                    return content
            elif file_extension == 'csv':
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    data = [row for row in reader]
                return data

            elif file_extension == 'docx':
                try:
                    document = Document(file_path)
                    data = []

                    for paragraph in document.paragraphs:
                        data.append(paragraph.text)

                    return data
                except Exception as e:
                    handle_error(f"Error reading Word file '{file_path}': {e}")
                    return None

            handle_error(f"Unsupported file type: {file_extension}")
            return None

        except Exception as e:
            handle_error(f"Error reading file '{file_path}': {e}")
            return None





def extract_sales_data_with_range(product_name, data_table):
    try:
        sales_data = []

        for row in data_table:
            if product_name == row[0]:  # Assuming product name is in the first column
                quantity = row[1]
                total_amount = row[2]
                sales_data.append(quantity)

                # Extract the highest amount paid within the same product
                highest_amount_paid = max(data[2] for data in data_table if data[0] == product_name)
                # Include the range between the drawn number and highest amount paid
                sales_data.append((quantity, highest_amount_paid))

        return sales_data

    except Exception as e:
        handle_error(f"Error extracting sales data for '{product_name}': {e}")
        return None
def numerical_values_generator(main_table):
    df=pd.DataFrame(main_table)
    numeric_values = pd.to_numeric(df.columns[['Price','Total','Quantity']], errors='coerce')
    numeric_values = numeric_values.dropna()
    print(f'df is {numeric_values}')
def print_python_version():
    try:
        version_info = platform.python_version()
        print(f"Python Version: {version_info}")
    except Exception as e:
        handle_error(f"Error printing Python version: {e}")

def process_parameters(*args, **kwargs):
    result_dict = {}

    for arg in args:
        if isinstance(arg, (int, float)):
            print(f"Value: {arg}")

    for tag, value in kwargs.items():
        if isinstance(value, (int, float)):
            result_dict[tag] = value

    return result_dict


def print_main(main_table):
    # 6. Add prints for the main table
    print("Main Table:")
    print(main_table[0])
    for row in main_table:
        print(row)

    # Display 3 first rows
    print("\nFirst 3 Rows:")
    for row in main_table[:4]:
        print(row)

    # Display 2 last rows
    print("\nLast 2 Rows:")
    print(main_table[0])
    for row in main_table[-2:]:
        print(row)

    # Display some random row
    random_row_index = random.randint(0, len(main_table) - 1)
    print(f"\nRandom Row:")
    print(main_table[0])
    print(main_table[random_row_index])

    # 7. Go through all numerical values using only one loop
    # Flatten the table structure





# Rest of the code remains unchanged

# Example usage:
try:
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
    file_content=Read()
    file_content = file_content.read_file(r'C:\Users\user1\pythonProject\pythonProject1\project\UsersName.txt')
    if file_content:
        print(file_content)


    print_python_version()
    table = Read()
    table = table.read_file(r'C:\Users\user1\pythonProject\pythonProject1\project\YafeNof.csv')
    print_main(table)
    for numeric_value in numerical_values_generator(table):
        print(numeric_value)

    result_dict = process_parameters(5, 'tag1', 10, tag2='value2', tag1='value1')
    print(f'Processed Parameters: {result_dict}')
except Exception as e:
    handle_error(e)
