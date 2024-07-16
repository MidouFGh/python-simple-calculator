#simple python calculator v1.0
software = True
while software:
    #--------------------------------------------calculation----------------------------------------------
    def calculator():
        num1 = int(input("number 1: "))
        mark = input("\nplease enter the mark [+,-,/,*]: ")
        num2 = int(input("\nnumber 2: "))
        if mark == "+":
            result = num1 + num2
            print(result)
        elif mark == "-":
            result = num1 - num2
            print(result)
        elif mark == "/":
            result = num1 / num2
            print(result)
        elif mark == "*":
            result = num1 * num2
            print(result)
        else:
            print("sorry restart the software")
            exit()
    calculator()
    #-----------------------------------------------restart-----------------------------------------------
    def restart():
        q1 = input("do you want to exit the software [y/n]: ")
        if q1 == "y" or "Y" or "Yes" or "yes" or "YES":
            print("\n")
            exit()
        elif q1 == "n" or "N" or "No" or "no" or "NO":
            calculator()
        else:
            print("repeate please !")
            restart()
    
    restart()
