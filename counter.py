from bs4 import BeautifulSoup
from pygame import mixer
import requests
import time

mixer.init()

new_follow = mixer.music.load('new_follow.mp3')
lose_follow = mixer.music.load('lose_follow.mp3')

url = "https://www.tiktok.com/@fun_python_projects"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
}
soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")

while(1):
    original_followers = int(soup.select_one('[title="Followers"]').text)
    time.sleep(1)
    new_followers = int(soup.select_one('[title="Followers"]').text)
    if new_followers > original_followers:
        new_follow()
        print(new_followers)
    if new_followers < original_followers:
        lose_follow()
        print(new_followers)
    if new_followers == original_followers:
        pass
