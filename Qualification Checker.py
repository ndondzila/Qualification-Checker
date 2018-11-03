# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:41:22 2018

@author: Nicholas
"""

##These dicts contain qualifying totals for respective events accross weightclasses##  
american_open_series_f = {"45":85, "49":88, "55":97, "59":103, "64":113, "71":124, "76":127, "81":129, "87":134, "87+":144}
american_open_final_f = {"45":118, "49":132, "55":149, "59":163, "64":175, "71":182, "76":185, "81":186, "87":187, "87+":190}
nationals_f = {"45":120, "49":137, "55":151, "59":166, "64":177, "71":185, "76":191, "81":193, "87":194, "87+":195}
american_open_series_m = {"55":123, "61":137, "67":170, "73":174, "81":199, "89":207, "96":217, "102":222, "109":230, "109+":235}
american_open_final_m = {"55":178, "61":209, "67":237, "73":241, "81":267, "89":286, "96":291, "102":301, "109":306, "109+":308}
nationals_m = {"55":200, "61":210, "67":240, "73":260, "81":274, "89":290, "96":303, "102":305, "109":308, "109+":311}

##This function checks gender of the overlapped weightclasses##
   
name = input("Hello! What is your name?")

print("Hello, " + name + "!")

do_lift = input("Do you compete in weightlifting? (Y/N)")
if do_lift.lower() == "y":
    print("That's awesome! Me too!")
    gender = input("Do you compete as a male or a female?")
    if gender.lower() != "male" and gender.lower() != "female":
        gender = input("I understand not everyone identifies strictly as one or the other, I'm simply asking which you compete in; male or female?")
    weightclass = input("What weightclass do you compete in?")
    if weightclass not in nationals_f and weightclass not in nationals_m:
        weightclass = input("I'm sorry, that isn't an IWF weight cass, please enter a new weight class.")    
else:
    print("Darn! You should consider giving it a go, " + name + "!")
    
total = int(input("What is your best competition total in the last 6 months?"))

##This function checks for female qualification for events and returns a message indicating results##  
def qualified_f(weightclass, total):
    nats = "Congratulations, you're qualified for any USAW National event including AO Series, American Open Finals, and the National Championships!"
    a_o_finals = "Congratulations, you're qualified for the American Open Finals as well as the AO Series events!"
    a_o_series = "Congratulations, you're qualified for the American Open Series events!"
    not_yet = "Unfortunately you haven't qualified for an event yet, but keep training hard and you will get there soon!"
    if total > int(nationals_f[weightclass]):
        return nats
    elif total > int(american_open_final_f[weightclass]) and total < int(nationals_f[weightclass]):
        return a_o_finals
    elif total > int(american_open_series_f[weightclass]) and total < int(american_open_final_f[weightclass]):
        return a_o_series
    else:
        return not_yet

##This function checks for male qualification for events and returns a message indicating results## 
def qualified_m(weightclass, total):
    nats = "Congratulations, you're qualified for any USAW National event including AO Series, American Open Finals, and the National Championships!"
    a_o_finals = "Congratulations, you're qualified for the American Open Finals as well as the AO Series events!"
    a_o_series = "Congratulations, you're qualified for the American Open Series events!"
    not_yet = "Unfortunately you haven't qualified for an event yet, but keep training hard and you will get there soon!"
    if total > int(nationals_m[weightclass]):
        return nats
    elif total > int(american_open_final_m[weightclass]) and total < int(nationals_m[weightclass]):
        return a_o_finals
    elif total > int(american_open_series_m[weightclass]) and total < int(american_open_final_m[weightclass]):
        return a_o_series
    else:
        return not_yet
    
if gender == "female":
    print(qualified_f(weightclass, total))
elif gender == "male":
    print(qualified_m(weightclass, total))
