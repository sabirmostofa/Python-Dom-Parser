#!/usr/bin/env python

"""Simple HTML/XML Parser
Can detect the malformed  tags lik id=sth or style=somevalue etc. 
Sample usage:
 Instantiate the parser class by providing the url  or xml|http string
 
 To Get the 'id' attribute of the 'style' tag
 1.spp.parser('http://www.google.com').getByTag('style').item(0).attr('id')
 
 To get the attribute of a node whose id is 'csi'
 2.spp.parser('http://www.google.com').getById('csi).attr('style')
 
 # doc is the html or xml string you want to parse
 3.spp.parser(doc).getById('test').attr('href')
 
 To get the src of an image which is the 4th image of the document
 4.spp.parser(doc).getBytag('img').item(4).attr('src')
 
 To get the content of a node which has no child
 5.spp.parser(doc).getById('test').innerText()

"""

__author__ = "Sabirul Mostofa"
__copyright__ = "Copyright 2011"
__license__ = "GPL V2.0"
__version__ = "0.1"
__email__ = "sabirmostofa@gmail.com"
__status__ = "Production"

import re
import urllib2

class node:
    def __init__(self,tag,tagName=None,motherdoc=None):
        self.node=tag
        self.tagName = tagName
        self.doc =motherdoc
        
        
    
    def attr(self,attr):
        """supporting  id="test" | id='test' | id=test"""
        attrString='((?<={0}=").*?(?="))|((?<={0}=\').*?(?=\'))|((?<={0}=)[^\'"]+?(?=\s|>))'.format(attr)
        attr_re =  re.compile(attrString,re.S)
        return attr_re.search(self.node).group()
    
    def innerText(self):
        """Returns the Node Content: It returns only the single node content 
        So user this function to the node which has no childs
        """
        reString = '(?<=<{0})[^>]*>(.*?)(?=</{0}>)'.format(self.tagName)    
        tag_re = re.compile(reString,re.S)
        matches = re.findall(tag_re,self.doc)
        if(self.num!=-1):
            return matches[self.num]
        else:
            reString = '(?<=<{0}).*?\sid=(?:"|\')?{1}(?:"|\')?[^>]*>(.*?)(?=</{0}>)'.format(self.tagName,self.ida)    
            tag_re = re.compile(reString,re.S)
            matches = re.findall(tag_re,self.doc)
            return matches[0]         

class parser:
    """Instantiate this class like 
    spp.parser(doc)
    doc can be either xml|http document string or a URL 
    You can chain the methods """
    doc=''
    #elems is the total number of tags
    elems=''
    
    def __init__(self,doc):
        if(re.search(r'^http://',doc)):
            req = urllib2.Request(doc)
            self.doc = urllib2.urlopen(req).read()
        else:
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
            self.tagObjs= map(callNode,tags)
        return self
        
    def getById(self,idS):
        idStr =  '(id="{0}")|(id={0})|(id=\'{0}\')'.format(idS)
        attr_re =  re.compile(idStr,re.S)
        
        def getNum(single,allE):
            count=0
            for i in allE:
                if (i==single):
                    return count
                count=count+1
            
    
        for elem in self.elems:
            if(attr_re.search(elem)!=None):                
                tag = re.search(r'<(.*?)\s',elem).group(1)
                obj=node(elem,tag,self.doc)
                obj.num=-1
                obj.ida=idS
                return obj
                
                
                
    def item(self,no):
        """Returns a Node object and sets the number"""
        self.tagObjs[no].num=no
        return self.tagObjs[no]
        
