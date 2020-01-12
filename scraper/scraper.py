from urllib3 import PoolManager
import urllib
import requests
from io import BytesIO
import re
import json
import flask
from PIL import Image, ImageDraw
from webcolors import rgb_to_hex
import io
import base64
from time import sleep
from public import images


BASE_URL = 'https://www.instagram.com/'
CURRENT_USER_URL = ''


# Delete this function
def get_byte_image(images_list):
    all_encodings = []
    for i in images_list:
        img = Image.open(i, mode='r')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        encoded_img = base64.encodebytes(
            img_byte_arr.getvalue()).decode('ascii')
        all_encodings.append(encoded_img)
    print("len of encodings", len(all_encodings))
    return all_encodings


'''
generate palette function
tdo
'''


def get_palette_colors(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    small_image = image.resize((80, 80))
    # image with only 10 dominating colors
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=5)
    result.putalpha(0)
    colors = result.getcolors(80*80)      # array of colors in the image
    hexes = [rgb_to_hex(color[1][:3]) for color in colors]
    return hexes


def get_profile(username):
    user_url = BASE_URL+str(username)+'/'
    print('\n\n user url is:'+user_url)
    CURRENT_USER_URL = user_url
    # res = scrape(CURRENT_USER_URL)
    return scrape(CURRENT_USER_URL)


def scrape(link):
    print('\n\n# in scrape meothd.... about to scrape:', link)

    http = PoolManager()
    print("\n\n## about to make GET req.")
    response = http.request('GET', link)
    stringy = response.data.decode("utf-8")
    print("lens: ", len(stringy))
    all_js = []
    js = []

    display_url_scrape = []
    # grab all js from decoded html
    all_js.extend((re.findall(
        r'<script type="text/javascript">window._sharedData = {(.*?)}', stringy, re.IGNORECASE | re.DOTALL)))

    display_url_scrape.extend(
        (re.findall(r'"display_url":"(.*?)"', stringy, re.IGNORECASE | re.DOTALL)))
    print('diaply url scrape')
    print(display_url_scrape)

    js.extend((re.findall(r'<script type="text/javascript">window._sharedData = (.*);</script>\n<script type="text/javascript">window.__initialDataLoaded',
                          stringy, re.IGNORECASE | re.DOTALL)))

    dict0 = json.loads(js[0])
    list0 = dict0['entry_data']['ProfilePage']
    user_edges = list0[0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
    display_urls123 = [str(i['node']['display_url']) for i in user_edges]

    #print('du2', display_urls123)

    response_array = []
    for url in display_urls123:
        pic_details_json = {
            "url": url,
            "hexes": get_palette_colors(url)
        }
        response_array.append(pic_details_json)

    return response_array
