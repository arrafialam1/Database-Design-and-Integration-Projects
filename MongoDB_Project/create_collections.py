from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create the database
db = client.project

# Create the collections
channels_collection = db.channels
videos_collection = db.videos
playlists_collection = db.playlists
comments_collection = db.comments

# Insert data into Channels collection
channels = [
    {"channel_id": 1, "channel_name": "ALRA TV", "description": "ALRA TV serves as the official YouTube channel of the esteemed Universal Sufi Order, helmed by the revered Sufi Master Younus AlGohar", "total_videos": 2760, "subscribers": 1300000},
    {"channel_id": 2, "channel_name": "ALRA TV CLIPS", "description": "Official clips and highlights channel, owned and operated by the ALRA TV team", "total_videos": 69, "subscribers": 6230},
    {"channel_id": 3, "channel_name": "Sufi Library", "description": "This channel is aimed at providing the world with the speeches of His Holiness Younus AlGohar, the Representative of Imam Mehdi, Messiah & Kalki Avatar and the CEO of Messiah Foundation International", "total_videos": 130, "subscribers": 28600},
    {"channel_id": 4, "channel_name": "Paigham e Gohar", "description": "This channel is dedicated for spreading the message of Divine Love as per teachings of His Holiness Riaz Ahmed Gohar Shahi, who is a world renowned spiritual personality", "total_videos": 346, "subscribers": 12500},
    {"channel_id": 5, "channel_name": "Mehdi Foundation India Official", "description": "Video contents to spread the mission of Imam Mehdi Sarkar Gohar Shahi", "total_videos": 100, "subscribers": 3030},
    {"channel_id": 6, "channel_name": "Microsoft Azure", "description": "Microsoft Azure discussion and knowledge hub", "total_videos": 1400, "subscribers": 315000},
    {"channel_id": 7, "channel_name": "Google Career Certificates", "description": "Preparing you for entry-level roles in growing career paths", "total_videos": 803, "subscribers": 418000},
    {"channel_id": 8, "channel_name": "Caleb Oni. Certified", "description": "Just a Cloud Security Engineer documenting my career progress, helping people on the way!", "total_videos": 115, "subscribers": 9340},
    {"channel_id": 9, "channel_name": "Nicole Enesse", "description": "What I wish I had known when I started my career in tech", "total_videos": 146, "subscribers": 59300},
    {"channel_id": 10, "channel_name": "Learn English With TV Series", "description": "On this channel, we will practice and improve our listening comprehension, using your favorite TV shows, movies, and talk shows", "total_videos": 501, "subscribers": 8970000}
]
channels_collection.insert_many(channels)

# Insert data into Videos collection
videos = [
    {"video_id": 1, "channel_id": 1, "title": "Zikr e Qalb Kya Hai? | Younus AlGohar | ALRA TV", "views": 443543, "likes": 4500},
    {"video_id": 2, "channel_id": 2, "title": "The Religion of God (English Voiceover)", "views": 1476, "likes": 189},
    {"video_id": 3, "channel_id": 3, "title": "YOUNUS ALGOHAR Jashan-e-Shahi Speech, Karachi 1999", "views": 10758, "likes": 925},
    {"video_id": 4, "channel_id": 4, "title": "Image Of Imam Mehdi (A.S) On Moon (Wajah Imam Mahdi di Bulan)", "views": 812735, "likes": 2100},
    {"video_id": 5, "channel_id": 5, "title": "HH Younus AlGohar Nepal visit Nov 2018 Highlights", "views": 7899, "likes": 664},
    {"video_id": 6, "channel_id": 6, "title": "How does Microsoft Azure work?", "views": 779900, "likes": 6500},
    {"video_id": 7, "channel_id": 7, "title": "Cybersecurity for Beginners | Google Cybersecurity Certificate", "views": 3919332, "likes": 19000},
    {"video_id": 8, "channel_id": 8, "title": "What does a Cloud Security Engineer do?", "views": 9940, "likes": 420},
    {"video_id": 9, "channel_id": 9, "title": "Cybersecurity Vs. Cloud Computing VS IT - Which is better for career & pay?", "views": 67236, "likes": 2700},
    {"video_id": 10, "channel_id": 10, "title": "Learn English with Movies | Will Smith - The Pursuit of Happyness", "views": 6254420, "likes": 222000},
    {"video_id": 11, "channel_id": 1, "title": "Roz 20min Ka Ye Rouhani Amal Karen | ALRA TV", "views": 348000, "likes": 11000},
    {"video_id": 12, "channel_id": 2, "title": "Qasida: Manam Adna | Sayyidi Younus AlGohar | ALRA TV", "views": 17000, "likes": 1100},
    {"video_id": 13, "channel_id": 3, "title": "SARKAR GOHAR SHAHI -KARACHI KHITAB - IJAZAT E ZIKR E QALB", "views": 159000, "likes": 3700},
    {"video_id": 14, "channel_id": 4, "title": "Syedna Gohar Shahi | UK | 1994", "views": 31000, "likes": 1100},
    {"video_id": 15, "channel_id": 5, "title": "Zainab ki Sana | Ep 10 - Imam Mehdi Gohar Shahi ka faiz | Ramadan 2024 | ALRA TV", "views": 2300, "likes": 376}
]
videos_collection.insert_many(videos)

# Insert data into Playlists collection
playlists = [
    {"playlist_id": 1, "channel_id": 1, "title": "Zikr e Qalb", "videos": 61},
    {"playlist_id": 2, "channel_id": 2, "title": "Qasida", "videos": 7},
    {"playlist_id": 3, "channel_id": 3, "title": "DEEN E EILAHI  URDU AUDIO", "videos": 17},
    {"playlist_id": 4, "channel_id": 4, "title": "NULL", "videos": "NULL"},
    {"playlist_id": 5, "channel_id": 5, "title": "Zainab ki Sana", "videos": 10},
    {"playlist_id": 6, "channel_id": 6, "title": "Azure SQL for beginners", "videos": 61},
    {"playlist_id": 7, "channel_id": 7, "title": "Google Cybersecurity Certificate", "videos": 15},
    {"playlist_id": 8, "channel_id": 8, "title": "Learn Cloud Computing", "videos": 24},
    {"playlist_id": 9, "channel_id": 9, "title": "How to Start A Cloud Career", "videos": 12},
    {"playlist_id": 10, "channel_id": 10, "title": "Learn English with Movies", "videos": 107}
]
playlists_collection.insert_many(playlists)

# Insert data into Comments collection
comments = [
    {"comment_id": 1, "video_id": 1, "user_name": "pathoflove4468", "comment_text": "Wah Subhan Allah"},
    {"comment_id": 2, "video_id": 2, "user_name": "IqraIram-mu9qo", "comment_text": "The greatest sufi master Younus Algohar"},
    {"comment_id": 3, "video_id": 3, "user_name": "FollowerofImamMehdi", "comment_text": "What a point! When you are in the fold of true rapturous love, you don''t need to dance or sing physically to show that love - for every fiber of your being is already dancing in the Lord''s love"},
    {"comment_id": 4, "video_id": 4, "user_name": "NULL", "comment_text": "NULL"},
    {"comment_id": 5, "video_id": 5, "user_name": "ghulammurtaza993", "comment_text": "wah kiya baat ha haq"},
    {"comment_id": 6, "video_id": 6, "user_name": "NULL", "comment_text": "NULL"},
    {"comment_id": 7, "video_id": 7, "user_name": "XinYell", "comment_text": "Lovely to see a company like Google creating educational resources"},
    {"comment_id": 8, "video_id": 8, "user_name": "deborahquaye-nu4kn", "comment_text": "Thanks for sharing Caleb."},
    {"comment_id": 9, "video_id": 9, "user_name": "JuanRodriguez-qk4oi", "comment_text": "Been waiting for this one!!"},
    {"comment_id": 10, "video_id": 10, "user_name": "learnenglishwithsmitha8371", "comment_text": "Will Smith is such a great actor. I absolutely love watching his movies."}
]
comments_collection.insert_many(comments)
