try:
    balance=10000
    amount=int(input("Enter withdrawl amount :"))
    if amount>balance:
        raise Exception("Insufficent balance.")
        print("Please collect your cash.")
except ValueError:
    print("Value should be a integer")
except Exception as e:
    print(e)
else:
    print("Transaction successful.")
finally:
    print("Thank you for using our bank.")