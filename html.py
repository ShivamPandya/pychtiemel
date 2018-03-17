import os

mainDir = os.path.join(os.getcwd(),"www")
style = os.path.join(os.getcwd(),"www","css")
js = os.path.join(os.getcwd(), "www","js")

page = os.getcwd() + "\\src\\pages"

 
if not os.path.exists(mainDir):
    os.mkdir(mainDir)
    if not os.path.exists(style):
        os.makedirs(style)
    if not os.path.exists(js):
        os.makedirs(js)

html = open(os.path.join(mainDir, "index.html"), "w")

html.write("""<html> \n \t <head> \n \t \t <title> My Site </title> \n \t \t <link href="css/style.css" rel="stylesheet"> \n \t </head> \n <body> \n \n <h1>Demo Site</h1> \n \n \n </body> \n </html> """) 

styleFile = open(os.path.join(style, "style.css"), "w")
jsFile = open(os.path.join(js, "script.js"), "w")