password = "pass"
attempts = 0
def validate(p):
    global attempts
    attempts += 1
    if p == password and attempts < 5:
        return True
    elif attempts >= 5:
        print("too many attemps")
        return False
    else:
        return False
user = "default"
while not validate (user):
    user = input("What is your password?")
else:
    print("Secrets")