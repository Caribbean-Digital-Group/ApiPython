import hug

@hug.get('/home')
def root():
    return {'mensaje':'Bienvenido a casa!'}
@hug.get('/home/suma')
def root():
    return {'mensaje':'Bienvenido a las sumas'}

@hug.sink('/all') 
def my_sink(request): 
	return request.path.replace('/all', '/home') 