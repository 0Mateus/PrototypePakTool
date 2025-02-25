#!/usr/bin/env python3

import os
import sys

def StartsWithGimHeader(file):
    with open(file, "rb") as f:
        header = f.read(11)
        if header == gim_header:
            return True
        else:
            return False

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_FILE> <output_DIRECTORY>")
    exit(1)

file = sys.argv[1]
output = sys.argv[2]

gim_header = b"\x4D\x49\x47\x2E\x30\x30\x2E\x31\x50\x53\x50"
gim_file_size = 131792

with open(file, "rb") as f:
    content = f.read()

    index = 0
    occours_gim_header = []
    
    while True:
        index = content.find(gim_header, index)

        if index == -1:
            break

        occours_gim_header.append(index)
        index += 1

file_count = 0

if not StartsWithGimHeader(file):
    with open(file, "rb") as f:
            content = f.read()[:occours_gim_header[0]]
            with open(f"{output}/0.filler", "wb") as r:
                r.write(content)
                print(f"Header extraído!")
    file_count += 1

for i in occours_gim_header:
    with open(file, "rb") as f:
        content = f.read()[i:i + gim_file_size]
        with open(f"{output}/{file_count}.gim", "wb") as r:
            r.write(content)
    
    with open(file, "rb") as f:
        end_number = 0

        while i + gim_file_size > occours_gim_header[end_number]:
            end_number += 1

            if (i + gim_file_size > occours_gim_header[-1]):
                break

        with open(f"{output}/{file_count}.gim.filler", "wb") as r:
            if (i + gim_file_size > occours_gim_header[-1]):
                content_filler = f.read()[i + gim_file_size:]
            else:
                content_filler = f.read()[i + gim_file_size: occours_gim_header[end_number]]
            r.write(content_filler)

    print(f"Arquivo {file_count} extraído!")
    file_count += 1
