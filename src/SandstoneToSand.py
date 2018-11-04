import json
import os
import shutil

from common.PackData import *
from common.Recipe import *

NAME = 'SandstoneToSand'
VERS = '1.0'

CWD = os.getcwd()

def cleanup():
	path = os.path.join(CWD, 'dist', NAME)
	try:
		shutil.rmtree(path)
	except Exception:
		print('Clean up of %s failed' % path)
	else:
		print('Cleaned up %s' % path)

def makeRecipe(recipePath, recipeName, recipe):
	with open(os.path.join(recipePath, recipeName + '.json'), 'w', encoding='utf-8') as outfile:
		json.dump(recipe.getSerialized(), outfile, ensure_ascii=False)

def build():
	# List directories
	dirList = []

	path = os.path.join(CWD, 'dist', NAME)
	dirList.append(path)

	namespace = 'mdp_sandstone_to_sand'
	recipesDir = os.path.join(path, 'data', namespace, 'recipes')
	dirList.append(recipesDir)

	# Create dirs
	for dirs in dirList:
		os.makedirs(dirs)

	# Create pack metadata
	with open(os.path.join(path, 'pack.mcmeta'), 'w', encoding='utf-8') as outfile:
		metadata = getPackData(NAME, VERS)
		json.dump(metadata, outfile, ensure_ascii=False)
	
	# New recipe
	newRecipe = ShapelessRecipe()
	newRecipe.setIngredients(['minecraft:sandstone'])
	newRecipe.setResult('minecraft:sand', 4)
	makeRecipe(recipesDir, 'sand', newRecipe)

cleanup()
build()

