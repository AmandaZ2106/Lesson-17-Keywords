bill=int(input("Please enter total amount to pay:"))
paid=int(input("Please enter amount paid:"))
if bill==paid:
    print("Ther is no balance to be paid.\nHave a lovely day😊")
elif bill>paid:
    due=bill-paid
    print("Your amount due is: ",due)   
elif bill<paid:
    change=paid-bill
    print("Change:",change)
    Yes=input("Do we keep the change? ")
    if Yes=="yes" or Yes=="Yes":
        print("Thank you very much😀")
    else:
        print("Your change will be returned")  
print("Goodbye")             