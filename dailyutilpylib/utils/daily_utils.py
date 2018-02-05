from ..gis.coord_exchange import bd09togcj02, gcj02towgs84, wgs84togcj02, bd09towgs84
from django.contrib.gis.geos import Polygon, MultiPolygon, Point, GEOSGeometry
from math import radians, cos, sin, asin, sqrt
from collections import OrderedDict
import time
import datetime
import json
import socket
import struct


##########################################################################
#                            打印函数运行时间
##########################################################################
def timeit(func):
    """
    装饰器：打印时间
    :param func: 
    :return: 
    """
    def funca(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("Func {} costs {}s".format(func.__name__, (end - start)))
        return ret

    return funca


##########################################################################
#                            字符串转化为日期格式
##########################################################################
def parse_date(date_str):
    try:
        if not date_str:
            return None
        if "-" in date_str:
            if date_str.count("-") == 1:
                date = datetime.datetime.strptime(date_str, "%Y-%m")
            elif date_str.count("-") == 2:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        elif "年" in date_str:
            if "日" in date_str:
                date = datetime.datetime.strptime(date_str, "%Y年%m月%d日")
            elif "月" in date_str:
                date = datetime.datetime.strptime(date_str, "%Y年%m月")
            else:
                date = datetime.datetime.strptime(date_str, "%Y年")
        elif date_str.isdigit():
            if len(date_str) == 4:
                date = datetime.datetime.strptime(date_str, "%Y")
            elif len(date_str) > 6:
                date = datetime.datetime.strptime(date_str, "%Y%m%d")
            else:
                date = datetime.datetime.strptime(date_str, "%Y%m")
        else:
            date = None
    except:
        return None
    return date


##########################################################################
#                            小数转化成百分比
##########################################################################
def make_percent(s):
    """
    小数转化成百分比
    :param s: 
    :return: 
    """
    if not s:
        return "0"
    if s and s != "-":
        return str(round(float(s) * 100, 2))
    if float(s) == 0:
        return str(s)


##########################################################################
#                            计算两点间距离
##########################################################################
def haversine(lon1, lat1, lon2, lat2, default="GCJ02"):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    origin: https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
    """
    if default == "WGS84":
        pass
    elif default == "GCJ02":
        lon1, lat1 = gcj02towgs84(lon1, lat1)
        lon2, lat2 = gcj02towgs84(lon2, lat2)
        pass
    elif default == "BD09":
        lon1, lat1 = bd09towgs84(lon1, lat1)
        lon2, lat2 = bd09towgs84(lon2, lat2)
    else:
        pass
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


##########################################################################
#                            随机混淆数字
##########################################################################
def make_random(s):
    import random
    try:
        s = float(s)
    except:
        return s
    if isinstance(s, int) or isinstance(s, float):
        r = random.randint(1, 2)
        r_use = random.random()
        while r_use > 0.3:
            r_use = r_use / 2
        while r_use < 0.1:
            r_use = r_use * 2
        if r == 1:
            s = s * (1 + r_use)
        else:
            s = s * (1 - r_use)
    return s


def make_fixed_mix(s):
    try:
        s = float(s)
    except:
        return s
    if isinstance(s, int) or isinstance(s, float):
        if s > 1000:
            s = s * 1.1
        else:
            s = s * 0.9
        s = round(s, 4)
    return s


##########################################################################
#                            Request获取ip
##########################################################################
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


##########################################################################
#                            ip转换成整数及反转
##########################################################################
def ip2int(addr):
    if not addr or not isinstance(addr, str):
        return None
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    if not addr or not isinstance(addr, int):
        return None
    return socket.inet_ntoa(struct.pack("!I", addr))


##########################################################################
#                            字符串相似度
##########################################################################
def LevenshteinDistance(s, t):
    '''字符串相似度算法（Levenshtein Distance算法）
    一个字符串可以通过增加一个字符，删除一个字符，替换一个字符得到另外一个
    字符串，假设，我们把从字符串A转换成字符串B，前面3种操作所执行的最少
    次数称为AB相似度
    这算法是由俄国科学家Levenshtein提出的。
    Step Description
    1 Set n to be the length of s.
    Set m to be the length of t.
    If n = 0, return m and exit.
    If m = 0, return n and exit.
    Construct a matrix containing 0..m rows and 0..n columns.
    2 Initialize the first row to 0..n.
    Initialize the first column to 0..m.
    3 Examine each character of s (i from 1 to n).
    4 Examine each character of t (j from 1 to m).
    5 If s[i] equals t[j], the cost is 0.
    If s[i] doesn't equal t[j], the cost is 1.
    6 Set cell d[i,j] of the matrix equal to the minimum of:
    a. The cell immediately above plus 1: d[i-1,j] + 1.
    b. The cell immediately to the left plus 1: d[i,j-1] + 1.
    c. The cell diagonally above and to the left plus the cost:
       d[i-1,j-1] + cost.
    7 After the iteration steps (3, 4, 5, 6) are complete, the distance is
    found in cell d[n,m]. '''

    m, n = len(s), len(t)
    if not (m and n):
        return m or n

    # 构造矩阵
    matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
    matrix[0] = list(range(n + 1))
    for i in range(m + 1):
        matrix[i][0] = i

    for i in range(m):
        for j in range(n):
            cost = int(s[i] != t[j])
            # 因为 Python 的字符索引从 0 开始
            matrix[i + 1][j + 1] = min(
                matrix[i][j + 1] + 1,  # a.
                matrix[i + 1][j] + 1,  # b.
                matrix[i][j] + cost  # c.
            )

    return matrix[m][n]


##########################################################################
#                          wgs84多边形转换成gcj02
##########################################################################
def make_multipolygon_to_front(multipolygon_obj):
    # 这个boundary是multipolygon的属性
    # multipolygon = multipolygon_obj.boundary.coords
    # multipolygon = json.loads(multipolygon_obj.geojson)["coordinates"]
    multipolygon = multipolygon_obj.coords
    try:
        result = [[list(wgs84togcj02(*list(location))) for location in list(polygon)] for polygon in list(multipolygon)]
    except Exception as e:
        result = [
            [
                [
                    list(wgs84togcj02(*list(l))) for l in location
                ] for location in list(polygon)
            ] for polygon in list(multipolygon)
        ]
    return result


##########################################################################
#                          gcj02多边形转换成wgs84
##########################################################################
def make_multipolygon_to_wgs84(multipolygon_li):
    """
    该多边形列表结构为：多边形(高德)(格式:[[[x, x], [x, x], [x, x]...], [多边形2], [多边形3] ...])
    :param multipolygon_li: 
    :return: 
    """
    try:
        result = [[wgs84togcj02(*list(location)) for location in list(polygon)] for polygon in multipolygon_li]
    except Exception as e:
        result = "该多边形格式不正确"
    return result


##########################################################################
#                          gcj02单个多边形转换成wgs84
##########################################################################
def make_polygon_wgs84(polyline):
    """
    gcj02单个多边形转换成wgs84
    :param polyline: 多边形(高德)--[[x, x], [x, x], [x, x]...]
    :return: 
    """
    # if isinstance(polyline, str):
    #     polyline = eval(polyline)
    if polyline[-1] != polyline[0]:
        polyline.append(polyline[0])
    polyline_wgs84 = [tuple(gcj02towgs84(float(li[0]), float(li[1]))) for li in polyline]
    polygon_wgs84 = Polygon(tuple(polyline_wgs84))
    return polygon_wgs84


##########################################################################
#                             单例模式装饰器
##########################################################################
def singleton(cls):
    """
    装饰器：单例模式
    :param cls: 
    :return: 
    """
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


##########################################################################
#                                 平均数
##########################################################################
def avg(li, standrad):
    """
    求平均数
    :param li: [list] 列表 
    :param standrad: [int] 保留小数位数 
    :return: 
    """
    if li:
        try:
            li = [float(l) for l in li]
            return round(sum(li) / len(li), standrad)
        except:
            pass
    return 0


##########################################################################
#                              生成有序字典
##########################################################################
def make_order_dict(di, li):
    """
    生成有序字典
    :param di: 原字典
    :param li: 有序字典的顺序(字典的key的列表)
    :return: 
    """
    new_di = OrderedDict()
    for key in li:
        new_di[key] = di[key]
    return new_di


##########################################################################
#                               列表计数
##########################################################################
def li_count_dict(li, di):
    """
    形如[{"a": 1, "b": 2, "c": 3, ...}, {}, {}, ...]的列表计数
    即该list中的所有dict里包含{"a": 1}的数量为count
    :param li: 
    :param di: 
    :return: 
    """
    count = 0
    for l in li:
        repeat = 0
        for k, v in di.items():
            if l[k] != v:
                repeat = 1
                break
        if repeat == 0:
            count += 1
    return count
