from fake_useragent import UserAgent
import requests
import random
import time

s = requests.Session()


DP_PROXIES = [
    'ip:port',
    ...
]
TIMEOUT = 10


def choice_dp_proxy():
    if DP_PROXIES:
        return random.choice(DP_PROXIES)
    return ''


def get_user_agent():
    ua = UserAgent()
    return ua.random


def get_sofang_headers(version, url):
    if version == "列表页":
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Cookie": "global_cookie=aoiic9t0xkukjsj2ad34eauui20j1hhq1cp; Integrateactivity=notincludemc; lastscanpage=0; new_search_uid=13c35ccbd85befebf1e53d581b1d6201; recentViewlpNew_newhouse=3_1498133313_8013%5B%3A%7C%40%7C%3A%5D8a97de91b23c4f938ab9886ef0320238; newhouse_user_guid=8E675CDC-866F-EAEC-EADF-7FCDDE0A0BE8; vh_newhouse=3_1492153594_10140%5B%3A%7C%40%7C%3A%5D7b9789197db60f5ebe3e6e7e350422dc; city=sz; searchLabelN=3_1517305718_19758%5B%3A%7C%40%7C%3A%5Dc1c6502c7568adbfe304aa4034348043; searchConN=3_1517305718_20621%5B%3A%7C%40%7C%3A%5Db70fe8fd28420fb39d8be075b439b358; sf_source=; s=; __utmc=147393320; __utma=147393320.532264205.1492153594.1517379871.1517387570.169; __utmz=147393320.1517387570.169.44.utmcsr=newhouse.sz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/house/s/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; __utmb=147393320.10.10.1517387570; unique_cookie=U_2qyjhuk8aswft1k2q4989rt3j27jd2ospet*4",
            "Host": "newhouse.sz.fang.com",
            # "Referer": "https://wx.qq.com/",
            "Upgrade-Insecure-Requests": "1",
        }
    elif version == "首页":
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Cookie": "global_cookie=aoiic9t0xkukjsj2ad34eauui20j1hhq1cp; Integrateactivity=notincludemc; lastscanpage=0; new_search_uid=13c35ccbd85befebf1e53d581b1d6201; recentViewlpNew_newhouse=3_1498133313_8013%5B%3A%7C%40%7C%3A%5D8a97de91b23c4f938ab9886ef0320238; newhouse_user_guid=8E675CDC-866F-EAEC-EADF-7FCDDE0A0BE8; vh_newhouse=3_1492153594_10140%5B%3A%7C%40%7C%3A%5D7b9789197db60f5ebe3e6e7e350422dc; city=sz; searchLabelN=3_1517305718_19758%5B%3A%7C%40%7C%3A%5Dc1c6502c7568adbfe304aa4034348043; searchConN=3_1517305718_20621%5B%3A%7C%40%7C%3A%5Db70fe8fd28420fb39d8be075b439b358; sf_source=; s=; __utmc=147393320; __utma=147393320.532264205.1492153594.1517379871.1517387570.169; __utmz=147393320.1517387570.169.44.utmcsr=newhouse.sz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/house/s/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; Captcha=59482B546A54326C6351505765554859336A2B514D314C61644332424D626E2B7A7148637266797834616C42674737326B576E6F69334A6D422F433148792B5262474A4A716C2B4E4254343D; __utmb=147393320.20.10.1517387570; newhouse_chat_guid=CD8384BA-4039-61F5-E538-C45C39383A07; polling_imei=9e1d7ab94b5b6d06; unique_cookie=U_2qyjhuk8aswft1k2q4989rt3j27jd2ospet*6",
            "Host": url[7:].split("/")[0],
            # "Referer": "https://wx.qq.com/",
            "Upgrade-Insecure-Requests": "1",
        }
    elif version == "详情页":
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Cookie": "global_cookie=aoiic9t0xkukjsj2ad34eauui20j1hhq1cp; Integrateactivity=notincludemc; lastscanpage=0; new_search_uid=13c35ccbd85befebf1e53d581b1d6201; recentViewlpNew_newhouse=3_1498133313_8013%5B%3A%7C%40%7C%3A%5D8a97de91b23c4f938ab9886ef0320238; newhouse_user_guid=8E675CDC-866F-EAEC-EADF-7FCDDE0A0BE8; vh_newhouse=3_1492153594_10140%5B%3A%7C%40%7C%3A%5D7b9789197db60f5ebe3e6e7e350422dc; city=sz; searchLabelN=3_1517305718_19758%5B%3A%7C%40%7C%3A%5Dc1c6502c7568adbfe304aa4034348043; searchConN=3_1517305718_20621%5B%3A%7C%40%7C%3A%5Db70fe8fd28420fb39d8be075b439b358; sf_source=; s=; __utmc=147393320; __utma=147393320.532264205.1492153594.1517379871.1517387570.169; __utmz=147393320.1517387570.169.44.utmcsr=newhouse.sz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/house/s/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; newhouse_chat_guid=CD8384BA-4039-61F5-E538-C45C39383A07; polling_imei=9e1d7ab94b5b6d06; Captcha=4B665634476B504C30437342465A4F394E6A6C734F32526861507942724E466156383751742F66496244644E46533172384C47476D75486A74785770684A504748753830557A35514442493D; unique_cookie=U_2qyjhuk8aswft1k2q4989rt3j27jd2ospet*7; __utmb=147393320.30.10.1517387570",
            "Host": url[7:].split("/")[0],
            # "Referer": "https://wx.qq.com/",
            "Upgrade-Insecure-Requests": "1",
        }
    return headers


def fetch(url, retry=0, version="列表页"):
    if url:
        url = url.strip()
    if "http" not in url:
        return ""

    # 代理模式1
    choice_proxy_item = choice_dp_proxy()
    proxies = {
        'http': choice_proxy_item,
        'https': choice_proxy_item
    }
    # 代理模式2
    # from ..commons.common_params import proxy as proxies
    s.headers = get_sofang_headers(version=version, url=url)
    s.headers.update({'user-agent': get_user_agent()})
    try:
        res = s.get(url, timeout=TIMEOUT, proxies=proxies)

        if res.status_code != 200:
            print(res.status_code)
            raise Exception

        res.encoding = res.apparent_encoding
        return res

    except (requests.exceptions.RequestException,
            requests.exceptions.ProxyError) as e:
        if retry <= 3:
            print("休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1, version=version)
    except Exception as e:
        if e:
            print(e)
        if retry <= 3:
            print("着重休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1, version=version)
