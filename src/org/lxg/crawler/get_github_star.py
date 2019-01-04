# -*- coding:utf-8 -*-
__author__ = "MuT6 Sch01aR"

import requests
from pyquery import PyQuery

def GetGitHub(n):
    url = "https://github.com/trending/python"
    r = requests.get(url)
    for i in PyQuery(r.content)(".repo-list>li"):
        repo_url = "https://github.com"+PyQuery(i).find(".mb-1 a").attr("href")
        name = PyQuery(i).find(".mb-1 a").text()
        star = PyQuery(i).find("a.mr-3").text()
        if int(star.replace(" ","").replace("  ","").replace(",","")) > n:
            print("项目："+name,"星星数："+star,"项目地址："+repo_url)

if __name__ == '__main__':
    GetGitHub(10000)