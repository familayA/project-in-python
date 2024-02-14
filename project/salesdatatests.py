import unittest
from salesdata import *
class TestSalesData(unittest.TestCase):
    def setUp(self):
        data = SalesData("C:\\Users\\user1\\pythonProject\\pythonProject1\\project\\YafeNof.csv")
        self.data_table = data

    def test_calculate_total_sales(self):
        self.assertNotEqual(self.data_table.calculate_total_sales,10)
    def test_calculate_cumulative_sales(self):
        self.assertIn('Product',self.data_table.calculate_cumulative_sales())
    def test_identify_best_selling_product(self):
        self.assertEqual(self.data_table.identify_best_selling_product(),'Tanach')
    def test_calculate_average_sales(self):
        self.assertGreater(self.data_table.calculate_average_sales(),100)



if __name__ == '__main__':
    unittest.main()