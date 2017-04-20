from markdown_table import MarkdownTable


# related data class
class DataLayer:
    def __init__(self):
        self.id = None
        self.name = None
        self.webservice = None
        self.styles = None


class MarkDownLayerTable(MarkdownTable):
    english_header = ['Name', 'Id', 'Web Services', 'Styles']
    french_header = ['Nom', 'Id', 'Services web', 'Styles']

    def __init__(self, lang):
        self.lang = lang
        if lang == 'fr':
            super(MarkDownLayerTable, self).__init__(self.french_header)
        elif lang == 'en':
            super(MarkDownLayerTable, self).__init__(self.english_header)
        else:
            raise AssertionError('Unknown Language, markdown generation  halted')

    def data_to_row(self, data):
        row = [None]*4

        row[0] = data.name[self.lang]
        row[1] = data.id

        formatted_web_format = ''
        for web_format in data.webservice:
            formatted_web_format += web_format
            formatted_web_format += ', '
        row[2] = formatted_web_format[:-2]

        formatted_styles = ''
        formatted_styles += 'DEFAULT: ' + data.styles[-1].rsplit('/', 1)[-1].replace('.inc', '') + ', '
        for style in data.styles[:-1]:
            formatted_styles += style.rsplit('/', 1)[-1].replace('.inc', '') + ', '
        row[3] = formatted_styles[:-2]

        return row
