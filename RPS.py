import random
k= random.randint(1,3)
dict = {
    1:"R",
    2:"P",
    3:"S"
}
h = dict[k]
k = True
while(k):
    input1 = input("Enter your choice\n1.Rock\n2.Paper\n3.Scissor\n")
    input2 = (input1[0:1]).capitalize()
    if((h=='R' and input2=='R') or(h=='P' and input2=='P')or  (h=='S' and input2=='S')):
        print("Neutral, nobody wins\n")

    elif((h=='R' and input2=='P') or (h=='P' and input2=='R')):
        print("Paper wins")
        print("\tComputer's choice: " + h + "\n\tYour choice: " + input2)

        if(h=='P'):
            print("Computer wins.\nSorry:( ")
        else:
            print("You win.\nCongratulations!!")

    elif((h=='R' and input2=='S') or (h=='S' and input2=='R')):
        print("Rock wins")
        print("\tComputer's choice: " + h + "\n\tYour choice: " + input2)

        if(h=='R'):
            print("Computer wins.\nSorry:( ")
        else:
            print("You win.\nCongratulations!!")

    elif((h=='P' and input2=='S') or (h=='S' and input2=='P')):
        print("Scissor wins")
        print("\tComputer's choice: " + h + "\n\tYour choice: " + input2)

        if(h=='S'):
            print("Computer wins.\nSorry:( ")
        else:
            print("You win.\nCongratulations!!")    
    print("-"*20)
    n = input("Do you want to try again? (Y/N): ").strip().lower()
    if n != 'y':
        k = False 
        print("Thanks for playing!!")
    print("-"*20)
