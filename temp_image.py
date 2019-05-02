# import the necessary packages
import os
import time

class TempImage:
	def __init__(self, basePath="./media/", ext=".jpg"):
		# construct the file path
		self.path = "{base_path}/{name}{ext}".format(base_path=basePath,
			name=time.strftime("%Y%m%d-%H%M%S"), ext=ext)

	def cleanup(self):
		# remove the file
		os.remove(self.path)