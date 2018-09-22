def getPackData(packname, packversion):
	data = {
		'pack': {
			'pack_format': 1,
			'description': packname + ' V' + packversion
		}
	}
	return data