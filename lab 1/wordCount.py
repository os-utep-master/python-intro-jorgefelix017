#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:51:24 2019
@prgram name: Lab 1
@author: Jorge Felix

@purpose: to introduce the python language
"""

import re, sys

input_file = sys.argv[1]

output_file = sys.argv[2]

#make them all lowercase to ignore uppercasing
text_string = open(input_file, 'r').read().lower()

#looking to "find all" the words with 1 to 18 characters
caught_words = re.findall(r'\b[a-z]{1,18}\b', text_string)

#the dictionary
word_log = {}

for word in caught_words:
    count = word_log.get(word, 0)
    word_log[word] = count+1

frequency_list = sorted(word_log.keys(), reverse = True)

with open(output_file, 'w') as f:
    for word in word_log:
        f.write('%s %d \n' % (word, word_log[word]))