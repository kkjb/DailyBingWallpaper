# DailyBingWallpaper / 每日必应壁纸
This repo is designed for save the bing wallpaper daily
用来保存每日必应壁纸

## Environment/环境
Python3
Package:
requests

## Finished Features / 已完成功能
**Multi-resolution wallpapers download**
**多种分辨率壁纸下载**

添加了UHD全高清画质的支持，传递字符串"UHD" 给resolution即可

**Switching regions**
**地区切换**

Auto-start bash for VPS
VPS自启动脚本

## Explanation / 解释


bing.py is the core part of this repo, function bing.save_bing_wallpaper provides three parameters, *dirname* , *region* and *resolution*.

dirname is the position for saving the pictures

resolution should be given in the form of width * height, like 1920x1080 or 1080x1920

region must be in the valid set, which is given as below,


valid_mkt = ['ar-XA', 'bg-BG', 'cs-CZ', 'da-DK', 'de-AT',
    'de-CH', 'de-DE', 'el-GR', 'en-AU', 'en-CA', 'en-GB', 'en-ID',
    'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-PH', 'en-SG', 'en-US',
    'en-XA', 'en-ZA', 'es-AR', 'es-CL', 'es-ES', 'es-MX', 'es-US',
    'es-XL', 'et-EE', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR',
    'he-IL', 'hr-HR', 'hu-HU', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT',
    'lv-LV', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT',
    'ro-RO', 'ru-RU', 'sk-SK', 'sl-SL', 'sv-SE', 'th-TH', 'tr-TR',
    'uk-UA', 'zh-CN', 'zh-HK', 'zh-TW']

