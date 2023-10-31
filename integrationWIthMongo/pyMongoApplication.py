import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:<passwd>@cluster1.ercrt8d.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

# definição de infor para compor o doc
post1 = {
    "nome": "Marcos",
    "cpf": "12349039877",
    "endereco": "st John 310",
    "contas": [
        {
            "tipo": "Conta Corrente",
            "agencia": "001",
            "numero": "1001",
            "saldo": 1000.00
        }
    ]
}

post2 = {
    "nome": "Ana",
    "cpf": "98765432101",
    "endereco": "Elm Street 123",
    "contas": [
        {
            "tipo": "Conta Corrente",
            "agencia": "003",
            "numero": "3001",
            "saldo": 1500.00
        }
    ]
}

# preparando para submeter as infos
print("\nPrimeiro objeto")
posts = db.posts
post_id = posts.insert_one(post1).inserted_id
print(post_id)

pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [{
    "nome": "Alice",
    "cpf": "12345678901",
    "endereco": "123 Elm St",
    "contas": [
        {
            "tipo": "Conta Corrente",
            "agencia": "001",
            "numero": "1001",
            "saldo": 1500.00
        }
    ]}, {
    "nome": "Bob",
    "cpf": "98765432101",
    "endereco": "456 Oak St",
    "contas": [
        {
            "tipo": "Conta Poupança",
            "agencia": "002",
            "numero": "2001",
            "saldo": 2500.00
        }
    ]}
]

print("\nRecuperação final")
result = posts.insert_many(new_posts)
print(result.inserted_ids)
pprint.pprint(db.posts.find_one({"nome": "Bob"}))

print("\n contando documentos")
print(posts.count_documents({}))

pprint.pprint(posts.find_one({"agencia": "2001"}))
