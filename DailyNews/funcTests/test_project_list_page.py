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

    def test_project_account_creation(self):
        self.browser.get(self.live_server_url)

        #finds the signup button on the HTML and clicks it
        self.browser.find_element_by_name("signup").click()

        #Period of waiitng 5 seconds to allow the page to load
        time.sleep(5)

        #find all 3 inputs for registration
        email = self.browser.find)find_element_by_id("registerEmail")
        username = self.browser.find_element_by_id("registerMember")
        password = self.browser.find_element_by_id("password")

        #sends the input for all the 3 details for registration
        email=send_keys("something@gmail.com")
        username.send_keys("123")
        password.send_keys("123")

        #Waiting of 20 seconds to allow user to check the database to see that user has been registered
        time.sleep(20)


    def test_project_login_liking_posting_deleting(self):
        self.browser.get(self.live_server_url)
        #Finds the login button and clicks it to redirect to the login page
        self.browser.find_element_by_name("login").click()

        #5 Seconds to allow it to load
        time.sleep(5)

        #Finds the 2 inputs needed to login
        username = self.browser.find_element_by_id("loginMember")
        password = self.browser.find_element_by_id("password")

        #Sends in the details for the inputs to login
        username.send_keys("123")
        password.send_keys("123")

        #user clicks the like buttons
        self.browser.find_element_by_name("like-button").click()

        #Finds the comment section of the first article and submits a test comment
        comment = self.browser.find_element_by_id("postingComment")
        comment.send_keys("This is the test comment")
        self.browser.find_element_by_id("postingSubmit")

        time.sleep(5)

        #Deletes the first comment which is the latest comment that we sent as a test.
        self.browser.find_element_by_class("deleteComment").click()
