'''11) WAP to create five dictionaries(sample : Amit={'Name':'Amit','class':'12A','stream':'non-med','percentage':'97'}) where keys signifies the roll number
write two functions storedata and loaddata using pickle module using binary file.'''
import pickle
def storedata():
    Amit = {"Name":"Amit",'class':'12 A','stream':'non-med','percentage':97}
    Rahul = {"Name":"Rahul",'class':'12 B','stream':'med','percentage':96}
    Garima = {"Name":"Garima",'class':'12 C','stream':'commerce','percentage':95}
    Lia = {"Name":"Lia",'class':'12 D','stream':'Arts','percentage':94}
    Camey = {"Name":"Camey",'class':'12 E','stream':'med','percentage':93}
    db = {}
    db['Amit'] = Amit
    db['Rahul'] = Rahul
    db['Garima'] = Garima
    db['Lia'] = Lia
    db['Camey'] = Camey
    dbfile = open("pickle_data","wb")
    pickle.dump(db,dbfile)
    dbfile.close()
def loaddata():
    dfile = open("pickle_data","rb")
    dbl = pickle.load(dfile)
    for keys in dbl:
        print(keys,"=>",dbl[keys])
    dfile.close()
storedata()
loaddata()

