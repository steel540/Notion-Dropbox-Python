# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:41:42 2023

@author: User
"""

import dropbox
import os

def get_file_path(file_name):
    # 找出要上傳的檔案的目錄
    path = os.path.dirname(__file__)
    file_path = '{}/{}'.format(path, file_name)
    return file_path

def upload_file(access_token, upload_file, file_to):
    # 設定好dropbox
    dbx = dropbox.Dropbox(access_token)
    # 打開要上傳的檔案
    with open(upload_file, 'rb') as f:
        # 把檔案上傳，如果有同名檔案的話就overwrite他
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print('done.')

def get_shared_link(access_token, file_to):
    # 設定好dropbox
    dbx = dropbox.Dropbox(access_token)
    # 獲得檔案分享連結
    shared_link = dbx.sharing_create_shared_link(file_to)
    print('獲得分享連結：', shared_link.url)
    return shared_link

if __name__ == '__main__':
    # 這裡填入剛剛在dropbox產生的token
    dropbox_token = 'sl.Bd4vQXXXXXXXXXXX...........'
    
    # 這裡可以指定你要上傳的資料名稱，我這裡假設是Test.pdf
    uploadfile = 'slas382a.pdf'
    
    # 取得要上傳的檔案路徑
    file_from = get_file_path(uploadfile)
    print('印出file_from:{}'.format(file_from))
    
    # 這裡是你要上傳到dropbox的指定路徑
    file_to = '/test_file/{file_name}'.format(file_name=uploadfile)
    print('印出要上傳的路徑{}'.format(file_to))
    
    # 上傳檔案
    upload_file(dropbox_token, file_from, file_to)
    
    # 獲得分享連結
    getlink = get_shared_link(dropbox_token, file_to)
