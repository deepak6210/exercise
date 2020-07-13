import requests
import pickle

r = requests.get("file:///C:/Users/Deepak/AppData/Local/Temp/abalone.data")
file = "data.pkl"
fileobj = open(file, 'wb')
pickle.dump(r, fileobj)
fileobj.close()