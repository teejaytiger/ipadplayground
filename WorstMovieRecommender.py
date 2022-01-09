import random
import webbrowser
import urllib.request
from urllib.request import build_opener, HTTPCookieProcessor

class gentt:
	def __init__(self):
		self.url=""
		self.val = self.gen_val()
		self.fail='https://www.imdb.com/title/tt5865147/'
		
	def gen_val(self):
		self.val = "tt"+''.join(["{}".format(random.randint(0, 9)) for num in range(0, 7)])
		self.url="https://www.imdb.com/title/"+self.val+"/"

def pick_movie(c):
	opener = build_opener(HTTPCookieProcessor())
	try:
		response = opener.open(c.url)
		print(c.url + " success")
	except:
		print(c.url + " fail")
		c.gen_val()
		pick_movie(c)
		
c = gentt()
pick_movie(c)
webbrowser.open(c.url)
