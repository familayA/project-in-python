import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from salesdata import *


# Read Excel file using the default path
new_data=SalesData("C:\\Users\\user1\\pythonProject\\pythonProject1\\project\\YafeNof.csv")

print(new_data.identify_best_selling_product())
print(new_data.calculate_average_sales())
print(new_data.calculate_cumulative_sales())
print(new_data.calculate_total_sales_per_month())

