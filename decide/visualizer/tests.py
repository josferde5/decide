import datetime
import time

from authentication.models import UserProfile
from django.contrib import auth
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from base.tests import BaseTestCase
from rest_framework.test import APIClient, APITestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from base import mods

from voting.models import Voting

from decide.voting.models import Question, QuestionOption


class AdminTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

    def test_viewVisualizerGlobalLink(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.LINK_TEXT, "View global statistics").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".heading")
        assert len(elements) > 0
        self.driver.close()

    def test_visualizerGlobalTable1(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(1)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(2)")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(3)").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(3)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(4) th:nth-child(4)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(5)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(6)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "th:nth-child(7)")
        assert len(elements) > 0
        self.driver.close()

    def test_visualizerGlobalTable2(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(1)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(2)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(3)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(5) th:nth-child(4)")
        assert len(elements) > 0
        self.driver.close()

    def test_visualizerGlobalTable3(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.XPATH, "//a[contains(@href, \'/visualizer/global\')]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(1)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(2)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(3)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".table:nth-child(6) th:nth-child(4)")
        assert len(elements) > 0
        self.driver.close()



class List_View_Tests(APITestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_list_voting_200(self):
        response = self.client.get('/visualizer/')
        self.assertEqual(response.status_code, 200)

    def test_get_votings_from_list_voting_anonymous(self):
        response = self.client.get('/visualizer/')
        votings = response.context['votings']
        self.assertEqual(votings, [])

    def test_get_votings_from_list_voting_admin(self):
        voting = Voting(name='test', desc='r')
        voting.save()

        user_admin = UserProfile(username='admin', sex='F', style='N', is_staff=True, is_superuser=True, is_active=True)
        user_admin.set_password('qwerty')
        user_admin.save()
        self.client.force_login(user_admin)

        response = self.client.get('/visualizer/')
        votings = response.context['votings']

        self.client.logout()

        self.assertEqual(votings.first(), voting)

    def test_search_filter(self):
        date = datetime.datetime.now()
        voting = Voting(name='test 1', desc='r')
        voting.save()

        voting2 = Voting(name='test 2', desc='r', start_date=date)
        voting2.save()

        voting3 = Voting(name='test 3', desc='r', start_date=date, end_date=date)
        voting3.save()

        user_admin = UserProfile(username='admin', sex='F', style='N', is_staff=True, is_superuser=True, is_active=True)
        user_admin.set_password('qwerty')
        user_admin.save()
        self.client.force_login(user_admin)

        response = self.client.get('/visualizer/?filter=A')
        votings = response.context['votings']
        self.assertEqual(votings.first(), voting2)
        self.assertEqual(votings.count(), 1)
        response = self.client.get('/visualizer/?filter=S')
        votings = response.context['votings']
        self.assertEqual(votings.first(), voting)
        self.assertEqual(votings.count(), 1)
        response = self.client.get('/visualizer/?filter=Fn')
        votings = response.context['votings']
        self.assertEqual(votings.first(), voting3)
        self.assertEqual(votings.count(), 1)
        response = self.client.get('/visualizer/?nombre=1')
        votings = response.context['votings']
        self.assertEqual(votings.first(), voting)
        self.assertEqual(votings.count(), 1)
        response = self.client.get('/visualizer/?nombre=3')
        votings = response.context['votings']
        self.assertEqual(votings.first(), voting3)
        self.assertEqual(votings.count(), 1)

        self.client.logout()



class List_view_test_selenium(StaticLiveServerTestCase):

    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        voting = Voting(name='Test Voting', desc='r')
        voting.save()

        user_admin = UserProfile(username='decide', sex='F', style='N', is_staff=True, is_superuser=True, is_active=True)
        user_admin.set_password('decide98')
        user_admin.save()

        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

    def test_get_list_voting(self):
        self.driver.get(f'{self.live_server_url}/visualizer/')
        self.driver.set_window_size(1386, 692)
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Voting list"
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "b:nth-child(12)").text == "As you are not a superuser, you can only see the votes in which you are in the census"

    def test_search_filter_list_votings(self):
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1299, 741)
        self.driver.find_element(By.ID, "id_username").send_keys("decide")
        self.driver.find_element(By.ID, "id_password").send_keys("decide98")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(2)").click()
        self.driver.get(f'{self.live_server_url}/visualizer/')
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "tr:nth-child(2) > td:nth-child(2)").text == "Test Voting"
        self.driver.find_element(By.ID, "nombre").click()
        self.driver.find_element(By.ID, "nombre").send_keys("Test")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "tr:nth-child(2) > td:nth-child(2)").text == "Test Voting"
        self.driver.find_element(By.LINK_TEXT, "Finished, no tally").click()
        self.driver.find_element(By.LINK_TEXT, "Finished, with tally").click()
        self.driver.find_element(By.LINK_TEXT, "Without starting").click()
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text == "Test Voting"
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()


class Statistics_View_Tests(BaseTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_detail_voting_20(self):
        response = self.client.get('/visualizer/20/statistics')
        self.assertEqual(response.status_code, 200)

    def test_get_detail_voting_404(self):
        response = self.client.get('/visualizer/1010/statistics')
        self.assertEqual(response.status_code, 404)


class Statistics_View_Tests_Selenium(StaticLiveServerTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp()
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        user_admin = UserProfile(username='decide', sex='M', style='N', is_staff=True, is_superuser=True, is_active=True)
        user_admin.set_password('practica1234')
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
        self.base.tearDown()

    def test_statisticsWithLogin(self):
        voting = Voting(name='test 1', desc='r')
        voting.save()
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1920, 1000)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("decide")
        self.driver.find_element(By.ID, "id_password").send_keys("practica1234")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.get(f'{self.live_server_url}/visualizer/1/statistics')

class Identity_chart_test(BaseTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]
    
    def setUp(self):
        user_admin = UserProfile(username='admin1', sex='F', style='C', is_staff=True, is_superuser=True,
                                 is_active=True)
        user_admin.set_password('qwerty')
        user_admin.save()
        self.client.force_login(user_admin)

        super().setUp()

    def tearDown(self):
        self.client.logout()
        super().tearDown()

    def test_positive_view_identity_chart(self):
        response = self.client.get('/visualizer/23/')
        voting_type = response.context["type"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(voting_type, "IDENTITY")

    def test_negative_view_identity_chart(self):
        response = self.client.get('/visualizer/999999')
        self.assertEqual(response.status_code, 301)

    def test_positive_view_identity_chart_data(self):
        response = self.client.get('/visualizer/23/')
        voting_type = response.context["type"]
        labels = response.context["labels"]
        data = response.context["data"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(voting_type, "IDENTITY")
        self.assertEqual(labels, "['Rojo', 'Azul', 'Amarillo', 'Verde']")
        self.assertEqual(data, "[9, 8, 4, 4]")

    def test_negative_view_identity_chart_data(self):
        response = self.client.get('/visualizer/23/')
        voting_type = response.context["type"]
        options = response.context['options']
        votes_men = response.context['votes_men']
        votes_women = response.context['votes_women']
        gender_census = response.context['gender_census']
        results = response.context['results']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(voting_type, "IDENTITY")
        self.assertEqual(options, None)
        self.assertEqual(votes_men, None)
        self.assertEqual(votes_women, None)
        self.assertEqual(gender_census, None)
        self.assertEqual(results, None)

class Identity_chart_view_test_selenium(StaticLiveServerTestCase):
    fixtures = ['visualizer/migrations/populate.json', ]

    def setUp(self):
        self.client = APIClient()
        self.token = None
        mods.mock_query(self.client)
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        user_admin = UserProfile(username='admin', sex='F', style='N', is_staff=True, is_superuser=True)
        user_admin.set_password('qwerty')
        user_admin.save()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

    def test_identity_view(self):
        voting = Voting(name='test 1', desc='r')
        voting.save()
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1920, 1000)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.get(f'{self.live_server_url}/visualizer/23/')

    def test_identity_chart_view(self):
        voting = Voting(name='test 1', desc='r')
        voting.save()
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1920, 1000)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.get(f'{self.live_server_url}/visualizer/23/')
        self.driver.find_element(By.CSS_SELECTOR, "canvas.identityChart").is_displayed()
