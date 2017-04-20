# -*- coding:utf-8 -*-
"""
@author:gyk
@file:html_parser.py
@time:2017/4/18下午3:33
"""
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        #将结果传到一个列表里面
        new_urls=set()
        #/view/123.htm  /view/\d+\.htm
        #匹配正则表达式
        links = soup.find_all('a',href=re.compile(r"/item/*?"))
        for link in links:
            new_url = link['href']
            #urljoin可以自动将两个url拼接成对应的完整的url
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    #解析数据，需要解析title和summary两个数据
    def _get_new_data(self, page_url, soup):
        #建立一个字典来存放数据
        res_data = {}

        res_data['url']=page_url

        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary"> </div>
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data