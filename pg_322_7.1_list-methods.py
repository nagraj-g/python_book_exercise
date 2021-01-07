def main():
    name_list = []
    again = 'y'

    while again == 'y':
        name = input("Enter a name: ")
        name_list.append(name)

        print('Do you want to add another name ?')
        again = input('y = yes, anything else = no: ')
        print(name_list)
        name_list.insert(8, "Ramesh")
        print("In the name_list the index of Ramesh is given below.")
        print(name_list.index('Ramesh'))

    print("Here are the names you entered.")
    for name in name_list:
        print(name)

main()