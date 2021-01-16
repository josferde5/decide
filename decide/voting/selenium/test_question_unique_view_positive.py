# Generated by Selenium IDE
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from base.tests import BaseTestCase
from authentication.models import UserProfile

class TestQuestionUniqueViewPositive(StaticLiveServerTestCase):
  def setUp(self):
    self.base = BaseTestCase()
    self.base.setUp()
    user_admin_superuser = UserProfile(username='adminsuper', sex='F', style='N', is_staff=True, is_superuser=True)
    user_admin_superuser.set_password('qwerty')
    user_admin_superuser.save()
    self.base.user_admin = user_admin_superuser

    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    self.vars = {}
    self.driver.maximize_window() #For maximizing window
    self.driver.implicitly_wait(20) #gives an implicit wait for 20 seconds

    super().setUp() 
  
  def tearDown(self):
    super().tearDown()
    self.driver.quit()

    self.base.tearDown()

  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_question_unique_view_positive(self):
    # Test name: question_unique_view_negative
    # Step # | name | target | value
    # 1 | open | http://localhost:8000/admin/ | 
    self.driver.get(f'{self.live_server_url}/admin/')
    self.driver.find_element_by_id("id_username").send_keys("adminsuper")
    self.driver.find_element_by_id("id_password").send_keys("qwerty")
    self.driver.find_element_by_css_selector("div .submit-row input").click()
    # 3 | click | css=.model-question .addlink | 
    self.driver.find_element(By.CSS_SELECTOR, ".model-question .addlink").click()
    # 4 | click | id=id_option_types | 
    self.driver.find_element(By.ID, "id_option_types").click()
    # 5 | select | id=id_option_types | label=Multiple option
    dropdown = self.driver.find_element(By.ID, "id_option_types")
    dropdown.find_element(By.XPATH, "//option[. = 'Multiple option']").click()
    # 6 | click | css=#id_option_types > option:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, "#id_option_types > option:nth-child(2)").click()
    # 7 | click | id=id_desc | 
    self.driver.find_element(By.ID, "id_desc").click()
    # 8 | type | id=id_desc | prueba31
    self.driver.find_element(By.ID, "id_desc").send_keys("pruebaunique1")
    # 9 | click | id=id_options-0-number | 
    self.driver.find_element(By.ID, "id_options-0-number").click()
    # 10 | type | id=id_options-0-number | 1
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    # 11 | click | id=id_options-0-option | 
    self.driver.find_element(By.ID, "id_options-0-option").click()
    # 12 | type | id=id_options-0-option | 1
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("1")
    # 13 | click | id=id_options-1-number | 
    self.driver.find_element(By.ID, "id_options-1-number").click()
    # 14 | type | id=id_options-1-number | 2
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    # 15 | click | id=id_options-1-option | 
    self.driver.find_element(By.ID, "id_options-1-option").click()
    # 16 | type | id=id_options-1-option | 2
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("2")
    # 17 | click | name=_save | 
    self.driver.find_element(By.NAME, "_save").click()
    # 18 | click | css=.addlink | 
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    # 19 | click | id=id_option_types | 
    self.driver.find_element(By.ID, "id_option_types").click()
    # 20 | select | id=id_option_types | label=Rank order scale
    dropdown = self.driver.find_element(By.ID, "id_option_types")
    dropdown.find_element(By.XPATH, "//option[. = 'Rank order scale']").click()
    # 21 | click | css=#id_option_types > option:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, "#id_option_types > option:nth-child(3)").click()
    # 22 | click | id=id_desc | 
    self.driver.find_element(By.ID, "id_desc").click()
    # 23 | type | id=id_desc | prueba31
    self.driver.find_element(By.ID, "id_desc").send_keys("pruebaunique2")
    # 24 | click | id=id_options-0-number | 
    self.driver.find_element(By.ID, "id_options-0-number").click()
    # 25 | type | id=id_options-0-number | 1
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    # 26 | click | id=id_options-0-option | 
    self.driver.find_element(By.ID, "id_options-0-option").click()
    # 27 | type | id=id_options-0-option | 1
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("1")
    # 28 | click | id=id_options-1-number | 
    self.driver.find_element(By.ID, "id_options-1-number").click()
    # 29 | type | id=id_options-1-number | 2
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    # 30 | click | id=id_options-1-option | 
    self.driver.find_element(By.ID, "id_options-1-option").click()
    # 31 | type | id=id_options-1-option | 2
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("2")
    # 32 | click | id=id_type | 
    self.driver.find_element(By.ID, "id_type").click()
    # 33 | select | id=id_type | label=BORDA
    dropdown = self.driver.find_element(By.ID, "id_type")
    dropdown.find_element(By.XPATH, "//option[. = 'BORDA']").click()
    # 34 | click | css=#id_type > option:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, "#id_type > option:nth-child(2)").click()
    # 35 | click | name=_save | 
    self.driver.find_element(By.NAME, "_save").click()
    # 36 | assertText | css=li | Question with this Desc already exists.
    assert self.driver.find_element(By.LINK_TEXT, "pruebaunique1").text == "pruebaunique1"
    assert self.driver.find_element(By.LINK_TEXT, "pruebaunique2").text == "pruebaunique2"
  
