import pymongo
client = pymongo.MongoClient('mongodb+srv://giordano:waldo@cluster0-p2txm.mongodb.net/Almacen')
from connexion import NoContent

def obtenerStands():
	arreglo = []
	stands = client.Almacen.stands.find()
	for stand in stands:
		arreglo.append({"standId":stand['standId'],
			"nombre":stand['nombre'],
			"seccion":stand['seccion']})
	return arreglo

def registrarStand(stand):
	client.Almacen.stands.insert({"standId":stand['standId'],
			"nombre":stand['nombre'],
			"seccion":stand['seccion']})
	return NoContent, (200 if True else 201)

def editarStand(stand_id,stand):
	stands = client.Almacen.stands.update({"standId":stand['standId']},
		{"standId":stand['standId'],
		"nombre":stand['nombre'],
			"seccion":stand['seccion']})
	return NoContent, (200 if True else 201)

def eliminarStand(stand_id):
	stands = client.Almacen.stands.remove({"standId":int(stand_id)})
	return NoContent, 204

def obtenerStand(stand_id):
	stand = client.Almacen.stands.find_one({"standId":int(stand_id)})
	if stand:
		stand = {"standId":stand['standId'],
			"nombre":stand['nombre'],
			"seccion":stand['seccion']}
	else:
		stand = ('Not found', 404)
	return stand