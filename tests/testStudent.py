from model.student import Student
from unittest import TestCase

# to execute from the base of the project directory structure run:
# python3 -m unittest tests/testStudent.py
# to run all tests in a directory run:
# python3 -m unittest tests discover

class TestStudent(TestCase):
    def setUp(self):

        pass
    def tearDown(self):
        pass
    
    def testOneWhere(self):
        john = Student.findUser('mutantseabass', 'password' )
        self.assertEqual(john.name,'John Bomba',"Object returned has correct properties")

    def testSave(self):
        mike = Student(name='Mike Bloom', password = 'password', username='mikebloom', email='mikebloom@gmail.com')
        mike.save()
        mike.class_= '1900'
        mike.save()
        mike2 = Student.findUser('mikebloom', 'password' )
        self.assertEqual(mike2.class_,'1900',"Object returned has correct properties")
    def testAddProject(self):
        


    


