globalvar = "hey"


class demo:
    pass

    msg = "hello"

    def __init__(self):
        print("created!")

    def __init__(self, age):
        self.name = "xyz"
        self.age = age

    def __del__(self):
        print("deleted")

    def access_globalvar(self):
        print(globalvar)
        local_var = 90
        print(local_var)


obj = demo(20)
print(obj.name)
print(obj.age)
print(obj.msg)
print(demo.msg)
obj.access_globalvar()
print(globalvar)