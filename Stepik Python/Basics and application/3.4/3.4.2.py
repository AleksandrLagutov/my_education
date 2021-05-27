import json
inpf = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
data_join = json.dumps(inpf)
again_data = json.loads(data_join)
print(again_data[0])