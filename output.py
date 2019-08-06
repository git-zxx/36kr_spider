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

'''
    【GitChat】   1分钟了解互联网大事
2019年7月17日  星期三
—————————     

【热点消息】   

 ◆微信上线“一物一码”功能，每个商品都是品牌小程序“入口”

通过一物一码，商家即使没有渠道也可高效与消费者发生关联。微信表示希望借此，为品牌商家提供更完善的商品管理能力和更多样化的营销触点。未来，“一物一码”还将在零售更多领域发挥作用，帮助商家更深入地挖掘和触达消费者。

 ◆ 快手上调2019年商业化营收目标：在原先的百亿基础上增50%
 
快手商业副总裁表示，此举是为了冲刺3亿DAU的目标。这意味着快手商业已全面加速进入“战斗”模式，将专注于品牌去中心化、私域流量价值和社交资产沉淀。

【资讯】   

1.微信浮窗新增支持文件等形态，最多同时设置5个浮窗

2. 虾米音乐与MQA公司达成国内首家合作，将提供MQA音质音源

3.瑞幸咖啡宣布全国门店破3000家，今年目标4500家

【文章推荐】

程序员跳槽时，如何正确做好职业规划？

详情请戳：http://t.cn/AiWe45ij
「GitChat 下午茶🍭」
2019年7月17日  星期三

#硬核脑洞预测5G到底如何改变社会#

本系列要讲如下主题：
1 WIFI的没落
2 本地存储变得鸡肋
3 纽扣革命
4 远程混合现实技术
5 物联网操作系统
6 隐私进一步消失
7 金融行业的迎来史上最长的黄金发展期
每次通信的迭代升级，都会在终端连接密度、数据延迟、网速、资费出现明显的参数改变。1G~5G在性能上的数量级变化

点击阅读全文：https://36kr.com/p/5226053


「GitChat 晚间精选」

AI图像识别：人类看的是形状，算法看的是纹理

是猫还是大象？人类与AI意见不同。图片中的动物轮廓是猫，但是猫披着大象皮肤纹理，将图片交给人识别，人会说是猫，如果给计算机视觉算法处理，它会说是大象。德国研究人员认为：人看的是形状，计算机看的是纹理。这一发现相当有趣，但它证明计算机算法离人类视觉还有很远距离。

全文戳链接阅读：https://36kr.com/p/5225703

--------------------------------

文章来源 36氪



'''


