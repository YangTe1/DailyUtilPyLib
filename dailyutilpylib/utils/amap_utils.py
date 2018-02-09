from commons.common_params import AMAP_AK
from utils.http_utils import simple_fetch
import json


##########################################################################
#                              高德地图匹配经纬度
##########################################################################
def fetch_places_suggested_amap(query, city, show=False, prompt=False):
    url = "http://restapi.amap.com/v3/place/text?key={amap_ak}&keywords={keyword}&types=&city={city_name}&" \
          "children=1&offset=20&page=1&extensions=all".format(amap_ak=AMAP_AK, keyword=query, city_name=city)
    js = json.loads(simple_fetch(url).text)
    if js["status"] == "0":
        return False
    res = js['pois']
    if len(res) > 0:
        for i, item in enumerate(res):
            item["name"] = item["name"] if "name" in item else "ERROR"
            item["adname"] = item["adname"] if "adname" in item else "ERROR"
            item["cityname"] = item["cityname"] if "cityname" in item else "ERROR"
            item["location"] = item["location"] if "location" in item else 0
            item["id"] = item["id"] if "id" in item else 0
            if show:
                formated_string = "{0} : {1} | {2} - {3} : {4} ".format(
                    i,
                    item["id"] if "id" in item else "ERROR",
                    item["name"] if "name" in item else "ERROR",
                    item["adname"] if "adname" in item else "ERROR",
                    item["cityname"] if "cityname" in item else "ERROR",
                    item["location"] if "location" in item else 0,
                    item["id"] if "id" in item else 0
                )
                print(formated_string)

        while prompt:
            print("")
            print("----------------------")
            print("")
            option = input("请输入数字进行确认(输入n退出): >> ")
            if option == "n":
                option = -1
                break
            elif option == "":
                option = 0
            try:
                option = int(option)
            except Exception as e:
                print("只能输入数字!")
                continue
            print("")
            print("----------------------")
            print("")
            item = res[option]
            return item["name"], item["cityname"], item["adname"], item["location"], item["id"]
        else:
            item = res[0]
            return item["name"], item["cityname"], item["adname"], item["location"], item["id"]
    return False
