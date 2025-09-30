def calculator():
    print("Welcome to the sample calculator!")

    numbers = []

    # Step 1: Collect numbers
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ").strip().lower()
        if user_input == "done":
            print ("you finished entering your numbers!!")
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Step 2: Ensure at least two numbers
    if len(numbers) < 2:
        print("You need at least two numbers to perform calculations.")
        return

    # Step 3: Ask for operation
    sign = input("Enter a calculation sign (+, -, *, /): ").strip()
    if sign not in ['+', '-', '*', '/']:
        print("Invalid operation sign.")
        return

    # Step 4: Perform calculation
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
                print("Error: Cannot divide by zero.")
                return
            result /= num

    # Step 5: Show result
    print(f"The result of the calculation is: {result}")


# Run calculator
calculator()
      