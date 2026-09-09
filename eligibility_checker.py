age = int(input("Enter the person's age: "))

# Anyone 18 or older is automatically eligible to join the club.
if age >= 18:
    print("Welcome to the club!")

# If the person is between 13 and 17, they must have parental consent to join.
elif age >= 13 and age < 18:
    consent = input("Do you have parental consent? (yes/no): ").strip().lower()

    # If the response is yes, consent is granted and the person can join.
    if consent == "yes" or consent == "y":
        print("Welcome to the club!")

    # If consent is not yes, the person is not eligible yet.
    elif not (consent == "yes" or consent == "y"):
        print("Sorry, you are not eligible yet.")
    else:
        print("Sorry, you are not eligible yet.")

# Anyone under 13 is too young to join the club.
else:
    print("Sorry, you are not eligible yet.")
