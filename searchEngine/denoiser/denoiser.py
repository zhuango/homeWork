#!/usr/bin/python

from goose import Goose
from pathlib import Path
from goose.text import StopWordsChinese
import os
import codecs

url = '/home/laboratory/weblech/cleanSites/blog.sina.com.cn/5483xz'
# urlf = open(url, 'r')
# rawHtml = ''
# for line in urlf:
#     rawHtml += line + " "
#url = 'https://github.com/steinbacher/goose'
g_cn = Goose({'stopwords_class': StopWordsChinese})
g_en = Goose()
# article = g_cn.extract(raw_html=rawHtml)
# print(article.title)
# print(article.meta_description)
# print(article.cleaned_text)
# print(article.top_image.src)
rawHtml = ""
with open (url, 'r') as f:
    for line in f:
        rawHtml += line + " " 
#if isinstance(rawHtml, unicode):
rawHtml = rawHtml.encode('utf-8')
article_cn = g_cn.extract(raw_html=rawHtml)
article_en = g_en.extract(raw_html=rawHtml)

cleanFilePath = "/home/laboratory/weblech/cleanSites/blog.sina.com.cn/testU"
cleanedWebpage = codecs.open(cleanFilePath, 'w')

cleanedWebpage.write("<title>" + article_cn.title + "</title>\n")
cleanedWebpage.writelines(article_cn.meta_description)
cleanedWebpage.writelines(article_cn.cleaned_text)
cleanedWebpage.writelines(article_en.title)
cleanedWebpage.writelines(article_en.meta_description)
cleanedWebpage.writelines(article_en.cleaned_text)

cleanedWebpage.close()

cleanSitePath = "/home/laboratory/weblech/cleanSites"
dirtySitePath = "/home/laboratory/weblech/sites"

def cleanWebPages(dirtySitePath, cleanSitePath):
    print("processing " + dirtySitePath)
    if not os.path.exists(cleanSitePath):
        os.makedirs(cleanSitePath)
    dirInfo = Path(dirtySitePath)
    for item in dirInfo.iterdir():
        if item.is_file():
            try:
                dirtyFilePath = str(item)
                rawHtml = ""
                with open (dirtyFilePath, 'r') as f:
                    for line in f:
                        rawHtml += line + " " 
                article_cn = g_cn.extract(raw_html=rawHtml)
                article_en = g_en.extract(raw_html=rawHtml)
                
                fileName = os.path.basename(dirtyFilePath)
                cleanFilePath = os.path.join(cleanSitePath, fileName)
                cleanedWebpage = codecs.open(cleanFilePath, 'w', "utf-8")

                cleanedWebpage.write("<title>" + article_cn.title + "</title>\n")
                cleanedWebpage.writelines(article_cn.meta_description)
                cleanedWebpage.writelines(article_cn.cleaned_text)
                cleanedWebpage.writelines(article_en.title)
                cleanedWebpage.writelines(article_en.meta_description)
                cleanedWebpage.writelines(article_en.cleaned_text)

                cleanedWebpage.close()
            except:
                continue

        if item.is_dir():
            dirtyFolder = str(item)
            folderName = os.path.basename(dirtyFolder)
            cleanFolder = os.path.join(cleanSitePath, folderName)
            cleanWebPages(dirtyFolder, cleanFolder)

cleanWebPages(dirtySitePath, cleanSitePath)