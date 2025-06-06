# Python example of using narwhals with a MongoDB backend

A Python example of using narwhals with a MongoDB backend

## References

*

## History

| Date       | Description      |
|:-----------|:-----------------|
| 2025-06-06 | Initial creation |

## Tools Used

| Tool     |  Version |
|:---------|---------:|
| Python   |   3.13.3 |
| narwhals |   1.41.1 |
| pymongo  |   4.13.0 |
| VSCode   |  1.100.3 |
| PyCharm  | 2025.1.1 |

# Developer Notes

from pymongo import MongoClient

# Replace with your MongoDB Atlas connection string
client = MongoClient("mongodb+srv://your_username:your_password@your_cluster.mongodb.net/?retryWrites=true&w=majority")

# Select the database and collection
db = client["narwhal_database"]
collection = db["narwhals"]

class Narwhal:
    def __init__(self, name, age, tusk_length):
        self.name = name
        self.age = age
        self.tusk_length = tusk_length

    def to_dict(self):
        return {"name": self.name, "age": self.age, "tusk_length": self.tusk_length}


narwhal = Narwhal("Nelly", 5, 2.5)
collection.insert_one(narwhal.to_dict())
print("Narwhal added to MongoDB!")

for narwhal in collection.find():
    print(narwhal)


collection.update_one({"name": "Nelly"}, {"$set": {"age": 6}})
print("Narwhal updated!")


collection.delete_one({"name": "Nelly"})
print("Narwhal removed!")