my_set = {1,2,3,3,3}
print(my_set)

my_tuple = (1,2,3,3,3) #변경 불가능
print(my_tuple)

java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "하하"])

print(java & python)
print(java.intersection(python))
print(java | python)
print(java.union(python))
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)
java.remove("김태호")
print(java)

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))