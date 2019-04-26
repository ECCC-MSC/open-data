# -*- coding: utf-8 -*-
# =================================================================
#
# Copyright (c) 2017 Government of Canada
#
# =================================================================
import ruamel.yaml
import sys
import os
import shutil
from util import *
from parser_layer import *
from markdown_layer_table import MarkDownLayerTable
from markdown_dataset_table import MarkdownDatasetTable
from markdown_dataset_dd_table import MarkdownDatasetDDTable

import fnmatch

#python 2.x
# import urllib2
#python 3.x
import urllib.request


# this section handle WHEN to parse and WHAT to input and WHERE to output
def execute(input_yaml, input_folder, output_folder, is_raw):
    with open(input_yaml, 'r') as content_file:
        content = content_file.read()

    # parse the data
    code = ruamel.yaml.round_trip_load(content)
    layers_data_list = parse_layers_yaml(code)
    dataset_list = parse_dataset_layer(code)

    # Send the templates in input folder to output folder
    if output_folder != input_folder:
        # Remove the output folder if it already exists
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
        # Create a copy of the content in input folder in the output 
        shutil.copytree(input_folder, output_folder)
    
    # make a file_list of template files at their output repository
    ### py V >= 3.5 (for filename in glob.iglob('src/**/*.c', recursive=True):)
    file_list = [] # This will contain the path to every .md and .txt
                   # file in output folder.
    for root, dirnames, filenames in os.walk(output_folder):
        # os.walk recursively list every file and subfolder in a
        # directory. root contains the path to the parent folder, 
        # dirnames the names of the subfolders (if the element is a
        # directory and filenames the names of the files.
        for filename in fnmatch.filter(filenames, '*.md'):
            # filename contain the name of a file that finishes by .md
            # the file is added to file_list
            file_list.append(os.path.join(root, filename))
        for filename in fnmatch.filter(filenames, '*.txt'):
            # filename contain the name of a file that finishes by .txt
            # the file is added to file_list
            file_list.append(os.path.join(root, filename))
    
    # modify the data

    layer_dict = layers_to_dict(code, layers_data_list)
    add_layer_size(dataset_list, layer_dict)
    add_dataset_links(dataset_list, file_list, 'en')
    # make a table dictionary
    tables_layers_fr = {layer_id + '_FR': MarkDownLayerTable('fr').add_data_list(data).generate_table()
                        for layer_id, data in layer_dict.items()}

    tables_layers_en = {layer_id + '_EN': MarkDownLayerTable('en').add_data_list(data).generate_table()
                        for layer_id, data in layer_dict.items()}

    tables = dict(tables_layers_fr, **tables_layers_en)

    if is_raw:
        tables['README_FR'] = MarkdownDatasetDDTable('fr').add_data_list(dataset_list).generate_table()
        tables['README_EN'] = MarkdownDatasetDDTable('en').add_data_list(dataset_list).generate_table()
    else:
        tables['README_FR'] = MarkdownDatasetTable('fr').add_data_list(dataset_list).generate_table()
        tables['README_EN'] = MarkdownDatasetTable('en').add_data_list(dataset_list).generate_table()

    # place the table
    for md_file in file_list:
        add_tables_to_file(tables, md_file)


def add_tables_to_file(table_dict, md_file):
    new_text = ''
    with codecs.open(md_file, 'r', 'utf-8') as input_md:
        for line in input_md:

            if line.startswith('![alt text](htt'):
                start = line.index('![alt text](') + len('![alt text](')
                end = line.index(')')
                link_collaboration = line[start:end]
                link_datamart = link_collaboration.replace('http://collaboration.cmc.ec.gc.ca/', 'http://dd.meteo.gc.ca/')
                line_datamart = line.replace('http://collaboration.cmc.ec.gc.ca/', 'http://dd.meteo.gc.ca/')
                try:
                    #python 2.x
                    #response = urllib2.urlopen(link_collaboration)

                    #python 3.x
                    response = urllib.request.urlopen(link_collaboration)

                except Exception as e:
                    print (e)
                    print(link_collaboration + ' in ' + md_file + 'for collaboration')
                try:
                    #python 2.x
                    #response = urllib2.urlopen(link_datamart)

                    #python 3.x
                    response = urllib.request.urlopen(link_datamart)

                except Exception as e:
                    print (e)
                    print(link_datamart + ' in ' + md_file + 'for Datamart')
                new_text += line_datamart

            else:
                ids = re.findall('\$([^$]*)\$', line)
                for id_table in ids:
                    if id_table in table_dict:
                        line = line.replace('$' + id_table + '$', table_dict[id_table])
                else:
                    new_text += line
    os.remove(md_file)
    with codecs.open(md_file, 'w', 'utf-8') as output_md:
        output_md.write(new_text)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: %s <yaml_input_file>  <markdown_template_folder> <markdown_output_folder> [raw|default]'
              % sys.argv[0])
        sys.exit(1)
    execute(sys.argv[1], path.normpath(sys.argv[2]) + '/', path.normpath(sys.argv[3]) + '/', sys.argv[4] == 'raw')
