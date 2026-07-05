# class account:
#     def __init__(self, bal):
#         self.__bal = bal
#         self.__pm = "1234"

#     def get_bal(self):
#         return self.__bal

#     def set_bal(self, amt):
#         self.__bal = amt

#     def __deposit(self, amt):
#         self.__bal += amt
#         print("deposited", amt, "new bal is", self.__bal)

#     def __withdraw(self, amt):
#         if amt < self.__bal:
#             self.__bal -= amt
#             print("debited", amt, "remaining bal is", self.__bal)
#         else:
#             print("insuff...")

#     def __access_pm(self):
#         return self.__pm

#     def call_deposit(self, amt):
#         return self.__deposit(amt)

#     def call_withdraw(self, amt):
#         return self.__withdraw(amt)

#     def access_pm(self):
#         return self.__access_pm()


# obj = account(0)

# print(obj.get_bal())
# obj.set_bal(500)
# print(obj.get_bal())

# obj.call_deposit(200)
# obj.call_withdraw(300)

# print(obj.access_pm())

# import random

# class insta:
#     def __init__(self, name, username, pwd):
#         self.name = name
#         self.username = username
#         self.__pwd = pwd
#         self.__otp = None

#     def login(self, username, pwd):
#         if self.username == username and self.__pwd == pwd:
#             print("login successfull")
#             self.__otp = random.randint(1000, 9999)
#             print("otp send to yr registred mobile no ", self.__otp)
#         else:
#             print("invalid creditials !")

#     def verify_otp(self, u_otp):
#         if self.__otp == u_otp:
#             print("otp matched")
#         else:
#             print("invalid otp !")


# obj = insta("ram", "ram@123", 12345)
# obj.login("ram@123", 12345)

# u_otp = int(input("enter yr otp :\n"))
# obj.verify_otp(u_otp)