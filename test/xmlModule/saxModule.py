#!/usr/bin/python
# coding=UTF-8
# author: xuegangliu
# description: sax 解析xml文件

import xml.sax

"""
   解析XML实例
   SAX是一种基于事件驱动的API。
   利用SAX解析XML文档牵涉到两个部分:1.解析器  2.事件处理器。
   解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
   而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。
   1、对大型文件进行处理；
   2、只需要文件的部分内容，或者只需从文件中得到特定信息。
   3、想建立自己的对象模型的时候。
"""
class MovieHandler(xml.sax.ContentHandler):
   '''movies.xml 对象'''

   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   def startElement(self, tag, attributes):
      '''元素开始调用'''

      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         print ("Title:", title)

   def endElement(self, tag):
      '''元素结束调用'''

      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   def characters(self, content):
      '''读取字符时调用'''

      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content