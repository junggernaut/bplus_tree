import os
from bptree import BPTree

def safe_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

safe_mkdir('output')
fname = 0
while os.path.exists(f'input/{fname}.txt'):
    insert_keys, delete_keys = [], []
    input_f = open(f'input/{fname}.txt')
    input_s = input_f.read().splitlines()
    for line in input_s:
        if line.startswith('Insert '):
            val = int(line[len('Insert '):])
            insert_keys.append(val)
        elif line.startswith('Delete '):
            val = int(line[len('Delete '):])
            delete_keys.append(val)
    tree = BPTree()
    output = tree.show(insert_keys, delete_keys)
    output_f = open(f'output/{fname}.txt', 'w')
    output_f.write(output)
    answer_f = open(f'answer/{fname}.txt')
    answer = answer_f.read()
    if output == answer:
        print(f'Test {fname} Correct')
    else:
        print(f'Incorrect For Test {fname}')
    fname += 1
