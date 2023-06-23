import pprint
import datetime
import pymongo as pyM



# Create a new client and connect to the server
client = pyM.MongoClient("mongodb+srv://dio:<password>@dio.6pfzzjx.mongodb.net/?retryWrites=true&w=majority")


db = client.test
collection = db.test_collection
print(db.test_collection)

#doc test
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

#preparando para submeter as info
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# Recuperando arquivo de doc test

pprint.pprint(db.posts.find_one())

#definindo docs
newPost = [
    {
    "tipo" : "Corrente",
    "agencia" : " 001",
    "num" : "1234",
    "id_cliente" : "1",
    "saldo" : "1000",
    "date": datetime.datetime.utcnow()
    },
    {
    "tipo" : "Corrente",
    "agencia" : "001",
    "num" : "3214",
    "id_cliente" : "2",
    "saldo" : "50000",
    "date": datetime.datetime.utcnow()
    },
    {
    "tipo" : "Poupança",
    "agencia" : "001",
    "num" : "4568",
    "id_cliente" : "3",
    "saldo" : "200000",
    "date": datetime.datetime.utcnow()
    }

]

result = posts.insert_many(newPost)
print(result.inserted_ids)

print("\nRecuperando....find_one.....")
pprint.pprint(db.posts.find_one({"tipo" : "Corrente"}))
print("\n....................................................")


print("\nRecuperando....find com for.....")
for post in posts.find():
    pprint.pprint(post)
print("\n....................................................")

