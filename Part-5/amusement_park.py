age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your Adminssion cost is $25.")
# else:
#     print("You Admission cost is $40.")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your Admission Cost is ${price}")
