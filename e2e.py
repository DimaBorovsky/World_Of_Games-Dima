from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

webdriver_service = Service('usr/local/bin')

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get("http://localhost:5000")

    time.sleep(2)

    assert "Scores" in driver.title, "Title does not contain 'Scores'"

    score_element = driver.find_element(By.TAG_NAME, "body")

    scores_text = score_element.text


    expected_content = "Team A: 10"
    assert expected_content in scores_text, f"Expected score '{expected_content}' not found!"

    print("Test Passed: Scores are displayed correctly.")
    sys.exit(0)

except AssertionError as e:
    print(f"Test Failed: {e}")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

finally:
    driver.quit()
