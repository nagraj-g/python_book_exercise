# creating a list
def get_values():
    counter = 'y'
    values = []
    while counter == 'y':
        data_in = int(input('Enter a number: '))
        # using the append method to 
        values.append(data_in)

        print('Do you want to add another number?')
        counter = input('y = yes, n = no: ')
        print()

        # return the list 
    return values


# create a function that create a list.
def main():
    numbers = get_values()

    print("The numbers in the list are: ")
    print(numbers)

# Call the main function.
main()