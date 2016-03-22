# import pymongo


# conn = pymongo.MongoClient("localhost",27017)
# db = conn['Zoukloans']
# coll_name = raw_input("Collection name : ")
# coll = db[coll_name]


class Pymongo_importer():
	"""a class for utility functions used in MongoDB connection"""
	def __init__(self):
		import pymongo
		self.conn = pymongo.MongoClient("localhost",27017)
		self.db = self.conn['Zoukloans']
		# print self.db.collection_names()
		
	def new_collection(self):
		coll_name = raw_input("Enter collection name: ")
		try:
			self.db.validate_collection(coll_name)["valid"]
		except OperationFailure:
			self.db.create_collection(coll_name)
		return 	
	def json_to_csv(self):


		return True	

if __name__ == '__main__':
	classobj = Pymongo_importer()
