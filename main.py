# info={
#     "name":"piyush",
#     "subject":["c","python","java"],
#     "age":18,
#     "is_adult":True,
#     "marks":9.5,
# }
# print(info["name"]),
# print(info["subject"]),
# print(info["age"]),
# print(info["is_adult"]),
# print(["marks"])

# print(type(info))


# student={
#     "name":"piyush kumar",
#     "subject":{
#         "phy":95,
#         "che":85,
#         "maths":98,
#     }
# }
# print(student)
# print(student.keys())
# print(len(student))


# print(list(student.keys()))

# print(list(student.values()))
# print(student.items())


# print(student.get("name"))

# print(student.update({"city":"gopalganj"}))
# print(student)


#SETS 
# collection={2,3,3,3,3,6,9,8, "good","morning"}
# print(collection)
# print(type(collection))
# print(len(collection))


collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)


collection.remove(2)
print(collection)