import time

stations = [
    # {"name": "嘉定新城", "url": "https://sh.lianjia.com/ershoufang/xuxing/,https://sh.lianjia.com/ershoufang/juyuanxinqu/,https://sh.lianjia.com/ershoufang/jiadinglaocheng/,https://sh.lianjia.com/ershoufang/xinchenglu1/,https://sh.lianjia.com/ershoufang/jiadingxincheng/,https://sh.lianjia.com/ershoufang/malu/"},
    # {"name": "青浦新城", "url": "https://sh.lianjia.com/ershoufang/xianghuaqiao/,https://sh.lianjia.com/ershoufang/yingpu/,https://sh.lianjia.com/ershoufang/zhaoxiang/,https://sh.lianjia.com/ershoufang/xiayang/"},
    # {"name": "松江新城", "url": "https://sh.lianjia.com/ershoufang/songjiangdaxuecheng/,https://sh.lianjia.com/ershoufang/songjiangxincheng/,https://sh.lianjia.com/ershoufang/songjianglaocheng/,https://sh.lianjia.com/ershoufang/xinqiao/"},
    # {"name": "松江新城",
    #  "url": "https://sh.lianjia.com/ershoufang/songjianglaocheng/"},
    # {"name": "松江新城",
     # "url": "https://sh.lianjia.com/ershoufang/xinqiao/"},
    # {"name": "松江新城",
     # "url": "https://sh.lianjia.com/ershoufang/songjiangdaxuecheng/"},
    # {"name": "奉贤新城", "url": "https://sh.lianjia.com/ershoufang/nanqiao/,https://sh.lianjia.com/ershoufang/fengxianjinhui/"},
    # {"name": "南汇新城", "url": "https://sh.lianjia.com/ershoufang/lingangxincheng/"},
]

# 定义一组 User-Agent
user_agents = [
    # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    # 'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    # 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20210101 Firefox/4.0.1',
    # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    # 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    # 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20210101 Firefox/4.0.1',
   ]

import requests
# 导入数据解析模块
import parsel  # CSS解析
import re  # 正则解析
import csv  # 保存数据
import random


def second_url_visit(url_path):
    headers = {
        'User-Agent': '',
    }
    response = requests.get(url=url_path, headers=headers)
    html_data = response.text
    selector = parsel.Selector(html_data)

    # 1. 基本属性
    base_divs = selector.css('.base')
    info_key = base_divs.css('.content li .label::text').getall()
    info_b = base_divs.css('.content li::text').getall()
    info_bb = [x.strip(" ") for x in info_b]
    info_value = [item.strip() for item in info_bb if item.strip()]
    """.......
    """

    # 2. 交易属性
    transaction_divs = selector.css('.transaction')
    
    # 3. 房源特色
    """......
    """
    result = {**info_result, **trans_result, **special_result}



def is_south_north_facing(orientation):
    # 定义需要的方向
    required_directions = ['南', '东南', '西南']

    # 检查是否包含任何需要的方向
    if any(direction in orientation for direction in required_directions):
        return 1
    else:
        return 0

# Python循环示例
for station in stations:
    name = station.get("name", "N/A")
    '''......'''
        if response and response.status_code == 200:
            try:
                print(f"站名: {name}, URL: {url}")
                print(f"************************正在爬取{name}附近的房源信息,结果写入{name}二手房.csv文件中***********************")
                time.sleep(5)
                # 创建文件对象
                f = open(f"{name}二手房.csv", mode='a', encoding='utf-8', newline='')
                fieldnames_all = ['标题', '小区', '区域', '总价', '单价', '年份', '一级地址', '二级地址',
                                  '户型介绍', '装修描述', '售房详情', '房屋户型',
                                  '所在楼层', '建筑面积', '户型结构', '套内面积',
                                  '建筑类型', '房屋朝向', '朝向value', '建筑结构', '装修情况',
                                  '梯户比例', '配备电梯', '楼层高度', '挂牌时间',
                                  '房屋用途', '房屋年限', '房本备件', '房源核验码',
                                  '核心卖点', '小区介绍', '适宜人群', '周边配套',
                                  '税费解析', '交通出行']
                """......."""

                        csv_writer = csv.DictWriter(f, fieldnames=fieldnames_all)
                        csv_writer.writeheader()
                        csv_writer.writerow(filtered_dict)
            except Exception as e:
                total_page_value = f"Error: {e}"

        else:
            time.sleep(10)