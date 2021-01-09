import pickle
class likeDB:
  
    def saveObject(name,Object):
        name = str(name) + '.pkl'
        with open(name, 'wb') as f:
            pickle.dump(Object, f, pickle.HIGHEST_PROTOCOL)
    #to load object with run code again
    def loadObject(name):
        name = str(name) + '.pkl'
        with open(name, 'rb') as f:
            return pickle.load(f) 
        
    