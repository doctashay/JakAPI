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
