# class demo:
#     c_name = "xyz"
#     def __init__(self):
#         print("defautlt Constructor called")

# print(demo.c_name)

# obj = demo()
# print(obj.c_name)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = student("ram", 20)
# print(s1.name)

# s2 = student("sita", 23)
# print(s2.name)

# class student:
#     c_name = "xyz"

#     # class method
#     @classmethod
#     def change_c_name(cls):
#         return "class method"

#     @classmethod
#     def change_c_name(cls, new_value):
#       cls.c_name = new_value
#       return f"updated value is{cls.c_name}"
# print(student.change_c_name())
# print(student.change_c_name("Linkcode"))