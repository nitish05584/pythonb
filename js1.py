import json

d = '{"name":"python","fee":"30k","durations":"2 month"}'

x = json.loads(d)   # string → dict
print(x)