#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from contentnews.models import News
from tests.settings import USER1_EMAIL, USER1_PASSWORD, USER1_STATUS, USER2_EMAIL,\
    USER2_PASSWORD, USER2_STATUS, NEWS1_CATEGORY, NEWS1_TITLE, NEWS1_CONTENT, NEWS1_STATUS

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True

class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """
    This class allows us to test pages of the application for Firefox browser
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=str(settings.BASE_DIR / 'webdrivers' / 'geckodriver'),
            options=firefox_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            email=USER1_EMAIL,
            password=USER1_PASSWORD,
            status=USER1_STATUS,
        )

        self.user2 = User.objects.create_user(
            email=USER2_EMAIL,
            password=USER2_PASSWORD,
            status=USER2_STATUS,
        )

        self.news1 = News.objects.create(
            category=NEWS1_CATEGORY,
            title=NEWS1_TITLE,
            content=NEWS1_CONTENT,
            status=NEWS1_STATUS,
            author=self.user1
        )

    def user_connection(self):
        # Call the web application
        self.driver.get(self.live_server_url)
        # Localise the text field and we enter and confirm a email
        self.driver.find_element_by_id('login-id').send_keys(USER1_EMAIL)
        # idem for password
        self.driver.find_element_by_id('login-password').send_keys(USER1_PASSWORD)
        # Submit form
        self.driver.find_element_by_css_selector(
            'section.login-main-section form button'
        ).click()

    def test_login_form(self):
        """
        Test the login form
        """
        self.user_connection()
        # To know if we have been redirected to the home page after login,
        # we look for a specific tag for this page
        element_to_find = self.driver.find_element_by_css_selector(
            'div.index-welcome-title h1'
        )
        # Check that the chosen tag contains a text that is only found on the home page
        self.assertEqual(
            element_to_find.text, 'Bienvenue sur le site de notre copropriété'
        )

    def test_homepage_to_news(self):
        """
        Test the large search engine on the homepage
        """
        self.user_connection()
        # Localise and click the news link
        self.driver.find_element_by_css_selector('li.site-menu-1').click()
        # To know if we have been redirected to the news page after clicking on the link,
        # look for a specific tag for this page
        element_to_find = self.driver.find_element_by_css_selector(
            'div.page-title-block h1'
        )
        # Check that the chosen tag contains a text that is only found on the news page
        self.assertEqual(element_to_find.text, 'Les news')

    def test_newslist_to_newsdetail(self):
        """
        Test the transition from the list of news to the page of a particular news
        """
        self.user_connection()
        # Localise and click the news link
        self.driver.find_element_by_css_selector('li.site-menu-1').click()
        # Got to detailed news page
        self.driver.find_element_by_css_selector('div.content-list-item').click()
        # Find news detail title
        title = self.driver.find_element_by_css_selector('div.news-detail-title')
        self.assertEqual(title.text, NEWS1_TITLE)

        # Close the browser window
        self.driver.close()

    def test_contact_form(self):
        """
        Test the contact form
        """
        self.user_connection()

        # Go to the contact page
        self.driver.find_element_by_css_selector('div.f-contact a').click()
        title = self.driver.find_element_by_class_name('page-header-title')
        self.assertEqual(title.text, 'Contact')
        # Locate and fill in the various fields of contact form
        self.driver.find_element_by_id('id_first_name').send_keys('Nicolas')
        self.driver.find_element_by_id('id_last_name').send_keys('Valdem')
        self.driver.find_element_by_id('id_email_address').send_keys('nicolas.valdem@free.fr')
        # Select a user type
        user_type = self.driver.find_element_by_id('id_user_type')
        drop1 = Select(user_type)
        drop1.select_by_visible_text('Locataire')
        # Select a message subject
        message_subject = self.driver.find_element_by_id('id_message_subject')
        drop2 = Select(message_subject)
        drop2.select_by_visible_text('Le site')
        # The message
        editorFrame = self.driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
        self.driver.switch_to_frame(editorFrame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys('Lorem ipsum blablabla contact form')
        self.driver.switch_to_default_content()
        # Submit form
        self.driver.find_element_by_css_selector('form button').click()

        # To know if we have been redirected to the contact success page after submit,
        # look for a specific tag for this page
        element_to_find = self.driver.find_element_by_class_name('contact-success-msg')
        # We check that the chosen tag contains a text that is only found on the
        # contact success page
        self.assertEqual(element_to_find.text, 'Votre message a été envoyé avec succès !')
