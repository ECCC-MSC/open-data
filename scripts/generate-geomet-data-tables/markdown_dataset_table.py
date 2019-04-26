# -*- coding: utf-8 -*-
# =================================================================
#
# Copyright (c) 2017 Government of Canada
#
# =================================================================

from markdown_table import MarkdownTable


# related data class
class DataDataset:
    def __init__(self):
        self.id = None
        self.name = None
        self.model_runs = None
        self.forecast_hours = None
        self.forecast_hour_interval = None
        self.extent = None
        self.number_of_layer = None
        self.link = None


class MarkdownDatasetTable(MarkdownTable):
    english_header = ['Dataset', 'Id', 'MR', 'FH', 'FHI', 'N.']
    french_header = ['Dataset', 'Id',  'MR', 'FH', 'FHI', 'N.']

    def __init__(self, lang):
        self.lang = lang
        if lang == 'fr':
            super(MarkdownDatasetTable, self).__init__(self.french_header)
        elif lang == 'en':
            super(MarkdownDatasetTable, self).__init__(self.english_header)
        else:
            raise AssertionError('Unknown Language, markdown generation halted')

    def data_to_row(self, data):
        row = [None] * 6
        row[0] = '[' + data.name[self.lang].split('/')[0] + ']' + '(' + data.link + ')' if '/' in data.name else data.name
        row[1] = data.id
        row[2] = self.model_run_format(data.model_runs)
        row[3] = self.forecast_hours_format(data.forecast_hours)
        row[4] = self.forecast_hours_interval_format(data.forecast_hour_interval)
        row[5] = str(data.number_of_layer)
        return row

    @staticmethod
    def extent_format(data):
        string_result = str(data[0]) + ' '
        string_result += str(data[1]) + ' '
        string_result += str(data[2]) + ' '
        string_result += str(data[3])
        return string_result

    @staticmethod
    def model_run_format(model_run):
        if not model_run:
            return 'N/A'
        else:
            result_string = ''
            for mr in model_run:
                result_string += str(mr) + ','
            return result_string[:-1]

    @staticmethod
    def forecast_hours_format(forecast_hours):
        if not forecast_hours:
            return 'N/A'
        else:
            result_string = ''
            for fh in forecast_hours:
                result_string += str(fh) + ','
            return result_string[:-1]

    @staticmethod
    def forecast_hours_interval_format(forecast_hours_interval):
        if not forecast_hours_interval:
            return 'N/A'
        else:
            return str(forecast_hours_interval)
