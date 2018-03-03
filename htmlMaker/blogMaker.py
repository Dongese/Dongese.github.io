#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime


class BlogMaker(object):
	def __init__(self,title,subtitle):
		self.title = title
		self.subtitle = subtitle
		self.time     = datetime.datetime.today()
		self.rootPath = os.path.dirname(os.getcwd())
		self.checkAndLoadHtml()
		self.writePostPage()
		self.recordInfo()
		self.writeIndexPage()
		self.writeSharePage()


	def checkAndLoadHtml(self):
		# Index Page
		indexHeaderPath   = os.path.join(os.getcwd(),"index\\header.html")
		indexFooterPath   = os.path.join(os.getcwd(),"index\\footer.html")
		indexTemplatePath = os.path.join(os.getcwd(),"index\\template.html") 
		self.indexHeader   = self.readHtml(indexHeaderPath)
		self.indexFooter   = self.readHtml(indexFooterPath)
		self.indexTemplate = self.readHtml(indexTemplatePath)

		# Post Page
		postHeaderPath  = os.path.join(os.getcwd(),"post\\header.html")
		postFooterPath  = os.path.join(os.getcwd(),"post\\footer.html")
		postContentPath = os.path.join(os.getcwd(),"post\\save.html")
		self.postHeader  = self.readHtml(postHeaderPath)
		self.postFooter  = self.readHtml(postFooterPath)
		self.postContent = self.readHtml(postContentPath)

		# Share Page
		shareHeaderPath = indexHeaderPath
		shareFooterPath = os.path.join(os.getcwd(),"share\\footer.html")
		shareTemplatePath = os.path.join(os.getcwd(),"share\\template.html")
		self.shareHeader = self.readHtml(shareHeaderPath)
		self.shareFooter   = self.readHtml(shareFooterPath)
		self.shareTemplate = self.readHtml(shareTemplatePath)


	def readHtml(self,path):
		with open(path,"rt") as f:
			data = f.read()
		return data

	def writeHtml(self,path,data):
		with open(path,"wt") as f:
			f.write(data)

	def recordInfo(self):
		path = os.path.join(os.getcwd(),"post\\info.txt")
		with open(path,"rt") as f:
			data = f.read()
		info = ";".join([self.title,self.subtitle,self.time.strftime('%m %d.%Y')])
		self.data = "\n".join([info,data])
		with open(path,"wt") as f:
			f.write(self.data.encode('utf-8'))

	def writePostPage(self):
		self.postHeader = self.postHeader % (self.title,self.subtitle,self.time.strftime('%m %d.%Y'))
		self.post = "\n". join([self.postHeader,self.postContent,self.postFooter])
		fileName = "".join([self.rootPath,"\\post\\",self.title,".html"])
		self.writeHtml(fileName,self.post)

	def writeIndexPage(self, indexTitle = "Welcome", indexSubtitle = "To my blog"):
		contentList = []
		for infoData in self.data.split("\n"):
			title,subtitle,time = infoData.split(";")
			href = '"post/%s.html"' % title
			cont = self.indexTemplate % (href,title,subtitle,time)
			contentList.append(cont)

		content = "\n".join(contentList)
		self.indexHeader = self.indexHeader % (indexTitle,indexSubtitle)

		index = "\n". join([self.indexHeader,content,self.indexFooter])
		fileName = os.path.join(self.rootPath,"index.html")
		self.writeHtml(fileName,index)

	def writeSharePage(self, shareTitle = "Share", shareSubtitle = "All Posts"):
		shareList = []
		ym = None
		for infoData in self.data.split("\n"):
			title,_,time = infoData.split(";")
			href = '"post/%s.html"' % title
			cont = self.shareTemplate % (href,title)
			temp = "".join(["<P>",time.split(".")[-1]," ",time.split(".")[0].split(" ")[0],"</P>"])
			if temp != ym:
				saveList = [temp,cont]
				shareList.append(saveList)
				ym = temp
			else:
				saveList.append(cont)

		content = []
		for listPost in shareList:
			content.append("\n".join(listPost))
		content = "\n".join(content)
		self.shareHeader = self.shareHeader % (shareTitle,shareSubtitle)
		share = "\n".join([self.shareHeader,content,self.shareFooter])
		fileName = os.path.join(self.rootPath,"share.html")
		self.writeHtml(fileName,share)



if __name__ == '__main__':

	title     = "Bitcoin: A Peer-toPeer Electronic Cash System, by Satoshi Nakamoto"
	subtitle  = "Bitcoin become more and more popular. My note will figure out every details about bitcoin."
	BlogMaker(title,subtitle)

