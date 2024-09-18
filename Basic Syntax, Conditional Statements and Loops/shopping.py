budget = int(input())
exiting_word = input()

while exiting_word != "End":
    purchase = int(exiting_word)
    budget -= purchase
    if budget < 0:
        print("You went in overdraft!")
        break
    exiting_word = input()
else:
    print("You bought everything needed.")