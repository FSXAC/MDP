import json
import os
import shutil

from common.PackData import *
from common.Recipe import *

NAME = 'InstantConcrete'
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

	namespace = 'mdp_instant_concrete'
	recipesDir = os.path.join(path, 'data', namespace, 'recipes')
	dirList.append(recipesDir)

	# Create dirs
	for dirs in dirList:
		os.makedirs(dirs)

	# Create pack metadata
	with open(os.path.join(path, 'pack.mcmeta'), 'w', encoding='utf-8') as outfile:
		metadata = getPackData(NAME, VERS)
		json.dump(metadata, outfile, ensure_ascii=False)

	# Recipe constants
	TYPES = [
		'minecraft:white_concrete',
		'minecraft:orange_concrete',
		'minecraft:magenta_concrete',
		'minecraft:light_blue_concrete',
		'minecraft:yellow_concrete',
		'minecraft:lime_concrete',
		'minecraft:pink_concrete',
		'minecraft:gray_concrete',
		'minecraft:light_gray_concrete',
		'minecraft:cyan_concrete',
		'minecraft:purple_concrete',
		'minecraft:blue_concrete',
		'minecraft:brown_concrete',
		'minecraft:green_concrete',
		'minecraft:red_concrete'
	]
	PRE_CRAFT_SUFFIX = '_powder'
	PATTERN = [
		'CC',
		'CC'
	]

	# For each variant make recipe
	for block in TYPES:
		newRecipe = ShapedRecipe()
		newRecipe.definePattern(PATTERN)
		newRecipe.defineKey({
			'C': block + PRE_CRAFT_SUFFIX
		})
		newRecipe.setResult(block, 4)

		itemName = block.split(':')[-1]
		makeRecipe(recipesDir, itemName, newRecipe)

cleanup()
build()

