#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
from docx import Document
from docx.shared import Inches
import time

def tans(q):
	appid = ''  # 填写你的appid
	secretKey = ''  # 填写你的密钥

	httpClient = None
	myurl = '/api/trans/vip/translate'

	fromLang = 'auto'   #原文语种
	toLang = 'zh'   #译文语种
	salt = random.randint(32768, 65536)
	#q= 'I love you fuck'
	sign = appid + q + str(salt) + secretKey
	sign = hashlib.md5(sign.encode()).hexdigest()
	myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
	salt) + '&sign=' + sign

	try:
		httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
		httpClient.request('GET', myurl)

		# response是HTTPResponse对象
		response = httpClient.getresponse()
		result_all = response.read().decode("utf-8")
		result = json.loads(result_all)
		chi = result["trans_result"][0]["dst"]

		return chi

	except Exception as e:
		print (e)
	finally:
		if httpClient:
			httpClient.close()


document = Document('')  #打开文件demo.docx
for x in document.paragraphs: 
	if tans(x.text) == None:
		continue
	else:
		x.text=x.text.replace(x.text,tans(x.text))
	time.sleep(0.1)

document.save(r"")	#文件位置
