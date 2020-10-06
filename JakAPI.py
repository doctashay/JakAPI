import srcomapi, srcomapi.datatypes as dt
import os
api = srcomapi.SpeedrunCom(); api.debug = 1 

a = api.search(srcomapi.datatypes.Game, {"name": "jak and daxter: the precursor legacy"})

Game = a[0]

print(Game.records)
