# -*- coding: utf-8 -*-
import yaml

# 파이썬 데이터를 YAML 데이터로 출력
customer = [
    {"name": "InSeong", "age": "24", "gender": "man"},
    {"name": "Akatsuki", "age": "22", "gender": "woman"},
    {"name": "Harin", "age": "23", "gender": "man"},
    {"name": "Yuu", "age": "31", "gender": "woman"}
]

# python to yaml data
yaml_str = yaml.dump(customer)
print(yaml_str)
print("---------------------------")
# Yaml to python
data = yaml.load(yaml_str)

# 이름 출력
for p in data:
    print(p["name"])
