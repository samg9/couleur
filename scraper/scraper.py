#from flask import flask
from urllib3 import PoolManager
import urllib
import re
import json
from time import sleep


BASE_URL = 'https://www.instagram.com/'
CURRENT_USER_URL = ''


def get_profile(username):
    user_url = BASE_URL+str(username)+'/'
    print('\n\n user url is:'+user_url)
    CURRENT_USER_URL = user_url
    scrape(CURRENT_USER_URL)
# scrape url


def save_pics_from_scrape(list_of_srcs):
    # for i in list_of_srcs:
    return False


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
    #     all_js.extend((re.findall(r'/<script type="text\/javascript">window\._sharedData = (.*)<\/script>/' ,stringy,re.IGNORECASE|re.DOTALL)) )
    #       extend((re.findall(r'<script type="text/javascript">window._sharedData = (.*);</script><script type="text/javascript">window.__initial' ,data,re.IGNORECASE|re.DOTALL))
    #extend((re.findall(r'<script type="text/javascript">window._sharedData = (.*);</script><script type="text/javascript">window.__initial' ,data,re.IGNORECASE|re.DOTALL)) )

    display_url_scrape.extend(
        (re.findall(r'"display_url":"(.*?)"', stringy, re.IGNORECASE | re.DOTALL)))
    print('diaply url scrape')
    print(display_url_scrape)

    js.extend((re.findall(r'<script type="text/javascript">window._sharedData = (.*);</script>\n<script type="text/javascript">window.__initialDataLoaded',
                          stringy, re.IGNORECASE | re.DOTALL)))
    print(js)
    print('lens again ', len(all_js), len(all_js[0]), ' , ', len(js))

    # f = open("eli_fur_dump.txt", "w")
    # f.write(stringy)
    # f.close()

    dict0 = json.loads(js[0])
    # ['graphql']['user']['edge_owner_to_timeline_media']['edges']
    list0 = dict0['entry_data']['ProfilePage']
    user_edges = list0[0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

    display_urls = []

    for edge in user_edges:
        display_urls.extend(str(edge['node']['display_url']))

    display_urls123 = [str(i['node']['display_url']) for i in user_edges]
    print('du1', display_urls)
    print('du2', display_urls123)

    pic_num = 0
    for i in display_urls123:
        print("\n\n ->:final link before grabbing the pic:", i)
        urllib.request.urlretrieve(i, f'pic{pic_num}.jpg')
        pic_num = pic_num+1
        if pic_num > 5:
            print('~~reached max pics~~~')
            quit()

    display_urls = []
    pic_num = 0
    # #pick out some js(hacky)
    # js_stuff= all_js[3]
    # print('\n\n### js_stuff len: ',len(js_stuff))
    # ##convert list to string
    # s=""
    # for i in js_stuff:
    #     s+=str(i)

    # stringy_js_stuff = []
    # stringy_js_stuff.extend((re.findall(r'{"src":"(.*?)"}',s,re.IGNORECASE|re.DOTALL)) )
    # print("stringy js stuff len",len(stringy_js_stuff))

    # stringy_js_stuff = []
    # stringy_js_stuff.extend((re.findall(r'{"src":"(.*?)"}',s,re.IGNORECASE|re.DOTALL)) )
    # print("stringy js stuff len",len(stringy_js_stuff))

    # iterate over each l4 item, ignore the first source link ( lowest resolution)
    # grab the second link
    # grab the pre generate photo information

    # final_links = []
    # final_words = []
    # for i in stringy_js_stuff:
    #     final_links.extend((re.findall(r'{"src":"(.*?)"',i ,re.IGNORECASE|re.DOTALL)) )
    #     i+='}'
    #     final_words.extend((re.findall(r'"Image may contain: (.*?)}',i,re.IGNORECASE|re.DOTALL)) )
    #     i = i[0:len(i)-1]

    # print("\n______final words: ", final_words,
    #       "   final links size: ", final_links)
    # print("\n\n all finals_links:", final_links)
    # pic_num = 0
    # for i in final_links:
    #     print("\n\n ->:final link before grabbing the pic:", i)
    #     urllib.request.urlretrieve(i, f'pic{pic_num}.jpg')
    #     pic_num = pic_num+1
    #     if pic_num > 5:
    #         print('~~reached max pics~~~')
    #         quit()

    print('~~~~~finnnnn~~~~~~~')
    '''
    list0.extend((re.findall(r'<script type="text/javascript">(.*?)<' ,stringy,re.IGNORECASE|re.DOTALL)) )
    js_stuff= list0[3]
    s=""
    for i in js_stuff: 
        s+=str(i)


    l4.extend((re.findall(r'{"src":"(.*?)"}',ss,re.IGNORECASE|re.DOTALL)) )
    ### iterate over each l4 item, ignore the first source link ( lowest resolution)
    ### grab the second link 
    ### grab the pre generate photo information

    final_links = [] 
    final_words = [] 
    for i in l4:
        f=[]
        final_links.extend((re.findall(r'{"src":"(.*?)"}',i ,re.IGNORECASE|re.DOTALL)) )
        i+='}'
        final_words.extend((re.findall(r'"Image may contain: (.*?)}',last,re.IGNORECASE|re.DOTALL)) )
        i = i[0:len(i)-1]



    links_list = [] 
    list_links.extend((re.findall(r'"display_url":"(.*?)"',ss,re.IGNORECASE|re.DOTALL)) ) #getting blocked with 403s

    urllib.request.urlretrieve(i, f'pic{i}_{i}.jpg')

    ### clear caches for next request handling
    final_links = [] 
    final_words = []


'''
