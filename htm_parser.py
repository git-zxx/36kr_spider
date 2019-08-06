from bs4 import BeautifulSoup
from news_parser import output
import requests
urls = [
    "https://36kr.com/information/web_news",  # 最新
    "https://36kr.com/information/technology",  # 科技
    "https://36kr.com/information/happy_life",  # 生活
    "https://36kr.com/information/innovate",  # 创新
]
all_news = []
LINK_HEAD = "https://36kr.com"
"""
    模块功能：
    1.下载html文档
    1.解析htm文档，获取每项新闻标题及链接
    3.返回列表，列表内为每项新闻【标题、概述、链接】
    4.列表格式[
                {'title_':'文章1标题'，'overview':'文章1概述', 'link':'http://}
                {'title_':'文章2标题'，'overview':'文章2概述', 'link':'http://}
                                                .
                                                .
                                                .
                ]
"""


class HtmParser(object):

    out_ = output.Output()

    def parse(self, url):
        global all_news
        all_article_link = []
        res = requests.get(url)
        # res.encoding = res.apparent_encoding
        htm_doc = res.text
        soup = BeautifulSoup(htm_doc, 'html.parser')
        # <div class="information-flow-item"># 获取文章列表
        # <a class="article-item-title weight-bold" >最前线 | 飞聊、多闪各有风波，张一鸣的社交之路坎坷</a> # 获取标题
        # 获取连接方法：<a class="article-item-pic" href="/p/5226380"> # 获取文章链接
        # 进入链接格式：https://36kr.com/p/5226456
        items = soup.find_all('div', class_="information-flow-item")
        for item in items:
            link = LINK_HEAD+item.find('a', class_="article-item-pic")['href']
            title = item.find('a', class_="article-item-title weight-bold").text
            all_news.append({"title": title, 'link': link})
            all_article_link.append(link)
        print(all_article_link)

        for i in range(10):
            res = requests.get(all_news[i]['link'])
            # res.encoding = res.apparent_encoding
            news_txt = res.text
            # <div class="common-width content articleDetailContent kr-rich-text-wrapper">  获取段落区域
            # <div class="common-width margin-bottom-20">
            # <div class="article-left-container">
            news_soup = BeautifulSoup(news_txt, 'html.parser')
            overview_data = news_soup.find('div', class_="articleDetailContent")
            all_p = overview_data.find_all('p')
            txt_data = {"overview": all_p[1].text+"\n"+all_p[2].text}
            print('\n新闻【%d】[' % (i+1) + all_news[i]['title']+']\n' + txt_data['overview'] + '\n' + '——'*50)
            all_news[i].update(txt_data)


if __name__ == "__main__":
    obj = HtmParser()
    print('''
    可选抓取模块类别：
    1.最新
    2.生活
    3.科技
    4.创新
    ''')
    user_choose = input('   输入序号(回车确认)：')
    while user_choose not in ['1', '2', '3', '4']:
        user_choose = input('输入序号：')
    obj.parse(urls[int(user_choose)-1])
    out = output.Output()
    out.get_time()
    out.collect_data(all_news)

    for i in range(5):
        out.afternoon_tea(i)
        out.evening_featured(i)
    # out.one_min_news()
