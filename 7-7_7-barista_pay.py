# This program calculates the gross pay for each of megan's baristas.

NUM_EMPLOYEES = 6

def main():
    # create a list to hold employee hours
    hours = [0] * NUM_EMPLOYEES

    #Get the employees hours worked.
    for index in range(NUM_EMPLOYEES):
        print('Enter the no. hours: ',index+1, \
            ': ',sep='', end='')
        hours[index] = float(input())

    pay_rate = float(input("Enter the hourly rate: "))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee', index + 1, ': $',\
            format(gross_pay, ',.2f'), sep='')

main()