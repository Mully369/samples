def calculator (): 
    print ("welcome to te sample calculator")
    numbers = []
    while True:
        user_input = input("Enter your numbers one by one, type 'done' when finished: ").strip()
        if user_input == "done" :
            print("goodbye!!")
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("invalid input please enter a number or 'done' ")
        if len(numbers) < 2:
            print ("need atleast two numbers ")
           
        sign = input("enter a calculation sign among = + - / * ").strip()
        if sign not in ['=', '+', '-', '/', '*']:
            print("invalid operation sign")
            continue
        result = numbers[0]
        for num in numbers[1:]:
            if sign == '+':
                result += num
            elif sign == '-':
                result -= num
            elif sign == '*':
                result *= num
            elif sign == '/':
                if num == 0:
                    print ("cannot be divided by zero ")
                    return
                result /= num
                print (f"the result of thecalculation is :" ,{result})
calculator()
              