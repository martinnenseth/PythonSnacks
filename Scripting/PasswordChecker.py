password = input("Provide a new password")
if len(password) < 8:
    print("Password too short.")
elif len(password) > 20:
    print("password too long")
else:
    print("right")