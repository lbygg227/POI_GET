import json    #导入JSON库
import sys      #导入系统库
import requests  #导入requests库，
ty=sys.getfilesystemencoding()  #这个可以获取文件系统的编码形式
import time     #设置时间
import socket
import numpy as np
ak='tDM947ZCUIZXzs7ohNHsz77QkU22WzDa'#百度开发者平台的KEY
timeout=20



arr=np.zeros((19,29,2))
for lon in range(0,19):
    for lat in range(0,29):
        arr[lon][lat]=[31.234796+lat*(0.09867764285714285/2),118.350532+lon*(0.099678555555555/2)]
#对经纬度进行网格划分，分为18（经）*28（纬）的网格
        
urls=[]#所有网格
urls_NJ=[]
urls1=[]#南京市网格


name='公交车站'#爬取要素关键字
#tag='交通设施'#爬取要素类型

for lat in range(0,18):
#for lat in range(0,lat_num):
    for lng in range(0,28):
    #for lng in range(0,lng_num):
        
        page_num=0
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&bounds='+str((arr[lat][lng][0]))+','+str((arr[lat][lng][1]))+','+str((arr[lat+1][lng+1][0]))+','+str((arr[lat+1][lon+1][1]))+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        socket.setdefaulttimeout(timeout)
        html=requests.get(url)  #获取网页
        data=html.json()    #网页为JSON数据格式，获取数据
        if data['results']!=None:   #判断是否含有数据
            for item in data['results']:
                if item['city']=='南京市':     #筛选出属于南京市范围的网格
                    urls_NJ.append([lat,lng])   #将南京市网格重新添加到一个矩阵中
                    break
                else:
                    break
                break

print('南京市网格划分完成')
for a in urls_NJ:
    lat=a[0]
    lng=a[1]
    for b in range(0,20):
        page_num=str(b)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&bounds='+str((arr[lat][lng][0]))+','+str((arr[lat][lng][1]))+','+str((arr[lat+1][lng+1][0]))+','+str((arr[lat+1][lng+1][1]))+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls1.append(url)   #获取网页，并存储再列表中


f=open(r'D:\南京市'+name+'.txt','a',encoding='utf-8')#设置存储文件的路径和名称
print ('url列表读取完成')

def getdata(url):   #该函数用于获取数据，并写入txt文件
    try:
        socket.setdefaulttimeout(timeout)#防止被误判恶意攻击
        html=requests.get(url)
        data=html.json()
        if data['results']!=None:
            for item in data['results']:
                    jname=item['name']#获取名称
                    jlat=item['location']['lat']#获取经度
                    jlon=item['location']['lng']#获取纬度
                    jarea=item['area']#获取行政区
                    jadd=item['address']#获取具体地址
                    j_str=jname+','+str(jlat)+','+str(jlon)+','+jarea+','+jadd+','+'\n'
                    #将上述数据整理为一条字符串
                    f.write(j_str)#将字符串写入txt文件
            print (time.time())
        time.sleep(1)#设置时间间隔一秒，防止被误判为恶意攻击
    except:
        getdata(url)
        
for url in urls1:#对每一个网页进行爬取
    getdata(url)
f.close()#关闭文件
print (name+'完成') 
