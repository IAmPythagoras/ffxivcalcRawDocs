

from ffxivcalc.Fight import Fight
from ffxivcalc.Enemy import Enemy

newEnemy = Enemy() # Creating new Enemy instance
ShowGraph = True # We want the simulator to generate graphs

newFight = Fight(newEnemy, ShowGraph) # Creating new Fight instance

newFight.RequirementOn = True # Does NOT ignore requirement during simulation
newFight.IgnoreMana = False # Does NOT ignore Mana requirement during simulation


from ffxivcalc.Jobs.Player import Player # Importing player class
from ffxivcalc.Jobs.PlayerEnum import JobEnum # Importing JobEnum

ActionSet = [] # List containing actions to be performed. Can be left empty
EffectList = [] # List of all effect on the player at start. Can be left empty
Stat = {"MainStat": 2945, "WD":126, "Det" : 1451, "Ten" : 400, "SS": 840, "SkS" : 400, "Crit" : 2386, "DH" : 1307} # Stats for BlackMage


newBlackMage = Player(ActionSet, EffectList, Stat, JobEnum.BlackMage) # Creating player instance

from ffxivcalc.Jobs.Caster.Blackmage.BlackMage_Spell import * # Importing the Blackmage Actions
from ffxivcalc.Jobs.Caster.Caster_Spell import *    # Importing the roles action for Caster
from ffxivcalc.Jobs.Base_Spell import Potion, WaitAbility # Importing the Base actions

newBlackMage.ActionSet = [SharpCast, WaitAbility(20),Fire3, Thunder3, Fire4, Triplecast, Fire4, Potion, 
Fire4, Amplifier, LeyLines, Fire4, SharpCast, Swiftcast, Despair, Manafront, Triplecast, Fire4, Despair]

newFight.AddPlayer([newBlackMage]) # Adding newBlackMage to newFight. Input must be a list and can contain
# more than one Player object.

TimeUnit = 0.01 # Unit of time per frame
TimeLimit = 500 # Max running time of the simulation (time IN the simulation)

# Simulation parameters
newFight.RequirementOn = True # Will check for actions requirement
newFight.IgnoreMana = False # Will check for mana
vocal = True # Want to output data in text

newFight.SimulateFight(TimeUnit, TimeLimit, vocal) # Simulating the fight