from django.db import models

class URLtoHASH(models.Model):
	''' 
		Model defining a url value and corresponding hash value
	'''
	
	url = models.TextField()
	hash_value = models.TextField()

	def __unicode__(self):
		return self.url
