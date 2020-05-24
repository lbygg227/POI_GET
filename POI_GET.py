import json    #导入JSON库
import sys      #导入系统库
import requests  #导入requests库，
ty=sys.getfilesystemencoding()  #这个可以获取文件系统的编码形式
import time     #设置时间
import socket
import numpy as np
timeout=20

ak='tDM947ZCUIZXzs7ohNHsz77QkU22WzDa'

def getdata(url):
    try:
        socket.setdefaulttimeout(timeout)
        html=requests.get(url)
        data=html.json()
        if data['results']!=None:
            for item in data['results']:
                    jname=item['name']#获取名称
                    jlat=item['location']['lat']#获取经纬度
                    jlon=item['location']['lng']
                    jarea=item['area']#获取行政区
                    jadd=item['address']#获取具体地址
                    j_str=jname+','+str(jlat)+','+str(jlon)+','+jarea+','+jadd+','+'\n'
                    f.write(j_str)
        #time.sleep(1)
    except:
        getdata(url)

def method_region():
    print("请输入所需要爬取数据的行政区划名称，如南京市，南京市鼓楼区等")
    city=str(input())
      
    print ('开始')
    urls=[] #声明一个数组列表
    for i in range(0,20):
        page_num=str(i)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&region='+city+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
    print ('url列表读取完成')
   
    for url in urls:
        getdata(url)
        print('爬取中，请耐心等待')
    f.close()
    print ('完成，文件位于D盘目录下，请查看')
    
def method_bounds():
    print("请输入所选取地图矩形区域范围的左下角经度")
    lat_l=float(input())
    print("请输入所选取地图矩形区域范围的左下角纬度")
    lng_l=float(input())
    print("请输入所选取地图矩形区域范围的右上角经度")
    lat_r=float(input())
    print("请输入所选取地图矩形区域范围的右上角纬度")
    lng_r=float(input())
    a=(lat_l>=lat_r or lng_l>=lng_r)
    while a:
        print('经纬度输入错误,请重新输入')
        print("请输入所选取地图矩形区域范围的左下角经度")
        lat_l=float(input())
        print("请输入所选取地图矩形区域范围的左下角纬度")
        lng_l=float(input())
        print("请输入所选取地图矩形区域范围的右上角经度")
        lat_r=float(input())
        print("请输入所选取地图矩形区域范围的右上角纬度")
        lng_r=float(input())
        a=(lat_l>lat_r or lng_l>lng_r)
    
    lng_c=lng_r-lng_l
    lat_c=lat_r-lat_l

    lng_num=int(lng_c/0.1)+1
    lat_num=int(lat_c/0.1)+1

    arr=np.zeros((lat_num+1,lng_num+1,2))
    for lat in range(0,lat_num+1):
        for lng in range(0,lng_num+1):
            arr[lat][lng]=[lng_l+lng*0.1,lat_l+lat*0.1]

    urls=[]

    print('开始')
    for lat in range(0,lat_num):
        for lng in range(0,lng_num):    
            for b in range(0,20):
                page_num=str(b)
                url='http://api.map.baidu.com/place/v2/search?query='+name+'&bounds='+str((arr[lat][lng][0]))+','+str((arr[lat][lng][1]))+','+str((arr[lat+1][lng+1][0]))+','+str((arr[lat+1][lng+1][1]))+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
                urls.append(url)
    print ('url列表读取完成')
    
    for url in urls:
        getdata(url)
        print('爬取中，请耐心等待')
    f.close()
    print ('完成，文件位于D盘目录下，请查看')
                


def choose_method():
    print("选择爬取方法，1，行政区范围爬取，2，经纬度矩形范围爬取，输入序号")
    ch=input()
    if ch=='1':
        method_region()
    elif ch=='2':
        method_bounds()
    else:
        print('序号错误，请重新输入')
        choose_method()
        
print("请输入所需要爬取的POI要素名称，如电影院等")
name=input()
f=open(r'D:\POI-'+name+'.txt','a',encoding='utf-8')#存储文件
choose_method()
print('10秒后程序自动关闭')
time.sleep(10)


 
