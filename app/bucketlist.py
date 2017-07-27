class Bucketlist(object):
	allbucketlists = []

	def __init__(self, name=None):
		self.name = name

	def create_bucketlist(self, name=None):
		self.allbucketlists.append(name)
		return self.allbucketlists

	def view_bucketlist(self):
		if self.allbucketlists:
			return self.allbucketlists
			
	'''Delete bucketlists'''
	def delete(self):
		for items in self.allbucketlists:
			if items.name == name:
				self.allusers.remove(users)