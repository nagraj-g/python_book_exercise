def main():
    numbers = [2, 4, 6, 8, 10]
    total = 0
    count = len(numbers)
    for item in numbers:
        total += item

    print('The sum of the list is: ', total)
    print('The average of the list is: ', total/count)

main()