user_num = input("Enter Your Number: ")
result = ""

while(True):
    if user_num:
        user_num1 = input("Enter Your 2nd Number: ")
        while(True):
            if user_num1:
                user_char = input("Enter Your Operator: - \n\"+\"\t\"*\"\t\"-\"\t\"/\"\t\"%\": ")
                while(True):
                    if user_char:
                        user_num = int(user_num)
                        user_num1 = int(user_num1)
                        print("\n")
                        if user_char == '+':
                            result = (user_num) +  (user_num1) 
                            print(f"Add : {user_num} + {user_num1} = {result}")
                        elif user_char == '-':
                            result = (user_num) - (user_num1)
                            print(f"Subtract : {user_num} - {user_num1} = {result}")
                        elif user_char == '*':
                            result = (user_num) * (user_num1)
                            print(f"Multiply : {user_num} * {user_num1} = {result}")
                        elif user_char == '/':
                            result = (user_num) / (user_num1)
                            print(f"Divide : {user_num} / {user_num1} = {result}")
                        elif user_char == '%':
                            result = (user_num) % (user_num1)
                            print(f"Remainder : {user_num} % {user_num1} = {result}")
                        break

                    else:
                        user_char = input("Enter Your Operator: - \n\"+\"\t\"*\"\t\"-\"\t\"/\"\t\"%\": ")

                break
            else:
                user_num1 = input("Enter Your 2nd Number: ")
        break
    else:
        user_num = input("Enter Your Number: ")

