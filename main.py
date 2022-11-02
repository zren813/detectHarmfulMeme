from features.classifySentence import classify_sentence
from features.extractText import extract_text
import json
toxic_correct = 0
toxic_wrong = 0
intoxic_correct = 0
intoxic_wrong = 0
wrong = 0
trial = 0
for line in open('./data/train.jsonl', 'r'):
    if trial == 100:
        break

    path = './data/' + json.loads(line)['img']
    label = json.loads(line)['label']
    toxicity = classify_sentence(extract_text(path))['toxicity']

    if toxicity >= 0.2 and label == 1:
        toxic_correct+=1
    elif toxicity >= 0.2 and label == 0:
        intoxic_wrong+=1
        print(toxicity)
        print(path)
    elif label == 0:
        intoxic_correct+=1
    else:
        toxic_wrong+=1
        print(toxicity)
        print(path)
    trial+=1
print(toxic_correct)
print(toxic_wrong)
print(intoxic_correct)
print(intoxic_wrong)

