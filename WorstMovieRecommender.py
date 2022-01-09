import random
import webbrowser
from urllib.request import build_opener, HTTPCookieProcessor

class gentt:
	def __init__(self):
		self.url=self.gen_val()	
	def gen_val(self):
		val = "tt"+''.join(["{}".format(random.randint(0, 9)) for num in range(0, 7)])
		self.url="https://www.imdb.com/title/"+val+"/"

def pick_movie(c):
	try:
		response = build_opener(HTTPCookieProcessor()).open(c.url)
	except:
		c.gen_val()
		pick_movie(c)
c = gentt()
pick_movie(c)
webbrowser.open(c.url)