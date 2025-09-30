word=input("Enter a word:")
for letter in word:
    if letter=="A" or letter=="a":
        print("The letter A is there in the word")
        break 
    else:
        print("The letter A is not there")