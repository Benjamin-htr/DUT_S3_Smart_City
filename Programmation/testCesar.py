from classes.Cellule import Cellule
from classes.StationRecharge import StationRecharge
from classes.LieuMission import LieuMission
from classes.Robot import Robot
from classes.Carte import Carte
from random import *
from tkinter import *

carte = Carte("a")
carte.creationCartes(5,5)
rob = Robot("HAllo",carte.cellule(0,0), carte)

print(carte)