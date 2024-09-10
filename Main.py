from Organisms.Antelope import Antelope
from Organisms.World import World
from Organisms.Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx

import os

worldX = 10
worldY = 10

def add_new_organism(world):
	organism_type = input("Enter organism type (Antelope, Sheep, Lynx, Grass): ")

	try:
		x = int(input("Enter x position: "))
		y = int(input("Enter y position: "))
	except ValueError:
		print("Invalid input. Please enter integers for positions.")
		return

	if 0 <= x < worldX and 0 <= y < worldY:
		position = Position(xPosition=x, yPosition=y)
	else:
		print("Invalid input. Please enter a position within the map range.")
		return

	new_organism = None
	match organism_type:
		case "Antelope":
			new_organism = Antelope(position=position, world=world)
		case "Sheep":
			new_organism = Sheep(position=position, world=world)
		case "Lynx":
			new_organism = Lynx(position=position, world=world)
		case "Grass":
			new_organism = Grass(position=position, world=world)
		case _:
			print("Unknown organism type!")
			return

	if new_organism is not None:
		if world.isPositionFree(position):
			world.addOrganismAtPosition(new_organism, position)
			print(f"Added {organism_type} at {position}")
		else:
			print(f"Position {position} is not free!")


if __name__ == '__main__':
	pyWorld = World(worldX, worldY)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Lynx(position=Position(xPosition=5, yPosition=5), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Lynx(position=Position(xPosition=1, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Lynx(position=Position(xPosition=3, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Lynx(position=Position(xPosition=6, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Antelope(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 50):
		choice = input('Enter for next turn or insert "plague"/"organism" for additional modes\n')
		if choice == "plague":
			pyWorld.activate_plague()
		if choice == "organism":
			add_new_organism(pyWorld)
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
