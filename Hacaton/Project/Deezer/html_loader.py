import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def load_html(url, length=1, timeout=10):
    """Get html page, after loading necessary data."""
    logging.info('Preparing.')

    options = Options()
    options.add_argument("--headless")

    logging.info('Start driver.')
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    logging.info('Start loading page.')

    started = time.time()
    browser.get(url)
    html = browser.page_source
    while len(html) < length:
        time.sleep(0.5)
        html = browser.page_source
        if time.time() - started > timeout:
            logging.warning('Waiting time exceeded. Check normal len.')
            break
    browser.close()
    logging.info(f'Page loaded. Loaded symbols: {len(html)}. Elapsed time: {round(time.time() - started, 2)} sec.')
    return html