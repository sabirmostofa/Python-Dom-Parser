#!/usr/bin/env python

import urllib2
import re
import htmlentitydefs
import HTMLParser


#function copied from Internet

def unescape(text):
	def fixup(m):
		text = m.group(0)
		if text[:2] == "&#":
		# character reference
			try:
				if text[:3] == "&#x":
					return unichr(int(text[3:-1], 16))
				else:
					return unichr(int(text[2:-1]))
			except ValueError:
				pass
		else:
		# named entity
			try:
				text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
			except KeyError:
				pass
		return text # leave as is
	return re.sub("&#?\w+;", fixup, text)


print "Content-type: text/plain\n"
#req = urllib2.Request('http://itunes.apple.com/us/rss/topfreeapplications/limit=10/xml')
#response = urllib2.urlopen(req)
#raw_string = response.read()
f=open('rank.xml','r')
raw_string = f.read()
#raw_string = raw_string.encode('string_escape')
#print raw_string
#print raw_string.find('image')

#feed=re.compile(r'(\b\w+)\s+\1',re.DOTALL)
#feed=re.compile(r'<entry>.*</entry>.*(?=<entry>)')
feed=re.compile(r'(<entry.*?/entry>)',re.S)

a= feed.findall(raw_string)


for entry in a:
	updated_re = re.compile(r'(?<=<updated>).*?(?=</updated>)',re.S)
	id_re = re.compile(r'(?<=<id>).*?(?=</id>)',re.S)
	title_re = re.compile(r'(?<=<title>).*?(?=</title>)',re.S)
	summary_re = re.compile(r'(?<=<summary>).*?(?=</summary>)',re.S)
	link_re = re.compile(r'(?<=href=").*?(?=")', re.S)
	
	updated= updated_re.search(entry).group()
	entry_id = id_re.search(entry).group()
	title= title_re.search(entry).group()	
	summary =  summary_re.search(entry).group()
	link =link_re.search(entry).group()
	#print '<br/>',updated,'<br/>',title,'<br/>',entry_id,'<br/>',summary,'<br/>',link,'<br/>'

def getAttr(text,tag,attr):
	reString = '<{0}[^>]*>'.format(tag)
	tag_re = re.compile(reString,re.S)
	node = tag_re.search(text).group()
		
	attrString='(?<={0}=").*?(?=")'.format(attr)
	attr_re =  re.compile(attrString,re.S)
	return attr_re.search(node).group()
	
	
def getTag(tag,text):	
	"""only supports <id></id> style tags returns the innerText"""
	reString = '(?<=<{0}>).*?(?=</{0}>|/>)'.format(tag)	
	tag_re = re.compile(reString,re.S) 
	return tag_re.search(text).group()

def innerText(tag,doc):
	reString = '(?<=<{0})[^>]*>(.*?)(?=</{0}>)'.format(tag)	
	tag_re = re.compile(reString,re.S)
	return  tag_re.search(doc).group(1) 	
	
 
def getTagById(id):
	pass	

print getAttr(a[9],'im:image','height')

print '<><><><>'
print getTag.__doc__

print innerText('im:price',a[0]);

#Reinventing the wheel, A class for parsing HTML XML DOM

class node:
	def __init__(self,tag):
		self.node=tag
	
	def attr(self,attr):
		attrString='(?<={0}=").*?(?=")'.format(attr)
		attr_re =  re.compile(attrString,re.S)
		return attr_re.search(self.node).group()
		 

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
			return node(x)
			
		if(len(tags)>0):
			return map(callNode,tags)
	
	def getById(self,idS):
		idStr =  'id="{0}"'.format(idS)
		attr_re =  re.compile(idStr,re.S)
	
		for elem in self.elems:
			if(attr_re.search(elem)!=None):
				return attr_re.search(elem).group()
			
		

		
		
			

		
	


ex= parser(a[0]).getByTag('link')[0].attr('href')
b= parser(a[0]).getById('hellosA')

print b

print 'after init'

























	

	

	



