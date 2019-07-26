from model.alumni import Alumni
from unittest import TestCase

# to execute from the base of the project directory structure run:
# python3 -m unittest tests/testAlumni.py
# to run all tests in a directory run:
# python3 -m unittest tests discover

class TestAlumni(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testOneWhere(self):
        billy = Alumni.findUser('billybob', 'password' )
        self.assertEqual(billy.name,'Billy Bob',"Object returned has correct properties")

    def testSave(self):
        marlon = Alumni(name='Marlon Card', password = 'password', username='marloncard', email='mikebloom@gmail.com', projects=[{'test':0},{'test2':30}])
        marlon.save()
        marlon.class_= '1900'
        marlon.save()
        marlon2 = Alumni.findUser('marloncard', 'password' )
        self.assertEqual(marlon2.projects[0]['test'],0,"Object returned has correct properties")

    def testAddProject(self):
        greg = Alumni.findUser('gregbloom', 'password')
        greg.projects = [{'*non bogus startup idea*':5000}]
        greg.save()

        