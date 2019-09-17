#!/usr/bin/python3
import random
import os

MIN_NUM = 1
MAX_NUM = 15
INPUT = "input.txt"
OUTPUT = "output.txt"
MIXED = "russian_corpus.csv"
OUT_CSV = "output.csv"

def read_data(file):
    f = open(file, "r", encoding="utf-8")
    data = f.read()
    f.close()
    return data

def check_dots(data):
    return int(data.find('.'))

def write_to_file(file, data):
    f = open(file, "a")
    bytes = f.write(data)
    f.close()
    if bytes > 0:
        return 1
    else:
        return 0

def remove_empty_lines(input, output):
    fh = open(input, "r")
    lines = fh.readlines()
    fh.close()
    keep = []
    for line in lines:
        if not line.isspace():
            keep.append(line)
    fh = open(output, "w")
    fh.write("".join(keep))
    fh.close()

def randomize_lines_in_file(inputfile, outputfile):
    with open(inputfile,'r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open(outputfile,'w') as target:
        for _, line in data:
            target.write( line )

def replace_symbols(data):
    data = data.replace('!','.')
    data = data.replace('\\u0xE2', '.')
    data = data.replace('\\u0x80', '.')
    data = data.replace('\\u0xA6', '.')
    data = data.replace('. .', '.')
    data = data.replace('?','.')
    return data

def main():
    data = read_data(INPUT)
    current_pos = 0
    data = replace_symbols(data)
    global Data_size
    Data_size = len(data)
    while Data_size > 1:
        data = data[current_pos:].strip(" ")
        dot_pos = data[current_pos:].find('.')
        chars = len(data[current_pos:dot_pos + 1])
        write_to_file(OUT_CSV, data[current_pos:dot_pos + 1] + "\t " + str(chars) + "\n")
        current_pos = dot_pos + 1
        data = data[current_pos:].strip(" ")
        current_pos = 0
        Data_size = len(data)
    remove_empty_lines(OUT_CSV,OUT_CSV)
    randomize_lines_in_file(OUT_CSV,MIXED)
    os.remove(OUT_CSV)

if __name__ == "__main__":
    main()
