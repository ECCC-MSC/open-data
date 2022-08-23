import unittest
import filecmp
import os

import yaml

from fileparser import FileParser, write_variable_table

# Variable translation lookup table
variable_file = './variable_translation.yml'
product_file = './product_translation.yml'
# Readable level lookup table
level_file = './readable_level.yml'

class TestFileParser(unittest.TestCase):
    def setUp(self):
        # Load variable translation lookup table
        with open(variable_file, 'r') as file:
            self.variable_LUT = yaml.safe_load(file)
        # Load product translation lookup table
        with open(product_file, 'r') as file:
            self.product_LUT = yaml.safe_load(file)
        # Load readable level lookup table
        with open(level_file, 'r') as file:
            self.level_LUT = yaml.safe_load(file)

    def tearDown(self):
        # Delete files
        file_en = 'tests/RDPA_en.csv'
        file_fr = 'tests/RDPA_fr.csv'
        if os.path.exists(file_en):
            os.remove(file_en)
        if os.path.exists(file_fr):
            os.remove(file_fr)

    def test_parse_metadata(self):
        parser = FileParser(
            self.variable_LUT,
            self.product_LUT,
            self.level_LUT
        )
        expected_en = 'tests/RDPA_expected_en.csv'
        expected_fr = 'tests/RDPA_expected_fr.csv'
        files = [
            'tests/mock_files/MSC_RDPA_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2',
            'tests/mock_files/MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2'
        ]
        parser.parse_metadata(files, 'tests', 'RDPA')
        self.assertTrue(filecmp.cmp('tests/RDPA_en.csv', expected_en), 'english files are not equal')
        self.assertTrue(filecmp.cmp('tests/RDPA_fr.csv', expected_fr), 'french files are not equal')
        self.assertFalse(os.path.exists('tests/RDPA_prob_en.csv'), 'english product table should not exist')
        self.assertFalse(os.path.exists('tests/RDPA_prob_fr.csv'), 'french product table should not exist')

    def test_generate_row(self):
        parser = FileParser(
            self.variable_LUT,
            self.product_LUT,
            self.level_LUT
        )
        expected = 'Total precipitation,APCP,Surface,kg/m<sup>2</sup>'
        result = parser.generate_row(
            'EN',
            'Total precipitation [kg/(m^2)]',
            '0-SFC'
        )
        self.assertEqual(result, expected, 'incorrect variable')

    def test_generate_prod_row(self):
        parser = FileParser(
            self.variable_LUT,
            self.product_LUT,
            self.level_LUT
        )
        expected = 'Heat index,HEATX,2 m Above Ground Level,K'
        result = parser.generate_prod_row(
            'EN',
            '03 hr Heat index Percentile(10) [K]',
            '2-HTGL'
        )
        self.assertEqual(result, expected, 'incorrect variable')

    def test_write_variable_table(self):
        expected = 'tests/RDPA_expected_en.csv'
        data = ['Total precipitation,APCP,Surface,kg/m<sup>2</sup>']
        directory = 'tests/'
        name = 'RDPA_en.csv'
        header = 'Variable,Abbreviation,Level,Unit'
        write_variable_table(data, directory, name, header)
        self.assertTrue(filecmp.cmp('tests/RDPA_en.csv', expected), 'files are not equal')

if __name__ == '__main__':
    unittest.main()
