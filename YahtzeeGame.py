import random
stars = '*' * 40

#Generate 5 random numbers between 1-6 and create a tuple of them
def make_roll():
    list = (1, 2, 3, 4, 5, 6)
    rolls = tuple(random.choices(list, k = 5)) #Generates 5 random numbers from the list
    print(f"{stars}\nRolling the dice ... {rolls}\n{stars}")
    return rolls

#Determine how many times each number between 1-6 occurs and finds the sum of repeated numbers
def sum_of_given_number(roll, number):
    count = roll.count(number) #Determine how many times the number was generated
    sum = count * number #Determine the sum by multiplying the value of the number with its occurence
    return sum

#Creates a list with the sums
def fill_upper_section(roll, number):
    list_sum = []
    number = 1
    while number < 7:
        sum = sum_of_given_number(roll, number)
        list_sum.append(sum)
        number += 1 #Increase the number by 1 to go through the while loop
    return (list_sum)

#Print each sum using list sequencing
def display_upper_section(list_sum):
    print(f"\n\n{stars}\nUpper section:\n{stars}\nAces: {list_sum[0]}\nTwos: {list_sum[1]}\nThrees: {list_sum[2]}\nFours: {list_sum[3]}\nFives: {list_sum[4]}\nSixes: {list_sum[5]}")

#Determines whether a number was repeatedly rolled a given number of times and finds the sum of all rolls if it was
def num_of_a_kind(roll, number):
    exact = False
    i = 1
    #While loop will stop when the exact number of rolls is found or all numbers from 1-6 have been searched for
    while exact == False and i < 7: 
        count = roll.count(i)
        if count == number:
            exact = True
        else:
            exact = False
        i += 1 #Increments i so that all numbers from 1-6 are searched
    if exact == True:
        total = sum(roll) #Finds the sum of all dice in the list roll
    else:
        total = 0
    return total

#Determines whether the same number was rolled all 5 times
def yahtzee(roll):
    exact = False
    i = 1
    #While loop will stop when the exact number of rolls is found or all numbers from 1-6 have been searched for
    while exact == False and i < 7:
        count = roll.count(i)
        if count == 5:
            exact = True
        else:
            exact = False
        i += 1 #Increments i so that all numbers from 1-6 are searched
    if exact == True:
        total = 50
    else:
        total = 0
    return total

#Print each sum
def display_lower_section(sum_3, sum_4, sum_yahtzee):
    print(f"\n\n{stars}\nLower section:\n{stars}\nThree of a kind: {sum_3}\nFour of a kind: {sum_4}\nYahtzee: {sum_yahtzee}")

def main():
    roll = make_roll()
    list_sum = fill_upper_section(roll, 1)
    display_upper_section(list_sum)
    sum_3 = num_of_a_kind(roll, 3)
    sum_4 = num_of_a_kind(roll, 4)
    sum_yahtzee = yahtzee(roll)
    display_lower_section(sum_3, sum_4, sum_yahtzee)

main()