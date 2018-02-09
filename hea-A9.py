# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 19:43:07 2016

@author: hea
"""
#####################################################################################
# Author: Annie He
#hea    #2/9/16
# This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer and A9

# Acknowledgements: Dr. Jan Pearce with help from TA Ashley Aiken

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def descriptions(lifepath):
    '''this will print the comment depending on the lifepath number that
    has been outputted from overall2sum'''
    if lifepath == 1:
        print("Your lifepath number is 1. You must like pie and all things pie associated. Pie charts, pie graphs, and all flavors of pies are enjoyable!")
    elif lifepath == 2:
        print("Your lifepath number is 2. You live your life on the edge. You enjoy skydiving, rollercoasters, and having spontaneous adventures!")
    elif lifepath == 3:
        print("Your lifepath number is 3. You tend to be a little more sheltered. You enjoy a simple relaxation in your room watching movies.")
    elif lifepath == 4:
        print("Your lifepath number is 4. You are truly one with style. People tend to look at you for the next fashion trend!")
    elif lifepath == 5:
        print("Your lifepath number is 5. You love to be theatrical. Acting is your life calling.")
    elif lifepath == 6:
        print("Your lifepath number is 6. You are all about organization. Your room, closet, and desk are nice, neat, and clean.")
    elif lifepath == 7:
        print("Your lifepath number is 7. You are the athlete of the group, and 7 is always your jersey number.")
    elif lifepath == 8:
        print("Your lifepath number is 8. You are super comedic. Everything you say is punny. Ha, get it?")
    elif lifepath == 9:
        print("Your lifepath number is 9. You love to bake desserts! Cakes, cookies, and cheesecakes are your specialties!")
    elif lifepath == 11:
        print("Your lifepath number is 11. You are one to take leadership. Leading the group to success is your strong point and that is what makes you a great buisness person.")
    elif lifepath == 22: 
        print("Your lifepath number is 22. You are free-spirited! You fly planes for a living but take them out on a spin for fun!")
    elif lifepath == 33:
        print("Your lifepath number is 33. You have a talent of defending your arguments very persuasively. Becoming a lawyer is in your near future.")
    
def peel_digits(num):
    '''given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]'''   
    deciding = master(num)
    '''decides if the digits are a master number
    i.e. 11, 22, or 33'''
    if deciding == True: #If the number is a master number
        digit_list = [] #creates an empty list
        digit_list.append(int(num)) #puts down the master number
    else:
        str_num=str(num) # convert to string to utilize Python's strong string features
        digit_list=[] #create empty list
        for letter in str_num:
            digit_list.append(int(letter)) #Puts each digits into list
    # print(digit_list)
    return digit_list

def master(num):
    '''sees if the number is a multiple of 11'''
    if int(num) % 11 == 0:
        if int(num) >= 44:  #if the number is 44 or more, the process will repeat
            return False
        else: 
            return True     #will continue if true
    else:
        return False
        
def adder(num_list):
    '''will add the digits together
    e.g. [1, 9, 8, 4] is 1 + 9 = 10, 10 + 8 = 18, 18 + 4 = 22, then returns the total'''
    total = 0
    for i in num_list:
        total = total + i
    return total
    
def total(day, month, year):
    '''adds the digit totals for each day, month, and year, and combines into one total
    returns the total'''
    sum1 = day + month + year
    return sum1
    
    
def main():
    '''this main function is intended to display the raw_input function, the peel_digits function,
    the adder function, the total function, print function, and description function. It calculates the overall digits, and if the
    digit is 10 or larger, it will peel the digits again until the number is a single digit'''
    monthinput = raw_input("month")
    dayinput = raw_input("day")
    yearinput = raw_input("year")
        
    month = peel_digits(monthinput)     #peels the digits and makes them into lists
    day = peel_digits(dayinput)
    year = peel_digits(yearinput)
    
    monthsum = adder(month)     #adds the digits together
    daysum = adder(day)
    yearsum = adder(year)

    overall1 = total(monthsum, daysum, yearsum)     #is the sum of the digits from the lists
    overall2 = peel_digits(overall1)    #peels the digits of the previous sum
    overall2sum = adder(overall2)   #adds the digits of the previous sum together
  
    if overall2sum >= 10:
        overall2 = peel_digits(overall2sum)     #only runs if digit is greater than or equal to 10
        overall2sum = adder(overall2)
    print overall2sum
    descriptions(overall2sum)
    


    
main()  #calls to main


