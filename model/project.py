from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb+srv://ahadbadruddin:fuckthisshit@bytefinalproject-5nqms.mongodb.net/test?retryWrites=true&w=majority")
db=client.finalProject

class Project():
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('_id')
        self.title = kwargs.get('title')
        self.sDescription = kwargs.get('sDescription')
        self.lDescription = kwargs.get('lDescription')
        self.image = kwargs.get('image')
        self.funding_required = kwargs.get('funding required')
        self.funding_recieved = kwargs.get('funding recieved')
        self.completed = kwargs.get('completed',False)
        self.category = kwargs.get('category')
        self.likes = kwargs.get('likes',[])
        self.comments = kwargs.get('comments',[])
        self.alumni_contribution= kwargs.get('alumni contribution',[])
        self.student= kwargs.get('student',[])

    @classmethod
    def findProject(cls,title):
        object_ = db.Projects.find_one({
            'title': title
            })
        return cls(**object_)

    

    def save(self):
        projectItem = {
            'title' : self.title,
            'sDescription' : self.sDescription,
            'lDescription' : self.lDescription,
            'image': self.image,
            'funding_required': self.funding_required,
            'funding_recieved': self.funding_recieved,
            'completed': self.completed,
            'category': self.category,
            'likes': self.likes,
            'comments': self.comments,
            'alumni_contribution': self.alumni_contribution,
            'student': self.student
            }
        if(db.Projects.find_one({
            'title': self.title,
            })):
            updateOb= db.Projects.update_one({
            'title': title
            }, { "$set": projectItem })
        else:
            result=db.Projects.insert_one(projectItem)

        
        
    
