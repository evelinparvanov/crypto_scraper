# Cryptocurrency Data Scraper README

## Overview:
This script utilizes the Selenium library to scrape data from the CoinMarketCap website, specifically focusing on the trending cryptocurrencies. It fetches information such as rank, name, symbol, price, changes in various timeframes, market cap, volume in the last 24 hours, and circulating supply for each cryptocurrency. The data is then stored in a CSV file with today's date as part of the filename.
## Usage:
1. Ensure you have Python 3.12 installed.
2. Install the Selenium library if you haven't already (`pip install selenium`).
3. Download the appropriate Chrome WebDriver for your Chrome browser version from [Chrome WebDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the chromedriver executable file in your system PATH or specify its location in the script.
4. Clone or download the script `crypto_scraper.py` from this repository.
5. Run the script `crypto_scraper.py` in your Python environment.

## File Structure:
- `crypto_scraper.py`: The main Python script file for scraping cryptocurrency data.
- `README.md`: This README file providing information about the script.
- `LICENSE`: License information for the script (MIT License).

## Notes:
- Ensure that you have a stable internet connection while running the script.
- This script is designed to fetch data from CoinMarketCap's website, any changes in the website structure may require modifications to the script.
- Make sure to comply with CoinMarketCap's terms of service and robots.txt file while scraping data from their website.

## Contributing:
Contributions are welcome! If you encounter any issues, bugs, or have suggestions for improvements, feel free to open an issue or create a pull request on the GitHub repository.

## License:
MIT License

Copyright (c) 2024 Evelin Parvanov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
...
