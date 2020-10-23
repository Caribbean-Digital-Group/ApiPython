import hug

"""Api para sumar 2 numeros"""

@hug.get()
@hug.cli() 
def add(number_1: hug.types.number, number_2: hug.types.number): 
	"""Devuelve el resultado de sumar number_1 y number_2""" 
	return {"Resultado": "La suma de {0} + {1} es: {2}".format(number_1, number_2, (number_1 + number_2))}

if __name__ == '__main__': add.interface.cli()