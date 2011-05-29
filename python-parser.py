import re
""" New Class is being generated For better experience. This is going to be fun"""
def getAttr(text,tag,attr):
	reString = '<{0}[^>]*>'.format(tag)
	tag_re = re.compile(reString,re.S)
	node = tag_re.search(text).group()
		
	attrString='(?<={0}=").*?(?=")'.format(attr)
	attr_re =  re.compile(attrString,re.S)
	return attr_re.search(node).group()
	
	
def getTag(tag,text):	
	#only supports <id></id> style tags returns the innerText
	reString = '(?<=<{0}>).*?(?=</{0}>|/>)'.format(tag)	
	tag_re = re.compile(reString,re.S) 
	return tag_re.search(text).group()

def innerText(tag,doc):
	#supports all kinds of tags like <id style=''>hello</id>
	reString = '(?<=<{0})[^>]*>(.*?)(?=</{0}>)'.format(tag)	
	tag_re = re.compile(reString,re.S)
	return  tag_re.search(doc).group(1) 	
	
