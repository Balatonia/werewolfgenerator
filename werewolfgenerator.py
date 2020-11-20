#this is werewolfgenerator.py#
#this script generates random roles for the werewolves games from a list of participants entered into the console#
#created by Marie-Luise Popp#
# in this second version, I updated the original file so it allows regenerating after the first round #

import random

def determine_character(list1):
    if list1:
        x = random.choice(list1)
        list1.remove(x)
        return x

def determine_roles(input1):
    ## this function determines the following character from a list: villagers, werewolfes, seer, witch, hunter & cupid ##
    ## you can add more special roles by calling the determine_character function to another variable ##
    participants_split = input1.split(",")
    participants_list = [str(x) for x in participants_split if x]
    print(participants_list)
    participants_number = len(participants_list)
    # werewolf_factor is the factor that villagers outnumber werewolves, 4 is recommended in the real game
    werewolf_factor = 4
    werewolf_number = int(participants_number / werewolf_factor)

    werewolves = random.sample(participants_list, k=werewolf_number)

    new_participants = [part for part in participants_list if part not in werewolves]

    witch = determine_character(new_participants)
    seer = determine_character(new_participants)
    amor = determine_character(new_participants)
    hunter = determine_character(new_participants)
    print("The following characters were generated: \nVillagers: ", ", ".join(new_participants), "\nWerwolves: ",
          ", ".join(werewolves), "\nWitch: ", witch, "\nHunter: ", hunter, "\nAmor: ", amor, "\nSeer: ", seer)

participants_input = input("Please name all participants, separated by ',': \n")
q = "y"
## the while-loop allows you to re-generate ##

while q == "y" or q == "Y":
    determine_roles(participants_input)
    print("Would you like to generate again?\n ")
    reply = input("y / n? \n")
    q = str(reply)
#if reply_str == "y" or reply_str == "Y":
  #  determine_roles(participants_input)







participants_split = participants_input.split(",")
participants_list = [str(x) for x in participants_split if x]
participants_number = len(participants_list)
