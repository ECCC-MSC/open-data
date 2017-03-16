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
# Copyright (c) 2015 Government of Canada
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
import sys
import codecs
import re
import shutil
from os import walk, path, mkdir, makedirs


def clean_all_markdown(input_folder, output_folder):
    file_list = [map(lambda x: path.join(base, x), md_file) for (base, _, md_file) in walk(input_folder)]
    file_list = [item for sublist in file_list for item in sublist]

    # remove old output data
    if path.exists(output_folder):
        shutil.rmtree(output_folder)
    mkdir(output_folder)

    # pairs input and output paths
    io_paths = [(md_file, path.join(output_folder, md_file.replace(input_folder + '/', '').replace('.md', '.txt')))
                for md_file in file_list]

    # clean all markdown if it is one
    for input_md, output_md in io_paths:
        if '.md' in input_md:
            clean_single_markdown(input_md, output_md)
        else:
            dir_path = '/'.join(output_md.split('/')[:-1])
            if not path.exists(dir_path):
                makedirs(dir_path)
            shutil.copy(input_md, dir_path)


def clean_single_markdown(markdown_input, markdown_output):
    new_text = ''
    with codecs.open(markdown_input, 'r', 'utf-8') as input_md:
        for line in input_md:
            # start to add end lines only when the first line has been written in the file
            if new_text == '':
                new_text = handle_line(line)
            else:
                new_text += '\n' if line.isspace() else handle_line(line)

    dir_path = '/'.join(markdown_output.split('/')[:-1])
    if not path.exists(dir_path):
        makedirs(dir_path)
    with codecs.open(markdown_output, 'w', 'utf-8') as output_md:
        output_md.write(new_text)


def handle_line(line):
    # find a link pattern
    patterns = re.findall('.*\[.*\]\(\S*\).*', line)
    if patterns:
        # remove lang header
        line = '' if '[In English]' in line else line
        line = '' if '[En français]'.decode('utf-8') in line else line
        # remove bread crumb line
        line = '' if '[TdM]' in line else line
        line = '' if '[TOC]' in line else line

        # replace image link pattern by nothing
        img_pattern = re.findall('.*!\[.*\]\(\S*\)', line)
        line = line.replace(img_pattern[0], '') if img_pattern else line

        # replace anchor link by only the references anchor
        hashtag_link_patterns = re.findall('.*\[.*\]\(#\S*\).*', line)
        line = re.sub('\[.*\]|#|\(|\)', '', line) if hashtag_link_patterns else line

        # remove [] for the url links
        url_link_patterns = re.findall('.*\[.*\]\(http\S*\).*', line)
        line = line.replace('](', '] (') if url_link_patterns else line
        line = re.sub('\[|\]', '', line) if url_link_patterns else line

        # add links to the relatives url paths
        relative_link_patterns = re.findall('.*\[.*\]\(\S*\).*', line)
        line = line.replace('](', '] (' + DD_BASEPATH) if relative_link_patterns else line
        line = re.sub('\[|\]', '', line) if relative_link_patterns else line

    return '' if line.isspace() else line


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Usage: %s <input_markdown_directory>  <output_markdown_directory> <dd_base_path>')
        sys.exit(1)
    DD_BASEPATH = sys.argv[3]
    clean_all_markdown(path.normpath(sys.argv[1]), path.normpath(sys.argv[2]))
