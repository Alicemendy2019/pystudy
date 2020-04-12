
import json
menu = [
    {"name":"humberg","price":390,"calorie":350},
    {"name":"cheese","price":280,"calorie":160},
    {"name":"potato","price":220,"calorie":230}
]

with open('menu.txt','w') as f:
    json.dump(menu,f,indent=4)


with open('menu.txt','r') as f:
    data = json.load(f)

print(data)
