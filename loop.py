def cal():
    while True:
        get1 = int(input("Enter m1 (or type 'exit' to stop): "))
        get2 = int(input("Enter m2: "))
        total1 = get1 + get2
        print(f"The total is: {total1}")
        
        continue_input = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            print("Exiting the calculator.")
            break

cal()