# coding=utf-8
from spiders import *
import sys
import datetime
from libs import merge_pdf
import os
import msvcrt


def download_paper(param):
    if param == 'all':
        print('-->开始下载最新一期报纸')
        get_fzrb()
        get_grrb()
        get_jfjb()
        get_kjrb()
        get_rmrb()
        get_xhmrdx()
        get_xxsb()
        get_zggfb()
        get_hqsb()
        print('-->下载结束！')
    else:
        eval('get_' + param)()


def merge_paper(paper_dir):
    today_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    sub_dirs = []
    for idx, val in enumerate(os.walk('./papers/'+today_str+os.sep)):
        if idx == 0:
            sub_dirs = val[1]

    for sub_dir in sub_dirs:
        pdf_dir = paper_dir + os.sep + 'papers' + os.sep+today_str + os.sep+sub_dir
        if sub_dir == '环球时报':
            print(pdf_dir)
            # merge_hq(pdf_dir)
            continue
        merge_pdf(pdf_dir)


if __name__ == '__main__':
    if 'python.exe' in sys.executable:
        currentdir = os.path.dirname(__file__)
    else:
        currentdir = os.path.dirname(sys.executable)
    # merge_paper(currentdir)
    # sys.exit()
    if len(sys.argv) > 2:
        print('最多只能有一个参数')
        sys.exit()
    param = sys.argv[1] if len(sys.argv) == 2 else 'all'
    if param not in [
        'all',
        'fzrb',
        'grrb',
        'jfjb',
        'kjrb',
        'rmrb',
        'xhmrdx',
        'xxsb',
        'zggfb'
    ]:
        print('%s不是正确的报纸名称拼音首字母' % param)
        sys.exit()
    download_paper(param)
    merge_paper(currentdir)
    print("程序执行完毕，按回车键退出！")
    while True:
        if ord(msvcrt.getch()) in [13, 100]:
            break
