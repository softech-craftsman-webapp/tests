from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from numpy import arange
import unittest

class JobOfferDriver():
    def __init__(self):
        pass

    def open_browser(self, browser_type, is_headless, install_chrome_driver = True):
        
        if (browser_type.lower() == 'chrome'):
            print('Opening chrome')
            chrome_options = webdriver.chrome.options.Options()
            chrome_options.add_argument("--window-size=1600,1000")

            if (is_headless):
                chrome_options.add_argument("--headless")

            if (install_chrome_driver):
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            else:
                self.driver = webdriver.Chrome(options=chrome_options)
        
        if (browser_type.lower() == 'firefox'):
            print('Opening firefox')
            firefox_options = webdriver.firefox.options.Options()
            
            if (is_headless):
                firefox_options.add_argument('--headless')
            
            self.driver = webdriver.Firefox(options=firefox_options)
            

    def get_element(self, search_tag, search_term):
        return self.driver.find_element(search_tag, search_term)

    def click_on_button(self, text):
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in buttons:
            if button.text == text:
                button.click()
                return

        print('Button with text [', text, '] not found!')
        raise AssertionError

    def fill_create_jobb_offer(self, visible_text = 'IT'):
        select_box = Select(self.driver.find_element(By.ID, 'category_id'))
        select_box.select_by_visible_text(visible_text)

        self.click_on_button('Next')
        sleep(2)

        title_input_field = self.driver.find_element(By.ID, 'name')
        title_input_field.send_keys('Test Title')

        description_field = self.driver.find_element(By.ID, 'description')
        description_field.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

        date_field = self.driver.find_element(By.ID, 'valid_until')
        date_field.send_keys('20220101')
        
        equipment_field = Select(self.driver.find_element(By.ID, 'is_equipment_required'))
        # TODO: Allow test case to specify wether equipment should be required
        equipment_field.select_by_visible_text('No')

        self.click_on_button('Next')
        sleep(2)
        self.click_on_button('Next')
        sleep(2)
        self.click_on_button('Pay')
        sleep(0.5)
        self.click_on_button('Next')
        sleep(3)
        self.click_on_button('Create Job')

    def open_created_job_offers(self):
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div/div/a[1]').click()

    def open_and_login(self):
        self.driver.get('https://hiringo.tech/auth/sign-in/')
        sleep(5)
        self.driver.find_element(By.ID, 'email').send_keys('test@testing.test')
        self.driver.find_element(By.ID, 'password').send_keys('test1234')
        sleep(3)
        
        button = self.driver.find_element(By.TAG_NAME, 'button')
        button.click()
        sleep(3)

    def open_job_offers(self):
        list = self.driver.find_element(By.TAG_NAME, 'ul')
        items = list.find_elements(By.TAG_NAME, 'li')
        items[1].click()

    def search_job_offer(self, search_term):
        input = self.driver.find_element(By.TAG_NAME, 'input')
        input.send_keys(search_term)

        self.click_on_button('Search')
    
    def open_job_offer(self, id='0'):
        job = self.driver.find_element(By.ID, 'job-id-' + id)
        job.click()

    def open_create_job_offer(self):
        # Create job offer button XPATH: /html/body/div/div[2]/div[2]/main/div/div/div/a[3] note: click_on_button didn't seem to work
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div/div/a[3]').click()

    def apply_for_job(self):
        self.click_on_button('Apply now')

    def fill_time(self, input, time):
        input.click()

        input.send_keys(time[0:4])
        input.send_keys(Keys.ARROW_RIGHT)

        for i in arange(4, 11, 2):
            input.send_keys(time[i:i+2])

    def fill_apply_times(self, start_time, end_time):
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')

        self.fill_time(inputs[0], start_time)
        self.fill_time(inputs[1], end_time)

    def close(self):
        self.driver.close()
    

class JobOfferTests(unittest.TestCase):

    def setUp(self):
        self.browser_type = 'chrome'
        self.is_headless = True
        self.tester = JobOfferDriver()

    def tearDown(self):
        self.tester.close()

    def test_opening_job_offer_page(self):
        print("\n[TESTING OPENING PAGE]")
        
        self.tester.open_browser(self.browser_type, self.is_headless)
        sleep(2)
        self.tester.open_and_login()
        sleep(1)
        self.tester.open_job_offers()
        sleep(2)

        job_offer_heading = self.tester.get_element(By.TAG_NAME, 'h1').text
        self.assertEqual(job_offer_heading, 'Job Offers')

    def test_create_job_offer(self):
        print("\n[TESTING CREATING A NEW JOB OFFER]")

        self.tester.open_browser(self.browser_type, self.is_headless)
        sleep(2)
        self.tester.open_and_login()
        sleep(1)
        self.tester.open_job_offers()
        sleep(3)
        self.tester.open_create_job_offer()
        sleep(2)
        header = self.tester.get_element(By.TAG_NAME, 'h1').text
        self.assertEqual(header, 'Create new job')

        self.tester.fill_create_jobb_offer()
        sleep(4)
        
        self.tester.open_created_job_offers()
        sleep(3)

        job = self.tester.get_element(By.ID, 'job-id-0')

        self.assertIsNotNone(job)

        # Delete created job
        job.click()
        sleep(2)
        self.tester.click_on_button('Delete')

    def test_searching_job_offers(self):
        print("\n[TESTING SEARCHING FOR AN OFFER]")
        
        self.tester.open_browser(self.browser_type, self.is_headless)
        self.tester.open_and_login()
        sleep(1)
        self.tester.open_job_offers()
        sleep(1)
        self.tester.search_job_offer('a')

        sleep(2)

        job = self.tester.get_element(By.ID, 'job-id-0')
        self.assertIsNotNone(job)

    def test_opening_job_offer(self):
        print("\n[TESTING OPENING AN OFFER]")
        
        self.tester.open_browser(self.browser_type, self.is_headless)
        sleep(2)
        self.tester.open_and_login()
        sleep(1)
        self.tester.open_job_offers()
        sleep(2)
        self.tester.search_job_offer('a')
        sleep(2)

        id = '0'
        job_title_before = self.tester\
            .get_element(By.ID, 'job-id-' + id)\
            .find_element(By.TAG_NAME, 'h4').text

        self.tester.open_job_offer(id)
        sleep(2)

        headings = self.tester\
            .get_element(By.ID, 'job_details')\
            .find_elements(By.TAG_NAME, 'h4')

        self.assertEqual(headings[0].text, 'Information')
        self.assertEqual(headings[1].text, 'Applications')

        job_title_after = self.tester.get_element(By.TAG_NAME, 'h1').text

        self.assertEqual(job_title_before, job_title_after)

    def test_apply_for_job(self):
        print("\n[TESTING APPLYING FOR A JOB]")
        
        self.tester.open_browser(self.browser_type, self.is_headless)
        sleep(3)
        self.tester.open_and_login()
        sleep(2)
        self.tester.open_job_offers()
        sleep(2)
        self.tester.search_job_offer('a')
        sleep(3)

        self.tester.open_job_offer('2')
        sleep(3)

        applications_before = self.tester\
            .get_element(By.ID, 'job_details')\
            .find_elements(By.TAG_NAME, 'a')

        self.tester.apply_for_job()
        sleep(3)

        heading = self.tester.get_element(By.TAG_NAME, 'h1').text
        self.assertEqual(heading, 'aaa')

        contract_texts = self.tester\
            .get_element(By.ID, 'contract')\
            .find_elements(By.TAG_NAME, 'p')

        self.assertEqual(contract_texts[0].text, 'Contract')
        self.assertIsNotNone(contract_texts[2].text)

        self.tester.fill_apply_times('200001011000', '200002011000')
        self.tester.click_on_button('Apply')
        sleep(3)

        applications_after = self.tester\
            .get_element(By.ID, 'job_details')\
            .find_elements(By.TAG_NAME, 'a')

        self.assertGreater(len(applications_after), len(applications_before))


if __name__ == '__main__':
    unittest.main()