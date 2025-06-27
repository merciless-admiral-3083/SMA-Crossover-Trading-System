import unittest
import pandas as pd

class TestDataValidation(unittest.TestCase):

    def setUp(self):
        file_path = ".\\data\\HINDALCO_1D.xlsx"
        self.df = pd.read_excel(file_path)
    
    def test_data_types(self):
        numeric_cols = ['open', 'high', 'low', 'close']
        for col in numeric_cols:
            self.df[col] = self.df[col].astype(float)
            self.assertTrue(pd.api.types.is_float_dtype(self.df[col]), f"{col} should be a decimal.")

        self.df['volume'] = self.df['volume'].astype(int)
        self.assertTrue(pd.api.types.is_integer_dtype(self.df['volume']), "Volume should be an integer.")

        self.assertTrue(self.df['instrument'].dtype == 'O', "Instrument should be a string.")  # Object dtype
        self.df['datetime'] = pd.to_datetime(self.df['datetime'])
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df['datetime']), "Datetime should be of datetime type.")


if __name__ == '__main__':
    unittest.main()
