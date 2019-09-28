#!/usr/bin/env python3
import sys
import os

PROGRAM_OUTPUT_PATH = 'actual.out'

def main():
    if (len(sys.argv) < 4):
        print('Incorrect number of arguments')
        return

    exec_name = sys.argv[1]
    input_folder = sys.argv[2]
    output_folder = sys.argv[3]

    input_files = get_dir_content(input_folder)
    output_files = get_dir_content(output_folder)

    for i in range(len(input_files)):
        input_path = os.path.join(input_folder, input_files[i])
        output_path = os.path.join(output_folder, output_files[i])
        run_test(exec_name, input_path)
        display_results(i, output_path)


def get_dir_content(dir):
    name_list = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    return sorted(name_list)


def run_test(exec_name, input_file):
    os.system(f'{exec_name} < {input_file} > {PROGRAM_OUTPUT_PATH}')

def display_results(test_number, output_path):
    print(f'Running test: #{test_number}')
    
    print('')
    print('Expected Results:')
    with open(output_path, 'r') as f:
        print(f.read())

    print('')
    print('Actual Results:')
    with open(PROGRAM_OUTPUT_PATH, 'r') as f:
        print(f.read())



# def print_answers (self, input_file_names):
#     outf = open(input_folder + "answers.txt")
#     for (f in input_file_names)
#         inf = open(input_folder + f)
#         with open(outf, 'w') as fin:
#             print(fin.read())
#         inf.close()


if __name__ == '__main__':
    main()