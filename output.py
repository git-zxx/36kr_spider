import datetime
all_news = []
date = ''
f_urls = ['~/文档/news_data/晚间精选', '~/文档/news_data/下午茶', '~/文档/news_data/大事件']
end = '.txt'


class Output(object):

    def get_time(self):
        global date
        y = datetime.datetime.now().strftime('%Y')
        m = datetime.datetime.now().strftime('%m')
        d = datetime.datetime.now().strftime('%d')
        today = ''
        weekday = datetime.datetime.now().strftime('%w')
        if weekday == '0':
            today = '星期日'
        elif weekday == '1':
            today = '星期一'
        elif weekday == '2':
            today = '星期二'
        elif weekday == '3':
            today = '星期三'
        elif weekday == '4':
            today = '星期四'
        elif weekday == '5':
            today = '星期五'
        elif weekday == '6':
            today = '星期六'

        date = str(y)+'年'+str(m)+'月'+str(d)+'日 ' + today

    def collect_data(self, all_):
        global all_news
        all_news = all_

    def afternoon_tea(self, txt_num):
        f = open(f_urls[1] + str(txt_num+1) + end, 'w', encoding='utf-8')
        f.write("「GitChat 下午茶🍭」\n")
        f.write(date)
        f.write('\n\n#' + all_news[txt_num]['title']+'#')
        f.write("\n\n" + all_news[txt_num]['overview'])
        f.write("\n\n全文戳链接阅读："+all_news[txt_num]['link'])
        f.write("\n\n———————————\n文章来源：36氪")
        f.close()

    def evening_featured(self, txt_num):  # txx_num用于新建不同名字的同类推送文本,参数值来自parser模块
        txt_num += 5
        f = open(f_urls[0] + str(txt_num-4) + end, 'w', encoding='utf-8')
        f.write("「GitChat 晚间精选」\n")
        f.write(date)
        f.write('\n\n' + all_news[txt_num]['title'])
        f.write("\n\n" + all_news[txt_num]['overview'])
        f.write("\n\n全文戳链接阅读："+all_news[txt_num]['link'])
        f.write("\n\n———————————\n\n文章来源：36氪")
        f.close()

'''
    def one_min_news(self):
        txt_num = 10
        f = open(f_urls[2] + end, 'w', encoding='utf-8')
        f.write("【GitChat】   1分钟了解互联网大事\n")
        f.write(date+'\n———————————')
        f.write('\n\n【热点消息】')
        f.write('\n\n◆' + all_news[txt_num]['title'] + "\n\n" + all_news[txt_num]['overview'])
        f.write("\n\n◆" + all_news[txt_num + 1]['title'] + '\n\n'+all_news[txt_num + 1]['overview'])
        f.write("\n\n【资讯】")
        f.write("\n\n1." + all_news[txt_num + 2]['title'])
        f.write("\n\n2." + all_news[txt_num + 3]['title'])
        f.write("\n\n3." + all_news[txt_num + 4]['title'])
        f.write("\n\n【文章推荐】")
        f.write('\n\n\n详情请戳：')
        f.close()

'''



