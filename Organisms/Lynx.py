from .Animal import Animal


class Lynx(Animal):

	def __init__(self, lynx=None, position=None, world=None):
		super(Lynx, self).__init__(lynx, position, world)

	def clone(self):
		return Lynx(self, None, None)

	def initParams(self):
		self.power = 6
		self.initiative = 5
		self.liveLength = 18
		self.powerToReproduce = 14
		self.sign = 'R'

	def filterPositionsFreeOfLynx(self, fields):
		result = []
		pomOrg = None

		for filed in fields:
			pomOrg = self.world.getOrganismFromPosition(filed)
			if not isinstance(pomOrg, Lynx):
				result.append(filed)
		return result

	def getNeighboringPosition(self):
		return self.filterPositionsFreeOfLynx(self.world.getNeighboringPositions(self.position))