class ShapedRecipe:
	def __init__(self):
		self.type = 'crafting_shaped'

	def definePattern(self, grid):
		# check the pattern is valid
		gridHeight = len(grid)
		if gridHeight not in [2, 3]:
			raise RuntimeError('Recipe pattern is not the correct size')

		for row in grid:
			rowWidth = len(row)
			if rowWidth != len(grid[0]):
				raise RuntimeError('Recipe pattern is not the correct size')

		# Set to pattern
		self.pattern = grid

	def defineKey(self, mapping):
		if not hasattr(self, 'pattern'):
			raise RuntimeError('Recipe pattern does not exist')


		# Check that the key exists in pattern
		for key in mapping:
			if not self.isKeyInPattern(key):
				print('WARNING:', key, 'is not in recipe pattern')
		
		# Check that the pattern has keys
		checked = ''
		for row in self.pattern:
			for cell in row:
				if cell not in checked:
					if cell not in mapping:
						raise RuntimeError('Item in recipe pattern does not have mapping')
					else:
						checked += cell

		# Construct serializable obj
		self.key = {}
		for key in mapping:
			self.key[key] = {
				'item': mapping[key]
			}

	def isKeyInPattern(self, key):
		for row in self.pattern:
			if key in row:
				return True

		return False

	def setResult(self, result, count):
		self.result = {
			'item': result,
			'count': count
		}

	def getSerialized(self):
		data = {
			'type': self.type,
			'pattern': self.pattern,
			'key': self.key,
			'result': self.result
		}

		return data


class ShapelessRecipe:
	def __init__(self):
		self.type = 'crafting_shapeless'
	
	def setIngredients(self, ingredients):
		self.ingredients = []

		# TODO: assuming there is no substitutive items, and only 'items'
		for ingredient in ingredients:
			self.ingredients.append({'item': ingredient})

	def setResult(self, result, count):
		self.result = {
			'item': result,
			'count': count
		}
	
	def getSerialized(self):
		data = {
			'type': self.type,
			'ingredients': self.ingredients,
			'result': self.result
		}

		return data