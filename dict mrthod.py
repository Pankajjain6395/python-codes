marks = {
    "pankaj": 100,
    "Priya": 78,
    "Shubham": 25
}

print(marks.get("pankaj"))
print(type(marks))
print(marks.items())
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("ram"))


marks.update({"pankaj":101,"saroj":400})
print(marks)

print(marks.get("shubham2"))  # print non

print(marks["Shubham2"])  #returan an error

