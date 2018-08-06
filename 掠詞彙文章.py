from http.client import HTTPSConnection
import json
from urllib.parse import quote
import ssl

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
        匯入數量 = 0
        for 一篇 in self._全部資料():
            for 一逝 in 一篇['文章資料']:
                print('一逝', 一逝)

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
        print('內容', 內容)
        return json.loads(內容)['資料']
    
    
    
指令 = Command()
指令.全部資料()
