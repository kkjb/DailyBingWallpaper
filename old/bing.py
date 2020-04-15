# 下载并存储必应每日壁纸到指定位置

import time
import os
import urllib.request
import requests

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


# 文件夹不存在就创建
def create_404_dir(dirname):

    if not os.path.exists(dirname):
        print ('    提示：文件夹', dirname, '不存在，重新建立', '\n')
        os.makedirs(dirname)

# 这段推倒重写，使用python logger        
def log_record(dirname,log_txt):
    
    # change the directory to dirname
    os.chdir(dirname)
    
    # set default name for logging
    log_name = "log.txt"
    
    # get current time 
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # judge txt exists or not
    if not os.path.exists(log_name): 
        fw = open(log_name, 'a')
        fw.write(local_time + "\t" +log_txt)   
        fw.close()
    else:
        fw = open(log_name, 'a')
        fw.write(local_time + "\t" +log_txt) 
        fw.close()
        
#http://cn.bing.com/HPImageArchive.aspx?format=json&idx=0&n=1&mkt=zh-cn
        
def get_img_url(dirname,market):
    try:
        # 得到图片文件的网址
        raw_img_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        mkt_suffix = "&mkt=" + market 
        raw_img_url = raw_img_url +mkt_suffix
        response = requests.get(raw_img_url)    
        
        result = response.json()
        url_prefix ="https://www.bing.com"
        img_url = url_prefix + result["images"][0]["url"]
        
    except Exception as e:
        error_tips = 'error: wrong raw_img_url' + '\n'
        #log_record(dirname,error_tips)
        return False
    else:
        return img_url

# 保存图片到磁盘文件夹dirname中
# "1080x1920"
'''
    [ValidateSet('auto', 'ar-XA', 'bg-BG', 'cs-CZ', 'da-DK', 'de-AT',
    'de-CH', 'de-DE', 'el-GR', 'en-AU', 'en-CA', 'en-GB', 'en-ID',
    'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-PH', 'en-SG', 'en-US',
    'en-XA', 'en-ZA', 'es-AR', 'es-CL', 'es-ES', 'es-MX', 'es-US',
    'es-XL', 'et-EE', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR',
    'he-IL', 'hr-HR', 'hu-HU', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT',
    'lv-LV', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT',
    'ro-RO', 'ru-RU', 'sk-SK', 'sl-SL', 'sv-SE', 'th-TH', 'tr-TR',
    'uk-UA', 'zh-CN', 'zh-HK', 'zh-TW')]
'''

def resolution_repalce(img_url, resolution):
    
    img_url = img_url.replace("1920x1080",resolution)
    
    return img_url

def save_img(img_url, dirname, market, resolution = "1920x1080"):
    
    img_url = resolution_repalce(img_url,resolution)
    
    dirname = dirname +"/" + resolution
    
    create_404_dir(dirname)
    
    try:
        # 用日期命名图片文件名，包括后缀 
        basename = time.strftime("%Y-%m-%d", time.localtime()) + "_" + resolution +"_"+ market + ".jpg"
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print('    错误：文件操作失败', e, '\n')
    except Exception as e:
        print('    错误：', e, '\n')
    else:
        print("    保存", filepath, "成功！", '\n')
        
    return filepath


        

def save_bing_wallpaper(dirname,resolution,market):
    
    dirname = dirname +'/' + market
    
    create_404_dir(dirname)
    
    print("壁纸将被保存在：", dirname, '\n')
    market = market.upper()
    if market not in valid_mkt:
        print("不存在的地区，请检查", '\n')
    else:
        img_url = get_img_url(dirname,market)
    
    if img_url != False:
        print('图片地址为：', img_url, '\n')
        filepath = save_img(img_url, dirname,market,resolution)   # 图片文件的的路径
    
    
    
    
# 请求网页，跳转到最终 img 地址

'''
def main():
    dirname = "D:\\壁纸\\Bing"              # 图片要被保存在的位置
    dirname_mobile = "D:\\壁纸\\Bing\\1080x1920"   
    print("壁纸将被保存在：", dirname, '\n')

    img_url = get_img_url(dirname,"en-us")
    if img_url != False:
        print('图片地址为：', img_url, '\n')
        filepath = save_img(img_url, dirname)   # 图片文件的的路径


main()
'''