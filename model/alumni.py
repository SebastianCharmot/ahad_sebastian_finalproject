from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb+srv://ahadbadruddin:fuckthisshit@bytefinalproject-5nqms.mongodb.net/test?retryWrites=true&w=majority")
db=client.finalProject

class Alumni():
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('_id')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.class_ = kwargs.get('class')
        self.email = kwargs.get('email')
        self.image = kwargs.get('image')
        self.projects = kwargs.get('projects',[])
        self.bio = kwargs.get('bio')
        self.contribution = kwargs.get('contribution',0)

    @classmethod
    def findUser(cls,username,password):
        object_ = db.Alumni.find_one({
            'username': username,
            'password': password
            })
        return cls(**object_)

    

    def save(self):
        alumniUser = {
            'name' : self.name,
            'username' : self.username,
            'password' : self.password,
            'class': self.class_,
            'email': self.email,
            'image': self.image,
            'projects': self.projects,
            'bio': self.bio,
            'contribution': self.contribution
            }
        if(db.Alumni.find_one({
            'username': self.username,
            'password': self.password
            })):
            updateOb= db.Alumni.update_one({
            'username': self.username,
            'password': self.password
            }, { "$set": alumniUser })
        else:
            result=db.Alumni.insert_one(alumniUser)

    def addproject(self,projectTitle):
        self.projects.append(projectTitle)
        self.save()

    def addContribution(self, amount):
        self.contribution += amount
        self.save()

        
        
    
