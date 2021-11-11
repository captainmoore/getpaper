#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lipo
 
import tkinter as tk
import os

window = tk.Tk()
window.title('下载报纸-终南山下') 
window.geometry('400x160')
 
on_hit = False
def hit_me():
    global on_hit
    os.system("python ./spiders/xxsb.py")
    var.set('下载并合并完成')
    if on_hit == False:
        on_hit = True        
    else:
        on_hit = False
        
var = tk.StringVar()
var.set('点击下载')
b = tk.Button(window, textvariable=var, font=('simsun', 12), width=30, height=2, command=hit_me)
b.place(x=80, y=40)

window.mainloop()