#!/usr/bin/env python

"""Simple HTML/XML Parser

"""

__author__ = "Sabirul Mostofa"
__copyright__ = "Copyright 2011"
__license__ = "GPL V2.0"
__version__ = "1.0"
__maintainer__ = "Sabirul Mostofa"
__email__ = "sabirmostofa@gmail.com"
__status__ = "Production"

import re

class node:
	def __init__(self,tag,tagName=None,motherdoc=None):
		self.node=tag
		self.tagName = tagName
		self.doc =motherdoc
		
	
	def attr(self,attr):
		attrString='(?<={0}=").*?(?=")'.format(attr)
		attr_re =  re.compile(attrString,re.S)
		return attr_re.search(self.node).group()
	
	def innerText(self):
		#For inner values
		reString = '(?<=<{0})[^>]*>(.*?)(?=</{0}>)'.format(self.tagName)	
		tag_re = re.compile(reString,re.S)
		return tag_re.search(self.doc).group(1) 
		 

class parser:
	doc=''
	elems=''
	
	def __init__(self,doc):
		self.doc=doc
		tag_re = re.compile(r'<(?!/).*?>',re.S)
		self.elems =  re.findall(tag_re, self.doc)
		
	def count(self):
		return len(self.elems)
		
	def getByTag(self,tag):
		attrString = '<{0}.*?>'.format(tag)
		attr_re =  re.compile(attrString,re.S)
		tags = re.findall(attr_re, self.doc)
				
		def callNode(x):
			return node(x,tag,self.doc)
			
		if(len(tags)>0):
			return map(callNode,tags)
	
	def getById(self,idS):
		idStr =  'id="{0}"'.format(idS)
		attr_re =  re.compile(idStr,re.S)
	
		for elem in self.elems:
			if(attr_re.search(elem)!=None):
				return attr_re.search(elem).group()
