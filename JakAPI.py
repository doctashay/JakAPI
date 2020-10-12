# TO-DO # 
# Propagate and list all runs from a certain category 
# Barebones GUI framework - Eel?
# Check a user's PBs and wait for new PB 
# Add API Implementation for Personal Bests

import srcomapi, srcomapi.datatypes as dt
import os
api = srcomapi.SpeedrunCom(); api.debug = 0

print("Grabbing game name")
game = api.search(srcomapi.datatypes.Game, {"name": "jak and daxter: the precursor legacy"})[0]
assert(game.name == "Jak and Daxter: The Precursor Legacy")

print(game.name)

print("Grabbing categories")
print(game.categories)
print("Grabbing No FCS WR")
print(game.categories[1].records[0].runs[0]["run"].times)
print("Grabbing No LTS WR")
print(game.categories[0].records[0].runs[0]["run"].times)



def look_for_pb():
    print("Grabbing leaderboard information")
    for x in game.categories[0].records[0].runs[0]["run"].times:
        print(x)
    return True

if look_for_pb():
        print("Yes")
else:
        print("No")
