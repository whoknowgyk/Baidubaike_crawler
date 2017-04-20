# -*- coding:utf-8 -*-
"""
@author:gyk
@file:html_outputer.py
@time:2017/4/18下午3:34
"""

import xlwt

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        book = xlwt.Workbook(encoding='ascii')
        sheet=book.add_sheet('dede',cell_overwrite_ok='True')
        sheet.write(0, 0, 'url')
        sheet.write(0, 1, 'title')
        sheet.write(0, 2, 'summary')
        hang=1
        for data in self.datas:
            sheet.write(hang, 0, data['url'])
            sheet.write(hang, 1, data['title'])
            sheet.write(hang, 2, data['summary'])
            hang=hang+1
        book.save('/Users/apple/Desktop/output.xls')
        # fout = open('output.html','w')
        #
        # fout.write("<html>")
        # fout.write("<body>")
        # fout.write("<table>")
        #
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>%s</td>" % data['url'])
        #     fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
        #     fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
        #     fout.write("</tr>")
        #
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        #
        # fout.close()