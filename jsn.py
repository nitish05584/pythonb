import json

d={
    "name":"John",
    "age":30,
    "city":"New York"

}
f=json.dumps(d)
print(f)