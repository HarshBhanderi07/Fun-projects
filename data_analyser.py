print("Welcome to the Data analyser and Transformer Programme!\n")

data = []

while True:
    print("""\nMain menu:
1. Input data
2. Display data summary (Built in functions))
3. Calculate Factorial
4. Filter data by threshold
5. Sort data
6. Display dataset Statistics
7. Exit\n""")
    
    choice = int(input("Enter your choice: "))
    
    
    match choice:
        case 1:
            print("enter a data for 1D array (space separated):")
            data = [int(x) for x in input().split()]
            print("Data input successful!\n")
            
        case 2:
            if not data:
                print("No data available. Please input data first.\n")
            else:
                print("\nData Summary:")
                print(" - Total elements :", len(data))
                print(" - Min value :", min(data))
                print(" - Max value :", max(data))
                print(" - Sum of elements :", sum(data))
                print(" - Average value :", sum(data)/len(data))
                print()
        
        case 3:
            if not data:
                print("No data available. Please input data first.\n")
                continue
            print("calculate factorial.")
            num = int(input("Enter a non-negative number:"))
            def factorial(num):
                if num == 0 or num == 1:
                    return 1
                else:
                    return num * factorial(num - 1)
            print(f"The factorial of {num} is {factorial(num)}\n")    
                
                
        case 4:
            if not data:
                print("No data available. Please input data first.\n")
                continue
            print("Enter a threshold value to filter data:")
            thresold = int(input())
            print(f"Filtered data (greater than {thresold}):\n")
            filtered_data = [x for x in data if x > thresold]
            print(filtered_data)
            
            
        case 5:
            if not data:
                print("No data available. Please input data first.\n")
                continue
            choose = int(input("Choose sorting order(1/2):"))
            print("1. Ascending\n2. Descending")
            
            if choose == 1:
                print("Data in sorted order(Ascending):")
                print(sorted(data))
            elif choose == 2:
                print("Data in sorted order(Descending):")
                print(sorted(data, reverse=True))
            else:
                print("Invalid choice for sorting order.")
                
        case 6:
            print("FUCK YOU!!!")
            
        case 7:
            print("Thank you for using my programme")
            break
        
        case _:
            print("please enter an valid number")