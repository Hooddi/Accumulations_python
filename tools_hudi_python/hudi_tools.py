# -*- coding: utf-8 -*-
'''
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2019/4/2 13:03
@ file        : hudi_tools.py
@ description : 
'''
def file_back():
    '''备份文件夹'''
    import os, shutil, datetime
    path = os.getcwd()
    file_name = path.split('\\')[-1]  # 文件夹名称
    dt = datetime.datetime.now().strftime('%m%d%H%M')
    new_file_name = 'back' + dt + '_' + file_name
    path_list = path.split('\\')
    path_list[-1] = new_file_name
    new_path = '\\'.join(path_list)  # 备份文件所在文件夹
    shutil.copytree(path, new_path, True)  # 完成文件备份





