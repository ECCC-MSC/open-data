from markdown_dataset_table import MarkdownDatasetTable


class MarkdownDatasetDDTable(MarkdownDatasetTable):

    def data_to_row(self, data):
        row = [None] * 6
        row[0] = data.name[self.lang].split('/')[0]
        row[1] = data.id
        row[2] = self.model_run_format(data.model_runs)
        row[3] = self.forecast_hours_format(data.forecast_hours)
        row[4] = self.forecast_hours_interval_format(data.forecast_hour_interval)
        row[5] = str(data.number_of_layer)
        return row

