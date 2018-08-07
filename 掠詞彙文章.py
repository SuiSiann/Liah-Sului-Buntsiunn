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
    網址 = '/匯出資料庫'

    公家內容 = {
        '來源': '詞彙分級',
        '種類': '語句',
    }

    def 全部資料(self, *args, **參數):
        全部文章 = self._全部資料()
        if not exists('詞彙分級文章'):
            makedirs('詞彙分級文章')
        for 一篇 in 全部文章:
            檔案名 = '詞彙分級文章/{:03}_{}.txt'.format(
                一篇['id'], 一篇['文章名'])
            file = open(檔案名, "w")

            file.write('{} {}\n\n'.format(一篇['id'], 一篇['文章名']))
            臺羅 = 一篇['臺羅'].split('\n')
            漢字 = 一篇['漢字'].split('\n')
            for id, 一逝漢字 in enumerate(漢字):
                file.write(一逝漢字)
                file.write('\n')
                file.write(臺羅[id])
                file.write('\n\n')
            file.close()

    def _全部資料(self):
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
指令.全部資料()
