#! python
# coding:UTF-8
"""
脚本用来爬取信息安全漏洞门户网站的所有CVE漏洞信息，主要包括标识、提交时间、漏洞名称、漏洞代码利用。
为学习编程而写
v0.1版本
"""

import html.parser
import re
from html import unescape

import requests
from lxml import html


# typeLinks = []
# for i in range(1,34259):
#     typeLinks.append('http://cve.scap.org.cn/vulns/%s' % (str(i)))
# print(typeLinks) # 将typeLinks的内容赋值到 typeLinks = [] 中

# url = 'http://cve.scap.org.cn/vulns/1'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/88.0.4324.182 Safari/537.36'}
# response = requests.get(url, headers=headers)
# html_str = html.fromstring(response.text)

# res = re.findall(r"[\u4e00-\u9fa5]+",a)
# print(res)
# print(response.text)
# html_str = response.text
# print(html_str)

def log_list():
    for a in range(1, 11):
        # 定位标识，提取CVE字段
        logo_list_xpath = html_str.xpath(
            f'/html/body/div[1]/div[3]/div[1]/div/table/tbody/tr[{a}]/td[1]/a')  # 定位xpath标签 (获取指定位置的html)
        logo_list_convert = html.tostring(logo_list_xpath[0])  # 这里的logo_list_convert 取出的html 中文存在乱码，下面 unescape 进行转换
        logo_list_result = unescape(logo_list_convert.decode())  # logo_list_result 解析出来的html就可以使用正则表达式匹配需要的字符串
        # # print(str(logo_list_convert)[59:-53])
        # # print(logo_list_result[56:-49])
        logo = re.findall(r"([A-Z]{3}-\d{4}-\d*|[A-Z]{3}=\d{6})", logo_list_result)  # 使用正则表达式匹配出需要的字符串
        # print("漏洞标识:",logo)
        # print(logo_list_result)

        # 定位提取提交时间
        submission_time_xpath = html_str.xpath(f'/html/body/div[1]/div[3]/div[1]/div/table/tbody/tr[{a}]/td[2]')
        submission_time_convert = html.tostring(submission_time_xpath[0])
        submission_time_result = unescape(submission_time_convert.decode())
        # # print(submission_time_result[32:42])
        time = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", submission_time_result)
        # print('提交时间:',time)

        # 定位漏洞名称
        name_vulnerability_xpath = html_str.xpath(f'/html/body/div[1]/div[3]/div[1]/div/table/tbody/tr[{a}]/td[4]')
        name_vulnerability_convert = html.tostring(name_vulnerability_xpath[0])
        name_vulnerability_result = unescape(name_vulnerability_convert.decode())
        # rest = re.findall(r"([^<td>].*[\u4e00-\u9fa5]+)",Name_vulnerability_result)
        name = re.findall(r"([^<td>].*[<?])", name_vulnerability_result)
        # print('漏洞名称:',name)
        # print(Name_vulnerability_result)

        # 定位漏洞状态-漏洞利用代码
        status_vulnerability_xpath = html_str.xpath(
            f'/html/body/div[1]/div[3]/div[1]/div/table/tbody/tr[{a}]/td[5]/div/span[2]')
        status_vulnerability_convert = html.tostring(status_vulnerability_xpath[0])
        status_vulnerability_result = unescape(status_vulnerability_convert.decode())
        status = re.findall(r'[\u4e00-\u9fa5]+', status_vulnerability_result)
        # print('漏洞状态:',status)
        print("漏洞标识:%-19s" % logo, '提交时间:%-12s' % time, '漏洞名称:%-65s' % name, '漏洞状态:%-20s' % status)


for b in range(1, 3):
    try:
        url = f'http://cve.scap.org.cn/vulns/{b}'
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.190 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html_str = html.fromstring(response.text)
        # print(html_str)
        log_list()
    except Exception as s:
        print(end='')
