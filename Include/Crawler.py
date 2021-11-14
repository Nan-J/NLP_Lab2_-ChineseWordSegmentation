import requests
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        kv = {'user-agent': "Mozilla/5.0"}  # 修改头部信息，伪装成火狐访问
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()  # 如果状态不是200.则引发HTTPError异常
        r.encoding = r.apparent_encoding
        print("成功获取网页信息！")
        print("----------------")
        return r.text

    except:
        print("爬取失败!")
        print("----------------")
        return ""


def fillInList(html):
    print("开始解析网页信息")
    print("----------------")
    soup = BeautifulSoup(html, "html.parser")  # 得到一个BeautifulSoup的对象(标准的缩进格式)
    print("解析完成！")
    print("----------------")

    textList = []
    print("开始清洗数据！")
    print("----------------")

    ct_new = soup.select('div[class="wrap"]')
    for i in range(len(ct_new)):
        title = ct_new[i].select('h1[class="reportTitle"]')[0].get_text()
        author = ct_new[i].select('p[class="author"]')[0].get_text()
        time = ct_new[i].select('p[class="time"]')[0].get_text()
        abstract = ct_new[i].select('div[class="abstract"]')[0].get_text()
        main_text = ct_new[i].select('section[class="braft_output_content"]')[0].get_text()
        textList.append({"标题": title, "author": author, "时间": time,"摘要":abstract,"正文":main_text})

    print("成功完成文本爬取！")
    print("----------------")
    return textList


def storeInFiles(textList):
    print("开始写入文件！")
    print("----------------")
    num = 9
    file = open("..\\textLib\\text_test_" + str(num) + ".txt", "w", encoding="utf8")  # 文件命名
    for each in textList:
        file.write(str(each)) # 存入.txt文件
    file.close()
    print("成功写入文件！爬虫完成！")
    textList.clear()


if __name__ == "__main__":
    print("开始爬虫！")
    print("----------------")
    url1= "https://www.aminer.cn/research_report/614bd18530e6dd8ab7efeff7?download=undefined&from=likeRank"
    url2="https://www.aminer.cn/research_report/6160fb5e30e6dd8ab70c1978?download=undefined&from=likeRank"
    url3="https://www.aminer.cn/research_report/61615ac330e6dd8ab70c9231?download=false"
    url4="https://www.aminer.org/research_report/5d8472ddfd841a8ca264bf77?download=false"
    url5="https://www.aminer.org/research_report/5d808c15ed7dcc6932a1b7a5?download=false"
    url6="https://www.aminer.org/research_report/5d786d7fc70fbee87444bcef?download=false"
    url7="https://www.aminer.org/research_report/5d68cbae3671f8fad71aed0e?download=false"
    url8="https://www.aminer.org/research_report/5d6777973671f8fad71aecc1?download=false"
    url9="https://www.aminer.cn/research_report/5d7f4dece8efa3929d14b04e?download=false"
    html = getHtmlText(url9)  # 使用request库函数获取网页信息
    textList = fillInList(html)  # 使用BS4库函数进行页面解析
    storeInFiles(textList)
