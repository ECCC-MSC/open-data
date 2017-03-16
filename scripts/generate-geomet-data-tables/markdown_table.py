from array import array
import copy


class MarkdownTable(object):
    def __init__(self, headers):
        if type(headers) is not list:
            raise ValueError("List expected")
        self.column_num = len(headers)
        if self.column_num == 0:
            raise ValueError("Header list cannot be empty!")
        self.headers = headers
        self.column_sizes = array('i', map(len, headers))
        self.data = []

    def add_data(self, original_data):
        data = copy.copy(original_data)
        self.data.append(data)
        return self

    def add_data_list(self, data_list):
        for row in data_list:
            self.add_data(row)
        return self

    def generate_table(self):
        out = ''
        for data in self.data:
            row = self.data_to_row(data)
            for j in range(len(self.column_sizes)):
                self.column_sizes[j] = max(len(row[j]), self.column_sizes[j])

        out += u' | '.join(('%%-%ds' % l) % h for h, l in zip(self.headers, self.column_sizes)) + '\n'
        out += u'-|-'.join('-' * l for l in self.column_sizes) + '\n'
        for data in self.data:
            row = self.data_to_row(data)
            out += u' | '.join(('%%-%ds' % l) % h
                               for h, l in zip(row, self.column_sizes)) + '\n'
        return out

    def data_to_row(self, data):
        return data
