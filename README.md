# Prototype Pak Tool

Tool created to extract .gim files from .pak archives inside [Prototype](https://vndb.org/p26) PSP games.

Tested on: AIR

Currently only works with files that start with gim file header: `4D 49 47 2E 30 30 2E 31 50 53 50`.

Unpack:\
```$ python3 unpack.py <input_PAK> <output_DIRECTORY>```

Pack:\
```$ python3 pack.py <input_DIRECTORY> <output_PAK>```
