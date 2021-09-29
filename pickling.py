import pickle
from write_pickle import Object ### Necessary for proper loading of the Object class when pickle.load is called. 

class Object():
	def __init__(self):
		self.name="michael"

a_object = Object()

def write_to_pickle(pickled_filename, _object):
	filehandler = open(pickled_filename, 'wb') 
	pickle.dump(_object, filehandler)
	filehandler.close()
	print "{} file has been written to store object of type {}".format(pickled_filename, _object)
	return

def read_from_pickle(pickled_filename):
	file_pi2 = open(pickled_filename, 'rb') 
	object_pi2 = pickle.load(file_pi2)  ## Make sure object is imported above.
	file_pi2.close()
	print("The object {} has been found from the pickled file".format(object_pi2))
	return object_pi2

if __name__ == "__main__":
	filename = "testing.pickle"
	write_to_pickle(filename, a_object)
	a = read_from_pickle(filename)	
	print(a.name)
