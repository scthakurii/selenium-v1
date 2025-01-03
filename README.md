# Lottery Results Scraper

This project is a Python script that automates the scraping of lottery results from the Saturday Lotto results page on [theLott website](https://www.thelott.com/saturday-lotto/results). The script uses Selenium WebDriver to interact with the website and extracts lottery results for a specified range of years and months, saving the data to a CSV file.

## Features

- Automatically navigates the website to retrieve lottery results.
- Extracts data including the draw date, winning numbers, and supplementary numbers.
- Saves the extracted data to a CSV file (`lottery_results.csv`).
- Logs progress and errors for each year and month.
- Captures screenshots if errors occur, helping with debugging.

## Requirements

Ensure the following tools and libraries are installed:

- Python 3.8+
- Google Chrome Browser
- Selenium
- WebDriver Manager

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/scthakurii/selenium-v1.git
   cd selenium-v1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** Ensure `chromedriver` is compatible with your installed Chrome version. The script uses `webdriver-manager` to handle this automatically.

3. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. The script will:

   - Navigate to the Saturday Lotto results page.
   - Iterate through the defined years (2016-2024) and months.
   - Scrape and save the results to `lottery_results.csv`.

3. Results:

   - Check the `lottery_results.csv` file for the scraped data.
   - If errors occur, screenshots will be saved in the `screenshots` directory.

## Configuration

- Modify the range of years or list of months in the script:
  ```python
  years = range(2016, 2025)  # Modify year range
  months = ["January", "February", "March", ...]  # Modify months
  ```

## Project Structure

```
.
├── main.py                # Main script for scraping
├── requirements.txt       # Python dependencies
├── lottery_results.csv    # Output file with lottery results
├── screenshots/           # Directory for debug screenshots (created if errors occur)
└── README.md              # Project documentation
```

## Dependencies

- `selenium`: Web automation library.
- `webdriver-manager`: Handles the setup of ChromeDriver.
- `time`, `csv`, `os`, `traceback`: Built-in Python modules for time handling, file I/O, and debugging.

Install them using:

```bash
pip install selenium webdriver-manager
```

## Debugging

- If an error occurs, check the console logs for the stack trace.
- Screenshots of the error state will be saved in the `screenshots` directory for further inspection.
- Ensure that the website structure or element identifiers (CSS selectors) have not changed.

## Contribution

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This script is provided for educational purposes only. Use it responsibly and ensure you comply with the terms and conditions of the website being scraped.

## Author

[Sam JR](https://github.com/scthakurii)

