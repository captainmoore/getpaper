# coding = UTF-8
import os
import requests
import time
import sys
import bs4
from PyPDF2 import PdfFileWriter, PdfFileReader
import datetime
from urllib import request
# import easyocr


def fun(blocknum, blocksize, totalsize):
    """
    blocknum:当前的块编号
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    """
    percent = blocknum*blocksize/totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent*100
    print("\rDownloading:%s%.2f%%" % ('>'*int(percent/2), percent), end='')


def downfile(url, path):
    if os.path.exists(path):
        print('文件：%s 已存在' % path)
        return
    request.urlretrieve(url, path, fun)

# 进度条模块


def downwithbar(url, path, name=''):
    if not os.path.exists(path):   # 看是否有该文件夹，没有则创建文件夹
        os.mkdir(path)
    if name:
        filepath = path + name + '.pdf'
    else:
        filepath = path + os.path.basename(url)  # 设置文件存储路径
    if os.path.exists(filepath):
        print('文件：%s 已存在' % filepath)
        return
    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True)
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    if 'content-length' in response.headers:
        content_size = int(response.headers['content-length'])  # 下载文件总大小
    else:
        print('非标准格式文件，下载进度可能存在偏差')
        content_size = 1000000

    try:
        if response.status_code == 200:  # 判断是否响应成功
            print('[文件大小]:{size:.2f} MB'.format(
                size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
        with open(filepath, 'wb') as file:  # 显示进度条
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*40 /
                                                        content_size), float(size / content_size * 100)), end=' ')
        end = time.time()  # 下载结束时间
        print('下载完成,耗时: %.2f秒' % (end - start))  # 输出下载用时时间
    except:
        print('Error!')


def getSoup(url, coding='utf-8'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    res = requests.get(url, headers=headers)
    res.encoding = coding
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    return soup


def merge_pdf(pdf_dir):
    print('-->开始合并')
    today_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    pdfs = []
    for file in os.listdir(pdf_dir):
        if file.endswith('.pdf'):
            pdfs.append(pdf_dir + '\\' + file)
            pdfs.sort(key=str.lower)

    pdfWriter = PdfFileWriter()

    for file in pdfs:
        pdfFileObj = open(file, 'rb')
        try:
            pdfReader = PdfFileReader(pdfFileObj)
        except Exception as e:
            print(e, '--', file)
        else:
            for pageNum in range(0, pdfReader.numPages):
                # print(pageNum)
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

    pdf_path = pdf_dir + today_str + '.pdf'
    pdfOutput = open(pdf_path, 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    print(pdf_path)


def img_ocr(img_path):
    print(img_path)
    # img_path='D:\code\getpaper\papers\\20210516\\temp\\01.jpg'
    img_path = img_path.replace('环球时报\\', '')
    reader = easyocr.Reader(['ch_sim', 'en'])
    res = reader.readtext(img_path)
    return res


def main():
    url = ''
    path = ''  # 设置下载到本地的地址
    print("No Auth!")


if __name__ == '__main__':
    main()
