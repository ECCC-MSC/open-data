# -*- coding: utf-8 -*-
# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2017 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
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

#python 2.x
import urllib2
#python 3.x
#import urllib.request


# this section handle WHEN to parse and WHAT to input and WHERE to output
def execute(input_yaml, input_folder, output_folder, is_raw):
    with open(input_yaml, 'r') as content_file:
        content = content_file.read()

    # parse the data
    code = ruamel.yaml.round_trip_load(content)
    layers_data_list = parse_layers_yaml(code)
    dataset_list = parse_dataset_layer(code)

    # send the templates to output and make a file_list of those files at their output repository
    if output_folder != input_folder:
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
        shutil.copytree(input_folder, output_folder)

    file_list = [map(lambda x:path.join(base, x), md_file) for (base, _, md_file) in os.walk(input_folder)]
    file_list = [os.path.join(output_folder, item.replace(input_folder, ''))
                 for sublist in file_list for item in sublist]
    file_list = [f for f in file_list if '.md' in f or '.txt' in f]
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
                    response = urllib2.urlopen(link_collaboration)

                    #python 3.x
                    #response = urllib.request.urlopen(link_collaboration)

                except Exception as e:
                    print (e)
                    print(link_collaboration + ' in ' + md_file + 'for collaboration')
                try:
                    #python 2.x
                    response = urllib2.urlopen(link_datamart)

                    #python 3.x
                    #response = urllib.request.urlopen(link_datamart)

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
