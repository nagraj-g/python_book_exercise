# you can search for an item in a list using the in operator.

# This program demonstrate the in operator used with a list.

def main():
    prod_nums = ['v475', 'F987', 'Q123', 'R688']

    search = input('Enter a product number: __')

    if search in prod_nums:
        print(search, 'was found in the list.')
    else:
        print(search, "is not found in the list.")

# Call the main function.
main()

# Checkpoint:

# 7.14 What will the following code  display?
def main1():
    names = ['Jill', 'Jim', 'John', 'Jasmine']
    if 'Jasmine' not in names:
        print('Cannot find Jasmine.')
    else:
        print(names, 'This is Jasmine family.')
main1()