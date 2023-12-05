import os
import random
from bptree import BPTree

def safe_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def input_to_str(insert_keys, delete_keys):
    insert_s = list(map(lambda x: f'Insert {x}', insert_keys))
    delete_s = list(map(lambda x: f'Delete {x}', delete_keys))
    return '\n'.join(insert_s+delete_s)

safe_mkdir('input')
safe_mkdir('answer')
input_len = [2,3,4,5,10,20,30,40,50,100]
fname = 0
for include_del in [False, True]:
    for i in range(len(input_len)):
        insert_keys = list(range(input_len[i]))
        random.shuffle(insert_keys)
        delete_keys = []
        if include_del:
            delete_keys = list(range(input_len[i]))
            random.shuffle(delete_keys)
            delete_keys.pop()
        input_f = open(f'input/{fname}.txt', 'w')
        input_f.write(input_to_str(insert_keys, delete_keys))
        input_f.close()
        tree = BPTree()
        output = tree.show(insert_keys, delete_keys)
        answer_f = open(f'answer/{fname}.txt', 'w')
        answer_f.write(output)
        answer_f.close()
        fname += 1
