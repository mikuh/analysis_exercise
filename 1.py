import json

with open('gov.txt', 'r') as f:
    records = [json.loads(line) for line in f]

print(records[0])