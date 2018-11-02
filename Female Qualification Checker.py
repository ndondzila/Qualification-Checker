# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:41:22 2018

@author: Nicholas
"""

##These dicts contain qualifying totals for respective events accross female weightclasses##  
american_open_series_f = {"45":85, "49":88, "55":97, "59":103, "64":113, "71":124, "76":127, "81f":129, "87":134, "87+":144}
american_open_final_f = {"45":118, "49":132, "55":149, "59":163, "64":175, "71":182, "76":185, "81f":186, "87":187, "87+":190}
nationals_f = {"45":120, "49":137, "55":151, "59":166, "64":177, "71":185, "76":191, "81f":193, "87":194, "87+":195}

##This function checks gender of the overlapped weightclasses##
   
name = input("Hello! What is your name?")

print("Hello, " + name + "!")

do_lift = input("Do you compete in weightlifting? (Y/N)")

if do_lift.lower() == "y":
    print("That's awesome! Me too!")
    weightclass = input("What weightclass do you compete in?")
    if weightclass not in nationals_f:
        weightclass = input("I'm sorry, that isn't an IWF weight class, please enter a new weight class.")
    
else:
    print("Darn! You should consider giving it a go, " + name + "!")
    
total = int(input("What is your best competition total in the last 6 months?"))

##This function checks for qualification for events and returns a message indicating results##  
def qualified_f(weightclass, total):
    if total > int(nationals_f[weightclass]):
        print("Congratulations, you're qualified for any USAW National event including AO Series, American Open Finals, and the National Championships!")
    elif total > int(american_open_final_f[weightclass]) and total < int(nationals_f[weightclass]):
        print("Congratulations, you're qualified for the American Open Finals as well as the AO Series events!")
    elif total > int(american_open_series_f[weightclass]) and total < int(american_open_final_f[weightclass]):
        print("Congratulations, you're qualified for the American Open Series events!")
    else:
        print("Unfortunately you haven't qualified for an event yet, but keep training hard and you will get there soon!")

qualified_f(weightclass, total)