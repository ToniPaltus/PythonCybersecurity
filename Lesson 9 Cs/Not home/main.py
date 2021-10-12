import json

# 1

# Some Json - string
x = '{"name": "John", "age": 30, "sity": "New York"}'

# parge x:
y = json.loads(x)

# the result is a python dictionary
print(y["age"])
print(y)


# 2

print(json.dumps({'name': 'John', 'age': 30}))
print(json.dumps({'name': 'John', 'age': 30})[1])
print(json.dumps(['apple', 'bananas']))
print(json.dumps(('apple', 'bananas')))
print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# 3

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "children":('Ann', 'Billy'),
    "pets": None
}
# convert into JSON
y = json.dumps(x, indent=4)
print(y)


# 4

from urllib.request import urlopen

# Store the URL in url as parameter for urlopen
url = 'https://api.vk.com/method/users.get'
url2 = 'https://api.vk.com/method/users.getSubscriptions'

#store the response of URL
response = urlopen(url)
response2 = urlopen(url2)

#storing the Json response from url in data
data_json = json.loads(response.read())
data_json2 = json.loads(response2.read())

print(data_json)
print()
print(data_json2)












