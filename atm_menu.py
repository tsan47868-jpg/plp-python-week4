balance = 1000
correct_pin = 1234

pin = int(input("Enter your 4-digit PIN: "))

if pin == correct_pin:
    amount = int(input("How much would you like to withdraw? "))

    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance}")
    else:
        print("Insufficient funds")
else:
    print("Incorrect PIN")
