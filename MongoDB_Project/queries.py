from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select the database
db = client.project

# Collections
collections = {
    "Channels": db.channels,
    "Videos": db.videos,
    "Playlists": db.playlists,
    "Comments": db.comments
}

# Count of rows and sample documents from each collection
for name, collection in collections.items():
    count = collection.count_documents({})
    print(f"Count of rows in {name} collection: {count}")

    print(f"Sample documents from {name} collection:")
    sample = collection.find().limit(3)
    for doc in sample:
        print(doc)
    print("\\n")

# Perform a join between Channels and Videos using local and foreign key
pipeline = [
    {
        '$lookup': {
            'from': "videos",
            'localField': "channel_id",
            'foreignField': "channel_id",
            'as': 'videos'
        }
    },
    {
        '$limit': 3  # Show only 3 joined results for brevity
    }
]

joined_result = db.channels.aggregate(pipeline)

print("Joined data (Channels and Videos):")
for doc in joined_result:
    print(doc)
    print("\\n")