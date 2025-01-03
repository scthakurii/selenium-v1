import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up the Chrome WebDriver
# Use Service to specify the path to the ChromeDriver executable
service = Service(ChromeDriverManager().install())

# Configure Chrome options to specify the binary location if necessary
options = Options()
# If Chrome is installed in a non-default location, uncomment and set the correct path
# options.binary_location = "/path/to/your/chrome/binary" 

driver = webdriver.Chrome(service=service, options=options) 
driver.get('https://www.thelott.com/saturday-lotto/results')
time.sleep(15) # Wait for 15 seconds to allow the browser to open
# Define the years and months to iterate over

months = range(1, 13)  # 1 to 12 inclusive
years = range(2016, 2025)  # 2016 to 2024 inclusive


# Open a CSV file to write the results
with open('lottery_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Winning Numbers', 'Supplementary Numbers'])

    for year in years:
        for month in months:
            try:
                # Select the year
                year_dropdown = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'year-dropdown'))  # Correct ID
                )
                Select(year_dropdown).select_by_value(str(year))

                # Select the month
                month_dropdown = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'month-dropdown'))  # Correct ID
                )
                Select(month_dropdown).select_by_value(str(month))

                # Click the 'Find' button
                find_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'find-button'))  # Correct ID
                )
                find_button.click()

                # Wait for the results to load
                time.sleep(15) # Increase if needed

                # Extract results
                results = driver.find_elements(By.CLASS_NAME, 'result')  # Correct class name
                for result in results:
                    date = result.find_element(By.CLASS_NAME, 'date').text  # Correct class name
                    winning_numbers = result.find_element(By.CLASS_NAME, 'winning-numbers').text  # Correct class name
                    supplementary_numbers = result.find_element(By.CLASS_NAME, 'supplementary-numbers').text  # Correct class name

                    # Write to CSV
                    writer.writerow([date, winning_numbers, supplementary_numbers])

            except Exception as e:
                print(f"An error occurred for {year}-{month}: {e}")

# Close the WebDriver
driver.quit()