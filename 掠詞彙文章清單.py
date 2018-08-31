#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.client import HTTPSConnection
import json
from urllib.parse import quote
import ssl
from os import makedirs
from os.path import exists

ssl.match_hostname = lambda cert, hostname: True


class Command:
    help = 'https://詞彙分級.意傳.台灣'
    domain = 'xn--kbr112a4oa73rtw5adwqr1d.xn--v0qr21b.xn--kpry57d'
    網址 = '/'

    公家內容 = {
        '來源': '詞彙分級',
        '種類': '語句',
    }

    def 全部清單(self, *args, **參數):
        全部文章 = self._全部清單()
        if not exists('詞彙分級文章'):
            makedirs('詞彙分級文章')
        
        with open('./long-thok-tshing-tuann.csv', 'w') as ff:
            for 一篇 in 全部文章:
                if 一篇['類別'] in ['朗讀','文學獎', '電子報']:
                    print('{},{},{},{}'.format(
                        一篇['id'], 一篇['類別'], 一篇['文章名'], 一篇['作者']
                    ), file=ff)

    def _全部清單(self):
        conn = HTTPSConnection(self.domain)
        conn.request("GET", quote(self.網址))
        r1 = conn.getresponse()
        if r1.status != 200:
            print('not 200')
            raise RuntimeError('連線錯誤：{}{}\n{} {}'.format(
                self.domain, self.網址, r1.status, r1.reason
            ))
        內容 = r1.read().decode()
#         print('內容', 內容)
        return json.loads(內容)['資料']


指令 = Command()
指令.全部清單()
