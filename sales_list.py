# A list of string 
# info = ["sarah", "connor"]

# The NUM_DAYS constant holds the number of
# days that we will gather sales data for.
NUM_DAYS = 5

def main():
        # Create a list to hold the sales for each day.
    sales = [0] * NUM_DAYS

    # CREATE A VARIABLE TO HOLD AN INDEX.
    index = 0

    print("Enter the sales for each day.")

    # Get the sales for each day.
    while index < NUM_DAYS:
        print('Day #', index + 1, ':', sep="^", end="")
        sales[index] = float(input())
        index +=1

    # Display the values entered.
    print('Here are the values you entered: ')
    for values in sales:
        print(values)


# Call the main function.
main()