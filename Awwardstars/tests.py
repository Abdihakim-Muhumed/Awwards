from django.test import TestCase
from .models import Projects,Projects
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.newProfile = Profile(bio='Mybio',contact = '08200000')
        self.newProfile.save_profile()

    def test_instance(self):
        self.assertIsInstance(self.newProfile, Profile)

    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    def test_delete_profile(self):
        self.newProfile.delete_profile()
        profiles = Profile.objects.all()  
        self.assertTrue(len(profiles) == 0)    

class TestProjects(TestCase):
    def setUp(self):
        self.newProjects = Projects(title='FirstProject',description="This is the first one")
        self.newProjects.save_projects()

    def test_instance(self):
        self.assertIsInstance(self.newProjects, Projects)

    def test_save_Projects(self):
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)
    def test_delete_Projects(self):
        self.newProjects.delete_projects()
        projects = Projects.objects.all()  
        self.assertTrue(len(projects) == 0)    


