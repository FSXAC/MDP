import json
import os
import shutil

from common.PackData import *

NAME = 'InstantConcrete'
VERS = '0.0'

CWD = os.getcwd()

def cleanup():
	path = os.path.join(CWD, 'dist', NAME)
	try:
		os.rmdir(path)
	except OSError:
		print('Clean up of %s failed' % path)
	else:
		print('Cleaned up %s' % path)

def build():
	# create directories
	dirList = []

	path = os.path.join(CWD, 'dist', NAME)
	dirList.append(path)

	namespace = 'mdp_instant_concrete'
	recipesDir = os.path.join(path, 'data', namespace, 'recipes')
	dirList.append(recipesDir)

	# Create pack metadata
	with open(os.path.join(path, 'pack.mcmeta'), 'w', encoding='utf-8') as outfile:
		metadata = getPackData(NAME, VERS)
		json.dump(metadata, outfile, ensure_ascii=False)

cleanup()
build()

