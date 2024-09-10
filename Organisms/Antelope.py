from .Sheep import Sheep
from .Position import Position
from .Lynx import Lynx
from begin.Action import Action
from begin.ActionEnum import ActionEnum
import random

class Antelope(Sheep):

    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        return Antelope(self, None, None)

    def initParams(self):
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 5
        self.sign = 'A'

    def reactToLynx(self, lynxPosition):
        dx = self.position.x - lynxPosition.x
        dy = self.position.y - lynxPosition.y
        escape_position = Position(xPosition = self.position.x + 2 * dx, yPosition = self.position.y + 2 * dy)
        metOrganism = self.world.getOrganismFromPosition(escape_position)
        if metOrganism is None and self.world.positionOnBoard(escape_position):
            newPosition = escape_position
            print(f"Antelope escapes from Lynx")
        else:
            newPosition = lynxPosition
        return newPosition

    def checkLynx(self, fields):
        for field in fields:
            metOrganism = self.world.getOrganismFromPosition(field)
            if isinstance(metOrganism, Lynx):
                return field

    def move(self):
        result = []
        pomPositions = self.world.getNeighboringPositions(self.position)
        newPosition = None
        if pomPositions:
            lynxPostion = self.checkLynx(pomPositions)
            if lynxPostion:
                newPosition = self.reactToLynx(lynxPostion)
            else:
                if self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position)):
                    newPosition = random.choice(self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position)))
                else:
                    return result
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
            self.lastPosition = self.position
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        return result