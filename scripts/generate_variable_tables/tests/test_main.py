import unittest
import unittest.mock

import yaml

from main import read_args, append_date

# Datasets lookup table
model_file = 'lookup_tables/datasets.yml'

class TestMain(unittest.TestCase):
    def setUp(self):
        # Load variable translation lookup table
        with open(model_file, 'r') as file:
            self.model_LUT = yaml.safe_load(file)
    
    @unittest.mock.patch('main.os')
    def test_read_args(self, mock_os):
        directory = 'test_directory'
        input = ['--directory', directory]
        read_args(input, self.model_LUT)
        mock_os.makedirs.assert_called_with(directory, exist_ok=True)

    @unittest.mock.patch('main.input')
    def test_append_date(self, mock_input):
        path = 'ensemble/cansips/grib2/forecast/raw/'
        expected = 'ensemble/cansips/grib2/forecast/raw/2024/01/'
        mock_input.side_effect = ['2024', '1']
        result = append_date(path)
        self.assertEqual(result, expected, 'paths are not equal')

if __name__ == '__main__':
    unittest.main()
