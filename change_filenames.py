#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='+')
args = parser.parse_args()

for arg in args.filename:
    parts = arg.split('::')
    part_count = len(parts)
    extensions = parts[part_count-1].split(".")
    extension_count = len(extensions)

    if extension_count < 2:
        raise ValueError

    output = extensions[0]
    output += '.'
    output += extensions[1]

    for i in range(part_count-2, -1, -1):
        output += parts[i]

    for i in range(2, extension_count):
        output += '.'
        output += extensions[i]

    print output
