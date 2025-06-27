from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jas:Jaspreet-123@restro.6lokl.mongodb.net/?retryWrites=true&w=majority&appName=Restro")

db = client['sma_trading']
collection = db['stock_data']

sample_data = collection.find_one()

print("Sample document from MongoDB:", sample_data)
