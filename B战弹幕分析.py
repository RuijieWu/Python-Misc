'''
Author: JeRyWu 1365840492@qq.com
Date: 2023-01-10 18:52:35
LastEditors: JeRyWu 1365840492@qq.com
LastEditTime: 2023-01-16 23:06:54
FilePath: \Python-Misc\B战弹幕分析.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#Easy Python Script To Anaylysis Bilibili
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyecharts
import jieba
import json

urlList = [
               
]
wordslist = {
    
}
#Input
while True : 
    print("input quit to stop")
    url = input("Input URL :") 
    if url == "quit" or "Quit":
        print("Done")
        break
    elif url not in urlList :
        urlList.append(url)

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

#Download Approach
def Download(url) :
    response = requests.get(url, headers=headers)
    with open(f"./{datetime.date.today()}.txt") as f :
        f.write(response.text)

#Get Cid XML
def GetXmlByURL(url) :
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    content_all = soup.find_all("div")
    for content in content_all :
        if type(content) != None :
            for li in content.find_all("li") :
                if type(li) != None :
                    if li.attrs["cid"] != None :
                            cid = soup.find("cid=(.*?)&aid=")
                            xmlUrl = f"https://comment.bilibili.com/{cid}.xml"
                            return xmlUrl

def GetXmlByBV(bv) :
    url = f"https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp"
    res = requests.get(url)
    cid = json.loads(res.text)["data"][0]["cid"]
    xmlUrl = f"https://comment.bilibili.com/{cid}.xml"
    return xmlUrl
                        
#Analysis
def Deal (words):
    words = jieba.lcut(words)
    for word in words :
        if word not in wordslist.keys() :
            wordslist[word] = 1
        else :
            wordslist[word] += 1
    
#ShowData
#做成词云图(jieba+pyechars)or报表（Pandas）
#def Show(void)                             