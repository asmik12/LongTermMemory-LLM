import json
from tqdm import tqdm
import numpy as np

follow_up_q_file = 'processed_oracle_follow_ups.jsonl'

with open(follow_up_q_file, "r") as f:
    json_objects = (json.loads(line.strip()) for line in f)  # Generator to parse JSONL

    entry_list = np.arange(0, 501)

    for json_obj, entry in tqdm(zip(json_objects, entry_list), total=len(entry_list)):
        if not isinstance(json_obj['follow_up_questions'], list):
            print(entry)
    