from parser_dataset import *
from os import path
import codecs
import re


# transform layers to a single directory
def layers_to_dict(code, layers_row_list):
    dict_layer_table = dict()
    for key, data in code['forecast_models'].items():
        model_mcf = data['mcf']
        group_name = get_forecast_model_name(code, model_mcf).upper()
        if group_name not in dict_layer_table:
            # filter the layer list to find the good model ( looking for the same mcf files)
            layer_for_model = [x for x in layers_row_list if code['layers'][x.id]['forecast_model']['mcf'] == model_mcf]
            dict_layer_table[group_name] = layer_for_model
    return dict_layer_table


# add the missing size for each dataset based on the layer size
def add_layer_size(dataset_list, divided_layer):
    for dataset in dataset_list:
        dataset.number_of_layer = len(divided_layer[dataset.id.upper()])


# Horrible function that find the  markdown links to their datasets
def add_dataset_links(dataset_list, file_list, lang='fr'):
    dataset_table_location = ''
    lang = lang.upper()
    for md_file in file_list:
        with codecs.open(md_file, 'r', 'utf-8') as file_open:
            if '$README_' + lang + '$' in file_open.read():
                dataset_table_location = md_file[:md_file.rfind('/')]
                break

    for md_file in file_list:
        with codecs.open(md_file, 'r', 'utf-8') as file_open:
            dataset_id = re.findall('\$([^$]*)\$', file_open.read())
            if dataset_id:
                dataset_id = dataset_id[0]
                for dataset in dataset_list:
                    if dataset.id.upper() + '_' + lang == dataset_id:
                        dataset.link = path.relpath(md_file, dataset_table_location)
