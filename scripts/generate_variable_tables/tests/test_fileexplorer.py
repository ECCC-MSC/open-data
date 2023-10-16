import unittest
import unittest.mock
import os

from fileexplorer import FileExplorer

class TestFileExplorer(unittest.TestCase):
    def test_find_files(self):
        directory = '/data/geomet/dev/afsuxad/'
        explorer = FileExplorer(directory)
        expected = [
            'tests/mock_files/MSC_RDPA-Prelim_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2',
            'tests/mock_files/MSC_RDPA_APCP-Accum6h_Sfc_RLatLon0.09_PT0H.grib2'
        ]

        result = explorer.find_files(['mock_files'], 'tests')
        self.assertEqual(result, expected, 'lists of files are not equal')

    @unittest.mock.patch('fileexplorer.os.path')
    @unittest.mock.patch('fileexplorer.shutil')
    def test_remove_files(self, mock_shutil, mock_path):
        directory = '/data/geomet/dev/afsuxad/'
        temporary = directory + str(os.getpid())
        mock_path.join.return_value = temporary
        explorer = FileExplorer(directory)
        
        # Test where directory does not exist
        mock_path.isdir.return_value = False
        explorer.remove_files()
        self.assertFalse(mock_shutil.rmtree.called, "Failed to not remove the directory if not present")

        # Test where directory exists
        mock_path.isdir.return_value = True
        explorer.remove_files()
        mock_shutil.rmtree.assert_called_with(temporary)
