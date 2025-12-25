data = []
summary = {}

def input_data():
    global data
    choice = int(input("Enter 1 for 1D list or 2 for 2D list: "))
    if choice == 1:
        data = list(map(int, input("Enter values: ").split()))
    elif choice == 2:
        rows = int(input("Enter rows: "))
        data = []
        for i in range(rows):
            row = list(map(int, input("Enter row values: ").split()))
            data.append(row)

def display_summary():
    if isinstance(data[0], list):
        flat = []
        for r in data:
            for v in r:
                flat.append(v)
    else:
        flat = data
    print("Count:", len(flat))
    print("Min:", min(flat))
    print("Max:", max(flat))
    print("Sum:", sum(flat))
    print("Average:", sum(flat) / len(flat))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_data():
    t = int(input("Enter threshold: "))
    if isinstance(data[0], list):
        flat = []
        for r in data:
            for v in r:
                flat.append(v)
    else:
        flat = data
    result = list(filter(lambda x: x > t, flat))
    print(result)

def sort_data():
    if isinstance(data[0], list):
        sorted_data = sorted(data)
        for r in sorted_data:
            print(r)
    else:
        data.sort()
        print(data)

def stats():
    if isinstance(data[0], list):
        flat = []
        for r in data:
            for v in r:
                flat.append(v)
    else:
        flat = data
    return min(flat), max(flat), sum(flat) / len(flat)

while True:
    print("\n ==== Welocme to the Data Analyzer and Transformer program ===")
    print("\n1.Input Data")
    print("2.Display Data Summary (Built-in Functions)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data (Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7.Exit program")
    ch = int(input("Enter choice: "))

    if ch == 1:
        input_data()
    elif ch == 2:
        display_summary()
    elif ch == 3:
        n = int(input("Enter number: "))
        print(factorial(n))
    elif ch == 4:
        filter_data()
    elif ch == 5:
        sort_data()
    elif ch == 6:
        a, b, c = stats()
        print("Min:", a)
        print("Max:", b)
        print("Average:", c)
    elif ch == 7:
        print("\nThank you for using Data Analyzer and Transformer Program. Goodbye !")
    else:
        print("Invalid choice")