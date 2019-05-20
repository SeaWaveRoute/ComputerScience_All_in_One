import requests
from bs4 import BeautifulSoup

URL = "https://www.fastcampus.co.kr/online_category/"

response = requests.get(url=URL)  # 해당 url에 요청을 보냄
soup = BeautifulSoup(response.text, "html.parser")  # 해당 페이지의 text를 parse함
get_all_course = soup.find_all("div", {"class": "mk-text-block"})



# get_all_course = soup.find("div", {"class": "wpb_row vc_row mk_fullwidth-true attched-alse vc_row0fliid js-master-row mk-in-viewport"})
# get_all_course = soup.find_all("div", {"class": "mk-grid"})
# 전체 강의목록 class명이지만 띄어쓰기 떄문인지 find가 되지않음. 아래가 좀더 작은 박스 그런데 mk-grid라는 게 너무 많음

def parsing_class(elements):
    subject = elements.find("h1", {"class": "subject"}) # 강의명
    descrip = elements.find("p", {"class": "descrip"})  # 강의 설명
    info = elements.find("p", {"class": "info"})  # 강의 세부 설명
    day = elements.find("p", {"class": "day"})  # class명은 day라고 되어있지만 해시태그명이 되어있음
    url = elements.find("a")  # 강의 상세 페이지 url
    print("강의명 : {}".format(subject))
    print("강의설명 : {}".format(descrip))
    print("강의 세부 설명 : {}".format(info))
    print("강의 날짜 : {}".format(day))
    print("강의 url : {}".format(url))
    print("\n")
    print("-" * 100)


for i in get_all_course:
    parsing_class(i)
