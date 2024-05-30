import unittest
import unittest.mock

from fileexplorer import find_files

class TestFileExplorer(unittest.TestCase):
    def test_find_files(self):
        expected = [
            'tests/mock_files/MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2',
            'tests/mock_files/MSC_RDPA_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2'
        ]
        result = find_files(['mock_files'], 'tests')
        self.assertEqual(result, expected, 'lists of files are not equal')
