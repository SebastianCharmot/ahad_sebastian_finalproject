from pymongo import MongoClient
from pprint import pprint

class testfile: 
    def __init__(self):
        self.client = MongoClient("mongodb+srv://ahadbadruddin:fuckthisshit@bytefinalproject-5nqms.mongodb.net/test?retryWrites=true&w=majority")
        self.db=client.finalProject

    def one_where(whereJson):
        object_ = self.db.Students.find_one(whereJson)
        print(object_)
        


if __name__ == '__main__':

    testfile.one_where({'name': 'John Bomba'})