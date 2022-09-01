import requests
import urllib3

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}
request_str = "https://www.doviz.com/"

def call():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page = requests.get(request_str, headers=headers, timeout=(20, 20), verify=False)
    return page.text
