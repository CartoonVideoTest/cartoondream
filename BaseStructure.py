import requests
from bs4 import BeautifulSoup
from DrissionPage import SessionPage


def get_search_result(cartoon_name):
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        ,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        ,"cache-control":"max-age=0"
    }
    response = requests.get(f"https://www.agedm.org/search?query={cartoon_name}",headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select('div.video_cover_wrapper>a')
    detail_list = []

    for url_detail in results:
        url = url_detail.get('href')
        title = url_detail.get('title')
        picture = url_detail.find('img').get('data-original')

        detail_list.append(url)
        detail_list.append(title)
        detail_list.append(picture)

    return detail_list

def skip_get_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        ,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        , "cache-control": "max-age=0"
    }
    response=requests.get(url,headers)
    soup=BeautifulSoup(response.text,"html.parser")
    jishu=soup.select("div.show.active>ul.video_detail_episode>li>a")
    jishu_list_url=[]

    for i in jishu:
        jishu_list_url.append(i.get('href'))

    jishu=len(jishu_list_url)
    return jishu,jishu_list_url

def get_video_url(url):
    page = SessionPage()
    # 访问网页
    page.get(url)
    # 在页面中查找元素
    item = page.ele('#iframeForVideo')
    return item.link
