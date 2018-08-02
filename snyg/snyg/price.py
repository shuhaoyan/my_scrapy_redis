import requests

# 'https://product.suning.com/0070091633/192456756.html'
# 'https://pas.suning.com/nspcsale_0_000000000160397461_000000000160397461_0070141595_190_020_0200101_226503_1000041_9041_10274____R9011558_2.0___.html'

# url = 'https://pas.suning.com/nspcsale_0_000000000160397461_000000000160397461_0070141595_190_020_0200101_226503_1000041_9041_10274____R9011558_2.0___.html?callback=pcData&_=1532960003701'
#       'https://pas.suning.com/nspcsale_0_000000000192456756_000000000192456756_0070091633_190_020_0200101_226503_1000041_9041_10274____R9000195_1.0___.html?callback=pcData&_=1532960937518'
#       'https://pas.suning.com/nspcsale_0_000000000135408592_000000000135408592_0070121210_190_020_0200101_226503_1000041_9041_10274_Z001___R9011195_8.0___.html?callback=pcData&_=1532959803637'

headers = {
'Accept':' */*',
'Accept-Encoding':' gzip, deflate, br',
'Accept-Language':' zh-CN,zh;q=0.9',
'Connection':' keep-alive',
'Cookie':' _snmc=1; _snsr=direct%7Cdirect%7C%7C%7C; _snstyxuid=7258E572A2421OL4; _snvd=1532956048471jrKIk3A7aQj; SN_CITY=190_020_1000041_9041_01_10274_2_0; cityId=9041; districtId=10274; _cp_dt=7c4787ee-2c23-4b6a-8459-f98b606e29f4-48613; authId=siD02F07FB1DFC1DEEFB8E7E9B94E5E878; secureToken=47E5C5B37805A0F324727327CC47FC41; _df_ud=47ee76d0-9444-4f6f-87b1-747f79dd79ee; smhst=135408592|0070121210a160397461|0070141595a103281921|0070121210; _snma=1%7C153295604836398348%7C1532956048363%7C1532959804579%7C1532959994205%7C14%7C1; _snmp=153295999412197978; _snmb=153295604836815011%7C1532959994242%7C1532959994209%7C14',
'Host':' pas.suning.com',
'Referer':' https://product.suning.com/0070141595/160397461.html',
'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

params = {
'callback':'showHotkeywords',
'_':'1532960121151',
}

data ={

}
requests.get('',headers=headers)



# debug日志输出
# [scrapy.core.scraper]DEBUG: Scraped from <200 https...2.html>{}
#  每次yield item ,debug日志[scrapy.core.scraper]输出:url来源，级item内容
# 2018-07-31 14:01:47 [scrapy.core.scraper] DEBUG: Scraped from <200 https://product.suning.com/0070067079/190035612.html>
# {'desc': None,
#  'href': '//product.suning.com/0070121210/101962778.html',
#  'price': 'prive price ',
#  'salesname': '天源图书专营店',
#  'title': '平凡的世界(共三部)\n'}

# [scrapy.core.engine]
# 2018-07-31 14:01:44 [scrapy.core.engine] INFO: Spider opened    ！！！！！！！！！！！！！！！！
# [scrapy.core.engine] #DEBUG: Crawled (200) <GET https://list.suning.com/1-264003-0.html> (referer从哪里url获得的这个链接）
# HTTP Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，
# 告诉服务器我是从哪个页面链接过来的，服务器基此可以获得一些信息用于处理。
# 2018-07-31 14:01:45 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://list.suning.com/1-264003-0.html> (referer: None)
# 2018-07-31 14:01:45 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://product.suning.com/0070121210/103281921.html> (referer: https://list.suning.com/1-264003-0.html)
# 2018-07-31 14:01:47 [scrapy.core.engine] INFO: Spider closed (finished)    ！！！！！！！！！！！！！！

# 1 引擎：Hi！Spider, 你要处理哪一个网站？
#
# 2 Spider：老大要我处理xxxx.com。
#
# 3 引擎：你把第一个需要处理的URL给我吧。
#
# 4 Spider：给你，第一个URL是xxxxxxx.com。
#
# 5 引擎：Hi！调度器，我这有request请求你帮我排序入队一下。
#
# 6 调度器：好的，正在处理你等一下。
#
# 7 引擎：Hi！调度器，把你处理好的request请求给我。
#
# 8 调度器：给你，这是我处理好的request
#
# 9 引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求
#
# 10 下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
#
# 11 引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给def parse()这个函数处理的）
#
# 12 Spider：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。
#
# 13 引擎：Hi ！管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。
#
# 14 管道``调度器：好的，现在就做！