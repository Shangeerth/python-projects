def marks():
    
   while True:     
     input1 =int(input("Please enter the first input: "))
     input2 =int(input("Please enter the second input: "))
     input3 =int(input("Please enter the third input: "))

# Print the inputs in a single row
     print("You entered:", input1, input2, input3)
    
     continue_input = input("Do you want to calculate again? (yes/no): ").strip().lower()
     if continue_input != 'yes':
            print("Exiting the calculator.")
            break

    
marks()