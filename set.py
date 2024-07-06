menu = "라면", "김밥"
print(menu[0])
print(menu[1])

#menu.add("돈까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

my_set = {1,2,3,3,3} #중복 X
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)