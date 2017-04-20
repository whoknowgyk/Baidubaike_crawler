# -*- coding:utf-8 -*-
"""
@author:gyk
@file:spider_main.py
@time:2017/4/18下午3:32
"""
from work import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count=1#记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)#将入口url加入url管理器
        while self.urls.has_new_url():#如果有待爬取的url
            try:
                new_url=self.urls.get_new_url()#取一个出来
                print 'craw %d : %s' %(count,new_url)
                html_cont=self.downloader.download(new_url)#下载对应的页面
                new_urls,new_data=self.parser.parse(new_url,html_cont)#下载好以后，进行页面的解析，得到新的url数据
                self.urls.add_new_urls(new_urls)#将新的url补进url管理器
                self.outputer.collect_data(new_data)#同时进行数据的收集

                if count==10:
                    break

                count=count+1
            except:
                print 'craw failed'

        self.outputer.output_html()#输出收集好的数据


#main函数
if __name__=="__main__":
    #设置入口url
    root_url="http://baike.baidu.com/item/Python"
    #root_url = "http://s.weibo.com/weibo/%25E8%2582%25A1%25E7%25A5%25A8?topnav=1&wvr=6&b=1"
    obj_spider=SpiderMain()
    #启动爬虫
    obj_spider.craw(root_url)