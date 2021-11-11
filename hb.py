# coding = UTF-8
from libs import merge_pdf
import datetime
import os
import sys
import msvcrt

def merge_paper(paper_dir):
    today_str = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')
    sub_dirs = []
    for idx, val in enumerate(os.walk('./papers/'+today_str+'/')):
        if idx == 0:
            sub_dirs = val[1]

    for sub_dir in sub_dirs:
        pdf_dir = paper_dir + os.sep + 'papers/'+today_str+'/'+sub_dir
        if sub_dir == '环球时报':
            continue
        merge_pdf(pdf_dir)

if __name__ == '__main__':
    if 'python.exe' in sys.executable:
        currentdir = os.path.dirname(__file__)
    else:
        currentdir = os.path.dirname(sys.executable)
    merge_paper(currentdir)
    print("程序执行完毕，按回车键退出！")
    while True:
        if ord(msvcrt.getch()) in [13,100]:
            break