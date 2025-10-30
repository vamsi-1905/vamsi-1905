capitals = {"India":"delhi","USA":"Washington DC","Russia":"Moscow"}

#print(help(capitals))

print(capitals.get("India"))

if capitals.get("UK"):
    print("capital exists")
else:
    print("capital doesnt exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"India":"Bangalore"})
capitals.pop("India")
capitals.popitem()


keys= capitals.keys()


for key in capitals.keys():
    print(key)
print(capitals)


values = capitals.values()
print(values)

for value in capitals.values():
    print(value)


items = capitals.items()
print(items)