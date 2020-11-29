from selenium import webdriver
from news.models import Article,Category,Member
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class TestProject(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Chrome('funcTests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    #This method tests the program to go to the main URL
    def test_project_runs(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)
