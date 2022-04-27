# 下载并存储必应每日壁纸到指定位置

import time
import os
import urllib.request
import requests
import datetime

valid_mkt = ['ar-XA', 'bg-BG', 'cs-CZ', 'da-DK', 'de-AT',
    'de-CH', 'de-DE', 'el-GR', 'en-AU', 'en-CA', 'en-GB', 'en-ID',
    'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-PH', 'en-SG', 'en-US',
    'en-XA', 'en-ZA', 'es-AR', 'es-CL', 'es-ES', 'es-MX', 'es-US',
    'es-XL', 'et-EE', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR',
    'he-IL', 'hr-HR', 'hu-HU', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT',
    'lv-LV', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT',
    'ro-RO', 'ru-RU', 'sk-SK', 'sl-SL', 'sv-SE', 'th-TH', 'tr-TR',
    'uk-UA', 'zh-CN', 'zh-HK', 'zh-TW']

valid_mkt = [mkt.upper() for mkt in valid_mkt]

def bing_wallpaper_downloader( dirname, market, resolution = "1920x1080", ):
    #检查market 合法性
    market = market.upper()
    if market not in valid_mkt:
        print("不存在的地区参数，请检查输入变量", '\n')
    else:
        try:
        # 得到图片文件的网址
            #bing的地址
            raw_img_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
            #添加地区参数
            mkt_suffix = "&mkt=" + market 
            raw_img_url = raw_img_url + mkt_suffix
            #获取数据
            response = requests.get(raw_img_url)    
            result = response.json()
            #提取并得到图片地址
            url_prefix ="https://cn.bing.com"
            img_url = url_prefix + result["images"][0]["url"]
            #获取当前日期


        except Exception as e:
            print('错误: 无法获取到图片地址，请检查网络连接' + '\n')
            save_error_date(dirname)
        else:

            #调用图片保存模块
            download_img(img_url,dirname,market,resolution)


# 记录错误日期与保存图片原始地址

def save_error_date(dirname):
    #创建，并追加写入
    filename = dirname + "/" + "daily_bing_img_url.txt"
    local_date = time.strftime("%Y-%m-%d", time.localtime())
    if not os.path.exists(filename): 
        print ('提示：记录文件daily_bing_img_url.txt', filename, '不存在，重新建立', '\n')
        
    # 创建错误日期日志
    fw = open(filename, 'r+')
    #读旧数据
    old = fw.read()
    #回归初始位置
    fw.seek(0)
    #写新数据
    fw.write(local_date + "\t")
    fw.write("无法连接到网络"+ "\n") 
    #写旧数据
    fw.write(old)  
    #关闭文件指针
    fw.close()


#保存图片url地址子模块
def save_img_url_to_file(dirname,img_url,flag):
    #创建，并追加写入
    filename = dirname + "/" + "daily_bing_img_url.txt"
    local_date = time.strftime("%Y-%m-%d", time.localtime())
    if not os.path.exists(filename): 
        print ('提示：记录文件daily_bing_img_url.txt', filename, '不存在，重新建立', '\n')
        
    if flag == 1:
        fw = open(filename, 'r+')

        #读旧数据
        old = fw.read()
        #回归初始位置
        fw.seek(0)

        #写新数据
        fw.write(local_date + "\t")
        fw.write("保存成功"+ "\t")
        fw.write(img_url +"\n")

        #写旧数据
        fw.write(old)  

        #关闭文件指针
        fw.close()
    else:
        fw = open(filename, 'r+')

        #读旧数据
        old = fw.read()
        #回归初始位置
        fw.seek(0)

        #写新数据
        fw.write(local_date + "\t")
        fw.write("保存失败"+ "\t")
        fw.write(img_url +"\n")

        #写旧数据
        fw.write(old)  
        
        #关闭文件指针     
        fw.close()


def download_img(img_url,dirname,market,resolution = "1920x1080"):
    #分辨率替换
    img_url = img_url[0:img_url.find(".jpg")+4]
    img_url = img_url.replace("1920x1080",resolution)
        
    print('图片地址为：', img_url, '\n')
    #保留一份根目录地址
    root_dir = dirname

    #按照 地区\年\月\分辨率 归类并创建对应目录
    year = datetime.datetime.now().year
    year = str(year)
    month = datetime.datetime.now().month
    month = str(month)
    month = month.zfill(2)
    dirname = dirname + "/" + market
    dirname = dirname + "/" + year 
    dirname = dirname + "/" + month    
    dirname = dirname + "/" + resolution

    #创建目录对应的目录
    if not os.path.exists(dirname):
        print ('提示：文件夹', dirname, '不存在，重新建立', '\n')
        os.makedirs(dirname)

    # 用日期命名图片文件名，包括后缀 
    basename = time.strftime("%Y-%m-%d", time.localtime()) + "_" + resolution +"_"+ market + ".jpg"
    # 拼接目录与文件名，得到图片路径
    filepath = os.path.join(dirname, basename)

    #使用while循环来多次try和catch
    max_num = 0
    while max_num < 3:
        try:
            # 下载图片并重命名，并保存到文件夹中
            res = requests.get(img_url)
            with open(filepath,'wb') as f:
                f.write(res.content)
            flag = 1
                       
        except requests.exceptions.ConnectionError as e:
            print('错误：网络连接失败'+'\n', e, '\n')
            flag = 0
            max_num += 1

        except requests.exceptions.Timeout as e:
            print('错误：连接超时'+'\n', e, '\n')
            flag = 0
            max_num += 1

        except requests.exceptions.HTTPError as e:
            print('错误：非法的HTTP请求'+'\n', e, '\n')
            flag = 0
            max_num += 1

        except requests.exceptions.RequestException as e:
            print('错误：其他错误'+'\n', e, '\n')
            flag = 0
            max_num += 1

        else:
            print("保存", filepath, "成功！", '\n')
            break

    #调用图片url记录保存子模块,保存在文件在根目录下    
    save_img_url_to_file(root_dir,img_url,flag)
        

