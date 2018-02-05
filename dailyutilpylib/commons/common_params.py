##################################################################################
#                                代理服务器
##################################################################################
# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = ".."
proxyPass = ".."

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxy = {
    "http": proxyMeta,
    "https": proxyMeta,
}


##################################################################################
#                                 高德key
##################################################################################
AMAP_AK = "d077b34a617acd69a62dfdc34d24b0df"
