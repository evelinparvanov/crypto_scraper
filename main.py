import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

"""
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
...
"""

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get("https://coinmarketcap.com/trending-cryptocurrencies/")

all_crypto_currencies = driver.find_elements(By.XPATH,
                                             '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr')

crypto_list = []

for crypto_currency in all_crypto_currencies[:30]:
    elements = crypto_currency.find_elements(By.TAG_NAME, "td")
    if elements:
        rank = elements[1].text
        name = elements[2].text.split('\n')[0]
        symbol = elements[2].text.split('\n')[1] if len(
            elements[2].text.split('\n')) > 1 else ''
        price = elements[3].text
        change_1h = elements[4].text
        change_24h = elements[5].text
        change_168h = elements[6].text
        market_cap = elements[7].text
        volume_24 = elements[8].text
        circulating_supply = elements[9].text

        crypto_list.append([
            rank,
            name,
            symbol,
            price,
            change_1h,
            change_24h,
            change_168h,
            market_cap,
            volume_24,
            circulating_supply
        ])

today = datetime.now().date()

# Write to CSV file
with open(f'{today}_crypto_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "Name", "Symbol", "Price", "Change_1h", "Change_24h", "Change_168h",
                     "Market Cap", "Volume_24h", "Circulating Supply"])
    writer.writerows(crypto_list)

driver.quit()
