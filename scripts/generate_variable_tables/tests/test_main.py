import unittest
import unittest.mock

import yaml

from main import read_args, append_date

# Datasets lookup table
model_file = './datasets.yml'

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

    def test_append_date(self):
        path = 'http://hpfx.collab.science.gc.ca/20231231/WXO-DD/'
        expected = self.model_LUT['CanSIPS'][0] + '2024/01/'
        result = append_date(path, self.model_LUT['CanSIPS'][0])
        self.assertEqual(result, expected, 'paths are not equal')
    
    def test_append_date_no_pattern(self):
        path = 'https://dd.alpha.meteo.gc.ca/'
        expected = self.model_LUT['CanSIPS'][0]
        result = append_date(path, self.model_LUT['CanSIPS'][0])
        self.assertEqual(result, expected, 'paths are not equal')

if __name__ == '__main__':
    unittest.main()
