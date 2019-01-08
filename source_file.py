import os
import time

class source_file(object):
	def __init__(self, filename):
		self.filename = filename
		
	def get_last_modified(self):
		return time.ctime(os.path.getmtime(self.filename))
		
	def get_base_name(self):
		return os.path.basename(self.filename)
		
	def get_text(self):
		text = ""
		while len(text) == 0:
			with open(self.filename, 'r') as content_file:
				text = content_file.read()
			
			time.sleep(0.1)
			
		return text