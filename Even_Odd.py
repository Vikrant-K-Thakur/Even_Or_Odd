i = 1
while i!=0:
    print("Its a program to check even or odd")

    num = input("Enter any number: ")
    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
    
        if(int(num)%2==0):
            print("Its even number")
        elif(int(num)%2!=0):
                print("Its odd number")

        i = int(input("You have to check another number?\nwrite \"1\" for \"Yes\" or \"0\" for \"No\": "))
    else:
        print("Invalid input! please write valid number")
print("Thank for using the program")
