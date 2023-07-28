usernames = ['nazir','tomas','daniels','mutlu','admin']
admins = ['mutlu']

if 'admin' in usernames:
    print(f"\nHello admin, would you like to see status report?")

for admin in admins:
    if admin in usernames:
        print(f"Yes we have admin on the list {admin}.")
    else:
        print(f"Sorry No Admin found {admin}!!")

print(f"\nHello Jaden, Thank you for loggin in again")


