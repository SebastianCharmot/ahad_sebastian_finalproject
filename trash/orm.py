from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb+srv://ahadbadruddin:fuckthisshit@bytefinalproject-5nqms.mongodb.net/test?retryWrites=true&w=majority")
db=client.finalProject
class MongodbORM:

    def __init__(self):
        raise NotImplementedError
    @classmethod
    def new_insert(cls, newJson): 
        table = cls.dbtable
        post = db.table.insert_one(newJson)

    @classmethod
    def update(cls, whereJSON ,updateJSON):
        table = cls.dbtable
        updateOb= db.table.update_one(whereJSON, { "$set": updateJSON })

    @classmethod
    def addToArray(cls,whereJSON ,updateJSON):
        table = cls.dbtable
        updateOb= db.table.update_one(whereJSON, { "$push": updateJSON })


    @classmethod
    def one_whereStudent(cls, whereJson):
        object_ = db.Students.find_one(whereJson)
        return cls(**object_)


    
































studentTest = {
        'name' : "John Bomba",
        'username' : "mutantseabass",
        'password' : "password",
        'class':'1900',
        'email':'theJohnBomba@gmail.com',
        'image':'<imagepath>/image.png',
        'projects': ["Trip to South Africa", "3D Printer", "*enter bogus startup idea*"],
        'bio': 'im the john bomba. there is nothing else to say. Papa John\'s sucks. people who use umbrellas are idiots.',
        'major':'cybersecurity'
        

    }
projectTest = {
    'title': 'Trip to South Africa',
    'sDescription': 'I want to go to South Africa',
    'lDescription': 'i really want to go to south Africa',
    'image': '<imagepath>/image.png',
    'Funding Required': 1000,
    'Funding Recieved': 10,
    'Completed': False,
    'Category': 'Women in Tech',
    'Likes': [],
    'Comments': [
        {"John Bomba": "yooo this is sick broo"},
    ],
    'Alumni Contribution': [
        {"John Bomba": 10}
    ],
    'student': ['John Bomba']

}

alumniTest= {
    'name':'Billy Bob',
    'username': 'billybob',
    'password': 'password',
    'class':'2003',
    'email':'billybob@gmail.com',
    'image':'<imagepath>/image.png',
    'projects':[],
    'contribution': 0,
    'bio':'i work at Goldman Sachs'

}
#Step 3: Insert business object directly into MongoDB via isnert_one
#result=db.Projects.insert_one(projectTest)

#fivestar = db.Project.find_one({'student': "John Bomba"})
#postAlumni = db.Alumni.insert_one(alumniTest)
#updateJohn= db.Projects.update_one({'title': "Trip to South Africa"}, { "$push": { "student": "John Doe" } })
#print(fivestar)


