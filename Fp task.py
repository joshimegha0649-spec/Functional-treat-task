global dataset
dataset = []

# Flatten method:
def flatten_dataset(dataset):
    """Converts a 2-D list into a 1-D list."""

    flattened_data = []

    for item in dataset:
        if isinstance(item, list):
            flattened_data.extend(item)
        else:
            flattened_data.append(item)

    return flattened_data

# 2. Display Data Summary:
def display_summary():
    """Display the total elements, minimum, sum and average of the dataset."""

    result_data = flatten_dataset(dataset)

    print("\nData Summary:")
    print("- Total elements:",len(result_data))
    print("- Minimum value:",min(result_data))
    print("- Maximum value:",max(result_data))
    print("- Sum of all values:",sum(result_data))
    print(f"- Average value: {sum(result_data)/len(result_data):.2f}")


# 3. Calculate Factorial:
def calculate_factorial(number):
    """Calculation the factorial of a number using recursion."""

    if number == 0 or number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

# 5. Sort Data:
def sort_dataset(dataset):
    """Sorts the dataset in ascending or descending order."""

    result_data = flatten_dataset(dataset)
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    sort_choice = int(input("\nEnter your choice: "))

    match sort_choice:
        case 1:
            sorted_data = sorted(result_data)
            print("\nSorted data in Ascending Order:\n",end="")
            for value in sorted_data:
                print(value,end=" ")

        case 2:
            sorted_data = sorted(result_data,reverse=True)
            print("\nSorted data in Descending Order:\n",end="")
            for value in sorted_data:
                print(value,end=" ")

        case _:
            print("\nInvalid choice, Please enter valid choice.")

# 6. Display Dataset Statistics:
def dataset_statistics():
    """Returns the minimum, maximum, sum, and average of the dataset."""

    result_data = flatten_dataset(dataset)
    min_value = min(result_data)
    max_value = max(result_data)
    total_sum = sum(result_data)
    avg_value = sum(result_data)/len(result_data)

    return min_value,max_value,total_sum,avg_value


print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    menu_choice = int(input("\nPlease enter your choice: "))

    match menu_choice:
        case 1:
            print("1. 1-D Array Manually")
            print("2. 2-D Array Manually")
            print("3. Sample of 1-D Array")
            print("4. Sample of 2-D Array")

            input_choice = int(input("\nPlease enter your choice: "))

            match input_choice:
                case 1:
                    array_1 = input("Enter data for a 1-D array (Separated by spaces):\n").split(" ")
                    for item in array_1:
                        dataset.append(int(item))
                    print("\nData has been stored successfully!")

                case 2:
                    dataset = []
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    for row_index in range(0,rows):
                        row_data = []
                        row = input(f"Enter {cols} elements separated by spaces for {row_index+1}: \n").split(" ")
                        for element in row:
                            row_data.append(int(element))
                        dataset.append(row_data)

                    for row in dataset:
                        print(row)
                    print("\nData has been stored successfully!")

                case 3:
                    dataset = []
                    sample_1D = [45, 12, 89, 3, 67, 24, 91]
                    print(sample_1D)
                    dataset.extend(sample_1D)
                    print("\nData has been stored successfully!")

                case 4:
                    dataset = []
                    sample_2D = [
                        [45, 12, 89],
                        [3, 67, 24],
                        [91, 56, 78]
                    ]
                    for row in sample_2D:
                        print(row)
                    dataset.extend(sample_2D)
                    print("\nData has been stored successfully!")

                case _:
                    print("Inavalid choice, enter valid choice.")

        case 2:
            if len(dataset) == 0:
                print("\nData is not available.")
            else:
                display_summary()

        case 3:
            number = int(input("\nEnter a number to calculate its factorial: "))

            factorial_result = calculate_factorial(number)

            print(f"\nFactorial of {number} is: {factorial_result}")

        case 4:
            if len(dataset) == 0:
                print("\nData is not available.")
            else:
                filter_threshold = int(input("\nEnter a threshold value to filter out data above this value: \n"))

                result_data = flatten_dataset(dataset)

                filtered_data = list(filter(lambda x: x >= filter_threshold,result_data))
                print("\nFiltered Data (values >= 50):\n",end="")

                for value in filtered_data:
                    print(value,end=" ")
                print()

        case 5:
            if len(dataset) == 0:
                print("Data is not available.")
            else:
                sort_dataset(dataset)
                print()

        case 6:
            if len(dataset) == 0:
                print("Data is not available.")
            else:
                min_value,max_value,total_sum,avg_value = dataset_statistics()

                print("\nDataset Statistics:")
                print("- Minimum value:",min_value)
                print("- Maximum value:",max_value)
                print("- Sum of all values:",total_sum)
                print(f"- Average value: {avg_value:.2f}")

        case 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!\n")
            break

        case _:
            print("\nInvalid choice. Please enter valid choice!\n")
