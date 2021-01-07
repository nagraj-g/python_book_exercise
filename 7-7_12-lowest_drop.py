# get the student test score
# Calculate the total of the scores.
# Find the lowest score.
# Substract the lowest from the total.This gives the adjusted total.
# Divide the adjusted total by 1 less than the numbers of test scores.This is the average.

# Display the average.

def main():
    subject_score = sub_scr_list()
    lowest_score = min(subject_score)

    print(lowest_score ,': This is the lowest score.')

    # Calculate adjusted total and sum total.
    total = find_total(subject_score)
    print(total, " is the total.")

    # calculate adjusted total.
    # adjusted_score = subject_score.remove(lowest_score)

    #  NOte : I was gettting error because i was copying or assigning list wrong way.
    #  and i was assing a method to list.
    adjusted_score = [] + subject_score
    adjusted_score.remove(lowest_score)

    
    adjusted_total = find_total(adjusted_score)
    print(adjusted_total, " is the adjusted total.")


    # Find the average of the list.
    average = find_avg(subject_score)
    print(average, ' is the average of the student.')
    adjusted_average = find_avg(adjusted_score)
    print(adjusted_average, ' is the adjusted average of the student.')




# Get the scores and form a list.

def sub_scr_list():
    print('Enter the list in the following: ' )
    scr = []
    again = 'y'

    while again == 'y':
        element = int(input('Enter the score: '))
        scr.append(element)        
        again = input('(y = yes n = no to ) Enter to add more date:  ')

    return scr


def find_avg(list_scr):
    
    sum = find_total(list_scr)
    len_scr = len(list_scr)
    avg = sum/len_scr
    return avg

def find_total(list_scr): 
    sum = 0
    for item in list_scr:
        sum += item   
    return sum

main()
# Testing score, average, total.
# score = sub_scr_list()
# average = find_avg(score)
# total = find_total(score)
# print(score, '\n', average, '\n',total )