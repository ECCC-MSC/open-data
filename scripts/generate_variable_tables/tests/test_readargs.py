import unittest
import os
from datetime import datetime, timedelta

import yaml

from main import read_args

# Datasets lookup table
model_file = './datasets.yml'

class TestReadArgs(unittest.TestCase):
    def setUp(self):
        # Load variable translation lookup table
        with open(model_file, 'r') as file:
            self.model_LUT = yaml.safe_load(file)
    
    def test_read_args(self):
        expected_models = ['RDPA']
        expected_directory = 'tests'
        expected_url = 'https://dd.alpha.meteo.gc.ca/'
        input = [
            '--models', 'RDPA',
            '--directory', 'tests',
            '--url', 'https://dd.alpha.meteo.gc.ca/',
            '--verbose'
        ]
        args = read_args(input, self.model_LUT)
        self.assertEqual(args.models, expected_models)
        self.assertEqual(args.directory, expected_directory)
        self.assertEqual(args.url, expected_url)
        self.assertTrue(args.verbose)
        self.assertTrue(os.path.exists(args.directory))
        
    def test_read_args_default(self):
        expected_models = [
            'CanSIPS', 'GDPS', 'GDPS-WEonG', 'RDPS', 'RDPS-WEonG', 'RDPS-Astronomy',
            'GDWPS', 'RDWPS', 'GEPS', 'REPS', 'GEWPS', 'REWPS', 'HRDPA', 'RDPA',
            'HRDPS', 'RAQDPS', 'RAQDPS-FW', 'GDPS-Ice-Analysis', 'CIOPS', 'GIOPS',
            'RIOPS', 'GDSPS', 'RESPS', 'WCPS', 'HRDLPS', 'HREPA', 'NSRPS'
        ]
        expected_directory = '.'
        date = datetime.now() - timedelta(1)
        yesterday = date.strftime("%Y%m%d")
        expected_url = f'http://hpfx.collab.science.gc.ca/{yesterday}/WXO-DD/'
        args = read_args([], self.model_LUT)
        self.assertEqual(args.models, expected_models)
        self.assertEqual(args.directory, expected_directory)
        self.assertEqual(args.url, expected_url)
        self.assertFalse(args.verbose)

    def test_read_args_invalid_model(self):
        input = ['--models', 'GEM-Global']
        with self.assertRaises(SystemExit):
            read_args(input, self.model_LUT)

    def test_read_args_invalid_url(self):
        input = ['--url', 'http://hpfx.collab.science.gc.ca/WXO-DD/']
        with self.assertRaises(SystemExit):
            read_args(input, self.model_LUT)

if __name__ == '__main__':
    unittest.main()
