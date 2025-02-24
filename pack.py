#!/usr/bin/python

import os
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <input_DIRECTORY> <output_FILE>")
    exit(1)

input_folder = sys.argv[1]
output_file = sys.argv[2]

result_pak = []

def filename_sort_key(filename):
    try:
        return int(filename.split('.')[0])
    except (IndexError, ValueError):
        return filename

for file in sorted(os.listdir(input_folder), key=filename_sort_key):
    input_file = f"./{input_folder}/" + file
    with open(input_file, "rb") as f:
        result_pak.append(f.read())

with open(output_file, "wb") as f:
    f.write(b''.join(result_pak))

print(f"Arquivo {output_file} criado com sucesso!")