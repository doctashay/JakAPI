import srcomapi, srcomapi.datatypes as dt
import os
api = srcomapi.SpeedrunCom(); api.debug = 1 

game = api.search(srcomapi.datatypes.Game, {"name": "jak and daxter: the precursor legacy"})[0]
assert(game.name == "Jak and Daxter: The Precursor Legacy")

print(game.name)

print(game.categories)
print(game.categories[1].records[0].runs[0]["run"].times)
