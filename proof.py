#!/usr/bin/env python3
import sys

def main():
    if (len(sys.argv) < 4):
        print('Incorrect number of arguments')
        return

    
    exec_name = sys.argv[1]
    input_folder = sys.argv[2]
    output_folder = sys.argv[3]

    print(f'Executable name: {exec_name}')
    print(f'Input folder: {input_folder}')
    print(f'Output folder: {output_folder}')

if __name__ == '__main__':
    main()

def print_answers (self, input_file_names):
    outf = open(input_folder + "answers.txt")
    for (file in input_file_names)
        inf = open(input_folder + file)
        with open(outf, 'w') as fin:
            print(fin.read())
        inf.close()