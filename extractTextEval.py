from features.extractText import extract_text
import json
import numpy as np

trial = 0
text_list = []
pred_list = []

# compute character error rate per image
for line in open('./data/train.jsonl', 'r'):
    if trial == 500:
        break

    path = './data/' + json.loads(line)['img']
    text = json.loads(line)['text']
    text_list.append(text.lower())
    # print(text)

    pred = extract_text(path)
    pred_list.append(pred.lower())
    # print(pred)

    trial += 1

error_list = []
for i in range(len(text_list)):
    total_char = min(len(text_list[i]), len(pred_list[i]))
    if total_char == 0:
        continue
    error_char = 0
    for j in range(total_char):
        if text_list[i][j] != pred_list[i][j]:
            error_char += 1
    error_list.append(error_char / total_char)

print(np.mean(error_list))