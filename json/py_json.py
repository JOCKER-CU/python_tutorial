import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#json
human = {
    "name": "John",
    "age": 30,
    "gender": "Male",
    "city": "New York",
    "hobbies": ["reading", "painting"],
    "friends": ["Alice", "Bob", "Charlie"],
    "family": {
        "parents": ["Mother", "Father"],
        "children": ["Emma", "Olivia"]
    }
}
print(json.dumps(human, indent=4))