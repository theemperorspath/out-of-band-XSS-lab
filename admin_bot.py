import threading
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

CHROME_PATH = "/usr/bin/chromium"
DRIVER_PATH = "/usr/bin/chromedriver"
TARGET = "http://127.0.0.1:5000"

# Custom admin cookie
ADMIN_SESSION = "ADMIN-" + str(int(time.time()))


def run_bot():
    print("[ADMIN BOT] Starting admin bot...")

    options = Options()
    options.binary_location = CHROME_PATH
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    # Set realistic admin cookie
    driver.get(TARGET)
    driver.add_cookie({
        "name": "sessionid",
        "value": ADMIN_SESSION,
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "sameSite": "Lax"
    })
    print(f"[ADMIN BOT] Injected admin cookie sessionid={ADMIN_SESSION}")

    seen = set()

    while True:
        try:
            stored = requests.get(f"{TARGET}/admin/pending").json()

            for idx, raw_payload in enumerate(stored):
                if idx not in seen:
                    url = f"{TARGET}/admin/review/{idx}"
                    print(f"[ADMIN BOT] Visiting {url}")
                    driver.get(url)
                    seen.add(idx)

            time.sleep(2)

        except Exception as e:
            print("[ADMIN BOT] Error:", e)
            time.sleep(5)

    driver.quit()


def start_bot_thread():
    t = threading.Thread(target=run_bot, daemon=True)
    t.start()
