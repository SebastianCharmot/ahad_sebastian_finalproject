from model.project import Project
from unittest import TestCase

# to execute from the base of the project directory structure run:
# python3 -m unittest tests/testProject.py
# to run all tests in a directory run:
# python3 -m unittest tests discover

class TestProject(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testSave(self):
        projectTest = {
    'title': 'Trip to South Africa',
    'sDescription': 'I want to go to South Africa',
    'lDescription': 'i really want to go to south Africa',
    'image': '<imagepath>/image.png',
    'funding required': 1000,
    'funding recieved': 10,
    'completed': False,
    'category': 'Women in Tech',
    'likes': [],
    'comments': [
        {"John Bomba": "yooo this is sick broo"},
    ],
    'alumni contribution': [
        {"John Bomba": 10}
    ],
    'student': ['John Bomba']

}
        southAfrica = Project(**projectTest)
        southAfrica.save()
        















