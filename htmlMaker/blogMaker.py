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


	def checkAndLoadHtml(self):
		# Index Page
		indexHeaderPath   = os.path.join(os.getcwd(),"index\\header.html")
		indexFooterPath   = os.path.join(os.getcwd(),"index\\footer.html")
		indexTemplatePath = os.path.join(os.getcwd(),"index\\template.html") 
		if os.path.exists(indexHeaderPath) and os.path.exists(indexFooterPath) and os.path.exists(indexTemplatePath):
			self.indexHeader   = self.readHtml(indexHeaderPath)
			self.indexFooter   = self.readHtml(indexFooterPath)
			self.indexTemplate = self.readHtml(indexTemplatePath)

		# Post Page
		postHeaderPath  = os.path.join(os.getcwd(),"post\\header.html")
		postFooterPath  = os.path.join(os.getcwd(),"post\\footer.html")
		postContentPath = os.path.join(os.getcwd(),"post\\save.html")
		if os.path.exists(postHeaderPath) and os.path.exists(postFooterPath) and os.path.exists(postContentPath):
			self.postHeader  = self.readHtml(postHeaderPath)
			self.postFooter  = self.readHtml(postFooterPath)
			self.postContent = self.readHtml(postContentPath)

	def readHtml(self,path):
		with open(path,"rt") as f:
			data = f.read()
		return data

	def writeHtml(self,path,data):
		with open(path,"wt") as f:
			f.write(data.encode('utf-8'))

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

	def writeIndexPage(self):
		contentList = []
		for infoData in self.data.split("\n"):
			title,subtitle,time = infoData.split(";")
			href = '"post/%s.html"' % title
			cont = self.indexTemplate % (href,title,subtitle,time)
			contentList.append(cont)
		content = "\n".join(contentList)
		index = "\n". join([self.indexHeader,content,self.indexFooter])
		fileName = os.path.join(self.rootPath,"index.html")
		self.writeHtml(fileName,index)


if __name__ == '__main__':

	title     = "Test"
	subtitle  = "Test"
	BlogMaker(title,subtitle)

