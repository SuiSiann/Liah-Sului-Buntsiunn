import os
import re

# Theh 47*-499的文章
搜尋式 = re.compile('4[7-9]._')

清單 = [file for file in os.listdir('./詞彙分級文章') if 搜尋式.search(file)]

print(sorted(清單)) 