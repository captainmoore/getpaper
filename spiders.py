# coding = UTF-8
import requests
import bs4
import os
from urllib.parse import urljoin
from urllib.parse import quote
from urllib.parse import urlparse
import re
from urllib.request import urlopen
from lxml import etree
from datetime import datetime
import sys
import os
import time
import json
import random
from libs import downwithbar, getSoup, downfile, img_ocr
# from PIL import Image

# 法制日报


def get_fzrb():
    paper_name = '法制日报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)
    url = 'http://epaper.legaldaily.com.cn/fzrb/content/PaperIndex.htm'
    soup = getSoup(url)

    real_url = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url)
    soup = getSoup(url)
    url_page1 = urljoin(url, re.findall(
        'URL=(.*?)"', str(soup.select('meta')[3]))[0])
    soup = getSoup(url_page1)

    # 各版面pdf地址列表
    layout_pdf_trs = soup.select(
        'body>table>tr:nth-of-type(2)>td:nth-of-type(1)>table>tr:nth-of-type(1)>td:nth-of-type(2)>table:nth-of-type(3) tr')

    for tr in layout_pdf_trs:
        print('-'*50)
        a = tr.select('tr td:nth-of-type(3) a')[0].attrs['href']
        pdf_url = urljoin(url, a)
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 工人日报


def get_grrb():
    paper_name = '工人日报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)

    paper_api_home = 'http://i.workercn.cn/paper'
    paper_date = json.loads(requests.get(
        paper_api_home+'/grrb/index.json?t='+str(random.random())).text)['index']
    dates = str.split(paper_date, '-')
    paperUrl = paper_api_home + "/" + "grrb" + "/" + \
        dates[0] + "/" + dates[1] + "/" + dates[2] + ".json"
    paper_data = json.loads(requests.get(paperUrl).text)

    for i in range(1, len(paper_data['pages'])+1):
        pdf_url = paper_data['paperHomeUrl'] + "/" + \
            str(i) + "/grrb" + dates[0] + dates[1] + dates[2] + str(i) + ".pdf"
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 解放军报


def get_jfjb():
    paper_name = '解放军报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)

    url = 'http://www.81.cn:80/jfjbmap/paperindex.htm'

    soup = getSoup(url)
    real_url = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url)
    soup = getSoup(url)

    layouts = soup.select('#APP-SectionNav li a')
    for layout in layouts:
        layout_url = urljoin(url, layout.attrs['href'])
        layout_soup = getSoup(layout_url)
        pdf_url_temp = layout_soup.select('#APP-Pdf')[0].attrs['href']
        pdf_url = urljoin(layout_url, pdf_url_temp)
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 科技日报


def get_kjrb():
    paper_name = '科技日报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)
    url = 'http://digitalpaper.stdaily.com/'

    soup = getSoup(url)
    url_1 = urljoin(url, re.findall(
        'URL=(.*?)"', str(soup.select('meta')[3]))[0])
    soup = getSoup(url_1)
    url_2 = urljoin(url_1, re.findall(
        'URL=(.*?)"', str(soup.select('meta')[3]))[0])
    soup = getSoup(url_2)

    layouts = soup.select('div.bmname a')

    for layout in layouts:
        layout_url = urljoin(url_2, layout.attrs['href'])
        layout_soup = getSoup(layout_url)
        a = layout_soup.select('.pdf a')[0].attrs['href']
        pdf_url = urljoin(layout_url, a)
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 人民日报


def get_rmrb():
    paper_name = '人民日报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)

    url = 'http://paper.people.com.cn/rmrb/paperindex.htm'
    soup = getSoup(url)
    real_url = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url)
    soup = getSoup(url)

    layouts = soup.select('#pageLink')
    for layout in layouts:
        time.sleep(1)
        layout_url = urljoin(url, layout.attrs['href'])
        layout_soup = getSoup(layout_url)

        pdf_url_temp = layout_soup.select('.paper-bot .btn a')[0].attrs['href']
        pdf_url = urljoin(layout_url, pdf_url_temp)
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 新华每日电讯


def get_xhmrdx():
    paper_name = '新华每日电讯'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)

    url = 'http://mrdx.cn/content/PaperIndex.htm'
    soup = getSoup(url)
    real_url = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url)
    soup = getSoup(url)
    real_url_2 = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url_2)
    soup = getSoup(url)

    layouts = soup.select('.pdf')
    for layout in layouts:
        pdf_url = urljoin(url, layout.attrs['href'])
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 学习时报


def get_xxsb():
    paper_name = '学习时报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)
    url = 'http://paper.cntheory.com'

    soup = getSoup(url)
    url_1 = urljoin(url, re.findall(
        'URL=(.*?)"', str(soup.select('meta')[3]))[0])
    soup = getSoup(url_1)
    layouts = soup.select('.right_title-pdf a')

    for i in range(len(layouts)):
        layout_url = urljoin(url_1, layouts[i].attrs['href'])
        pdf_url = layout_url
        print(paper_name + ' - ' + pdf_url)
        i = i + 1
        downwithbar(pdf_url, paper_dir, str(i) if i > 9 else '0'+str(i))
        print('-'*50)

# 中国国防报


def get_zggfb():
    paper_name = '中国国防报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)
    url = 'http://www.81.cn:80/gfbmap/paperindex.htm'

    soup = getSoup(url)
    real_url = re.findall('URL=(.*?)"', str(soup.select('meta')[3]))[0]
    url = urljoin(url, real_url)
    soup = getSoup(url)

    layouts = soup.select('#APP-SectionNav li a')
    for layout in layouts:
        layout_url = urljoin(url, layout.attrs['href'])
        layout_soup = getSoup(layout_url)
        pdf_url_temp = layout_soup.select('#APP-Pdf')[0].attrs['href']
        pdf_url = urljoin(layout_url, pdf_url_temp)
        print(paper_name + ' - ' + pdf_url)
        downwithbar(pdf_url, paper_dir)
        print('-'*50)

# 环球时报


def get_hqsb():
    paper_name = '环球时报'
    today_str = datetime.strftime(datetime.now(), '%Y%m%d')
    paper_dir = os.path.dirname(__file__) + os.sep + \
        'papers' + os.sep + today_str+'/'+paper_name+'/'
    os.makedirs(paper_dir, exist_ok=True)
    url = 'http://www.jdqu.com/bklist-10.html'
    soup = getSoup(url, coding='GBK')
    href = soup.select('.img-wrap a')[1].attrs['href']
    print(href)
    paper_url = urljoin(url, quote(href))
    print(paper_url)
    # sys.exit()
    paper_url_soup = getSoup(paper_url, coding='GBK')
    unpublished = re.findall(
        r'<font color="red" size="6">页面正在发布，请稍后，精彩即将呈现</font>', str(paper_url_soup))
    if len(unpublished) > 0:
        print('--> 今天的环球时报和参考消息还未更新')
    else:
        paper_num = 1
        download_pic(paper_url, paper_dir, str(paper_num)
                     if paper_num > 9 else '0' + str(paper_num))


# def merge_hq(pdf_dir):
#     temp_dir = os.path.join(pdf_dir, 'temp')
#     os.makedirs(temp_dir, exist_ok=True)
#     for root, dirs, files in os.walk(pdf_dir):
#         for file in files:
#             file_path = os.path.join(pdf_dir, file)
#             im = Image.open(file_path)
#             # 裁剪出报头，并进行文字识别，判断报纸的名称
#             region = im.crop((0, 0, 832, 263))
#             region.save(os.path.join(temp_dir, file))
#     for root, dirs, files in os.walk(temp_dir):
#         print(root)
#         for file in files:
#             file_path = os.path.join(root, file)
#             print(file_path)
#             txts = img_ocr(file_path)
#             print(txts)

#     return pdf_dir


def download_pic(url, paper_dir, name=''):
    soup = getSoup(url, coding='GBK')
    href = soup.select('img#demo')[0].attrs['src']
    # paper_pic_url = urljoin(url, href)
    paper_pic_url = urljoin(href, quote(urlparse(href).path))
    print(paper_pic_url)
    # sys.exit()

    if name:
        pic_name = name
        downfile(paper_pic_url, paper_dir + pic_name + '.jpg')
    else:
        downfile(paper_pic_url, paper_dir + os.path.basename(paper_pic_url))

    next_page = re.findall(
        r'<a href="([\d-]*?)\.html">下一页</a>', str(soup.select('.paging')[0]))
    print(next_page)
    if next_page:
        next_url = urljoin(url, next_page[0]+".html")
        paper_num = int(pic_name) + 1
        download_pic(next_url, paper_dir, str(paper_num)
                     if paper_num > 9 else '0' + str(paper_num))


if __name__ == '__main__':
    print('spiders')
