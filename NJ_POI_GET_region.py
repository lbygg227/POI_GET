import json
import sys
import requests  #导入requests库，
ty=sys.getfilesystemencoding()  #这个可以获取文件系统的编码形式
import time
import socket
timeout=20

ak='tDM947ZCUIZXzs7ohNHsz77QkU22WzDa'

names=['充电桩']
tag='交通设施'

print (time.time())  
print ('开始')
urls=[] #声明一个数组列表

for name in names:
    for i in range(0,20):
        page_num=str(i)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市建邺区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市秦淮区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市江宁区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市雨花台区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市高淳区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市玄武区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市栖霞区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市鼓楼区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市浦口区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak 
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市六合区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
        urls.append(url)
        url='http://api.map.baidu.com/place/v2/search?query='+name+'&tag='+tag+'&region=南京市溧水区'+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak 
        urls.append(url)
   

    f=open(r'D:\南京市'+name+'.txt','a',encoding='utf-8')

    print ('url列表读取完成')

    def getdata(url):
        try:
            socket.setdefaulttimeout(timeout)
            html=requests.get(url)
            data=html.json()
            if data['results']!=None:
                for item in data['results']:
                        jname=item['name']
                        jlat=item['location']['lat']
                        jlon=item['location']['lng']
                        jarea=item['area']
                        jadd=item['address']
                        j_str=jname+','+str(jlat)+','+str(jlon)+','+jarea+','+jadd+','+'\n'
                        f.write(j_str)
                print (time.time())
            time.sleep(2)
        except:
            getdata(url)
    for url in urls:
        getdata(url)
    f.close()
    print (name+'完成')  
