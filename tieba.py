import os
import re
import urllib.error
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
COUNT = 1

downloadDirectory = "downloaded"

def get_url_list(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "html.parser")
    url_list=bsobj.find("table", {"class":"drl_list"}).findAll("a", href=re.compile("^(/home/main/)((?!:).)*$"))
    global  COUNT
    for url in url_list:
        url_image="http://tieba.baidu.com/"+url["href"]

        get_image(url_image,COUNT)

        COUNT += 1


def get_image(url_image,count):
    html=urlopen(url_image)
    bsobj=BeautifulSoup(html,"html.parser")
    if bsobj.find("body",{"class":"page404"}) :
        print("page404")
    else:
        imageLocation = bsobj.find("a", {"href": "javascript:;"}).find("img")["src"]
        filename=str(count)+".jpg"
        path=downloadDirectory+'/'+filename
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        urlretrieve(imageLocation,path)


for i in range(2):
    url="http://tieba.baidu.com/f/like/furank?kw=%B3%AF%CF%CA%D7%E5%D7%E3%C7%F2&pn=" + str(i + 1)
    get_url_list(url)