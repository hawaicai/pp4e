"""
用python实现一个HTTP Web服务器，它知道如何运行服务器端CGI脚本；
从当前工作目录提供文件和脚本；python脚本必须存储在 webdir\cig-bin或webdir\htbin中；
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'    # 存放HTML文件和cig-bin脚本文件夹的所作
port= 808        # 缺省http://localhost/,也可以使用http://localhost:xxx/

os.chdir(webdir)
srvraddr = ("", port)
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()

