#this is werewolfgenerator.py#
#this script generates random roles for the werewolves games from a list of participants entered into the console#
#created by Marie-Luise Popp#

import random

def determine_character(list1):
    if list1:
        x = random.choice(list1)
        list1.remove(x)
        return x

participants_input = input("Please name all participants, separated by ',': \n")
participants_split = participants_input.split(",")
participants_list = [str(x) for x in participants_split if x]
participants_number = len(participants_list)

#werewolf_factor is the factor that villagers outnumber werewolves, 4 is recommended in the real game
werewolf_factor = 4
werewolf_number = int(participants_number / werewolf_factor)

werewolves = random.sample(participants_list, k=werewolf_number)

new_participants = [part for part in participants_list if part not in werewolves]

witch = determine_character(new_participants)
seer = determine_character(new_participants)
amor = determine_character(new_participants)
hunter = determine_character(new_participants)


print("The following characters were generated: \nVillagers: ", ", ".join(new_participants), "\nWerwolves: ", ", ".join(werewolves), "\nWitch: ", witch, "\nHunter: ", hunter, "\nAmor: ", amor, "\nSeer: ", seer)
