
Copy the spp.py in your working directory and import the package.

Sample usage:
 Instantiate the parser class by providing the url  or xml|html string
 
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
