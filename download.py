from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time ,sys

# APIキーの情報

key = "0d8aa3b8ca842f013662282ae2e716ee"
secret = "8524c72b8c6e68e2"
wait_time = 1.5

# 保存フォルダーの指定
animalname = sys.argv[1]   #argument value(パラメーターの値)
savedir = "./" + animalname 

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
    