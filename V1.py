

import requests
import urllib
from lxml import etree
import re


userInput = input('请输入您要下载的URL').replace(' ','')

Ruhtml = requests.get(userInput)

html = etree.HTML(Ruhtml.text)

def callbackfunc(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100

    print("已经下载{}%".format(int(percent)))


objs = html.xpath("//script[last()]")





download_link = re.search(r"/static/file/pod/[a-zA-Z0-9]+.mp3" , objs[2].text)
download_link_text = 'http://yuedu.fm{}'.format(download_link.group())


mp3_name = re.search(r"听.+（ @悦读FM ）" , objs[1].text)



urllib.request.urlretrieve\
    (download_link_text, "{}.mp3".format(mp3_name.group()[1:-9]),callbackfunc)





