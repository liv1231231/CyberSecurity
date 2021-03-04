import requests
from bs4 import BeautifulSoup
import hashlib

url = "http://46.101.84.10:32078"
r = requests.session()
get = r.get(url)
scrapedstring = get.text

soup = BeautifulSoup(scrapedstring)
target = soup.select('h3')[0].text

hashedstring = hashlib.md5(target.encode('utf-8')).hexdigest()
post = r.post(url=url,data = {'hash' : hashedstring})
print(post.text)




