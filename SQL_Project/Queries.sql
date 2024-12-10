-- Dropping existing tables to avoid conflicts
DROP TABLE IF EXISTS Comments, Videos, Playlists, Channels;

-- Creating Channels table
CREATE TABLE Channels (
    channel_id INT PRIMARY KEY,
    channel_name VARCHAR(255),
    description TEXT,
    total_videos INT,
    subscribers BIGINT
);

-- Inserting records into the Channels table
INSERT INTO Channels (channel_id, channel_name, description, total_videos, subscribers)
VALUES 
(1, 'ALRA TV', 'ALRA TV serves as the official YouTube channel of the esteemed Universal Sufi Order, helmed by the revered Sufi Master Younus AlGohar', 2760, 1300000), 
(2, 'ALRA TV CLIPS', 'Official clips and highlights channel, owned and operated by the ALRA TV team', 69, 6230), 
(3, 'Sufi Library', 'This channel is aimed at providing the world with the speeches of His Holiness Younus AlGohar, the Representative of Imam Mehdi, Messiah & Kalki Avatar and the CEO of Messiah Foundation International', 130, 28600),
(4, 'Paigham e Gohar', 'This channel is dedicated for spreading the message of Divine Love as per teachings of His Holiness Riaz Ahmed Gohar Shahi, who is a world renowned spiritual personality', 346, 12500),
(5, 'Mehdi Foundation India Official', 'Video contents to spread the mission of Imam Mehdi Sarkar Gohar Shahi', 100, 3030),
(6, 'Microsoft Azure', 'Microsoft Azure discussion and knowledge hub', 1400, 315000),
(7, 'Google Career Certificates', 'Preparing you for entry-level roles in growing career paths', 803, 418000),
(8,'Caleb Oni. Certified', 'Just a Cloud Security Engineer documenting my career progress, helping people on the way!', 115, 9340),
(9,'Nicole Enesse', 'What I wish I had known when I started my career in tech', 146, 59300),
(10, 'Learn English With TV Series', 'On this channel, we will practice and improve our listening comprehension, using your favorite TV shows, movies, and talk shows', 501, 8970000);

-- Creating Videos table
CREATE TABLE Videos (
    video_id INT PRIMARY KEY,
    channel_id INT,
    title VARCHAR(255),
    views INT,
    likes INT,
    FOREIGN KEY (channel_id) REFERENCES Channels(channel_id)
);

-- Inserting records into the Videos table
INSERT INTO Videos (video_id, channel_id, title, views, likes) VALUES
(1, 1, 'Zikr e Qalb Kya Hai? | Younus AlGohar | ALRA TV', 443543, 4500),
(2, 2, 'The Religion of God (English Voiceover)', 1476, 189),
(3, 3, 'YOUNUS ALGOHAR Jashan-e-Shahi Speech, Karachi 1999', 10758, 925),
(4, 4, 'Image Of Imam Mehdi (A.S) On Moon (Wajah Imam Mahdi di Bulan)', 812735, 2100),
(5, 5, 'HH Younus AlGohar Nepal visit Nov 2018 Highlights', 7899, 664),
(6, 6, 'How does Microsoft Azure work?', 779900, 6500),
(7, 7, 'Cybersecurity for Beginners | Google Cybersecurity Certificate', 3919332, 19000),
(8, 8, 'What does a Cloud Security Engineer do?', 9940, 420),
(9, 9, 'Cybersecurity Vs. Cloud Computing VS IT - Which is better for career & pay?', 67236, 2700),
(10, 10, 'Learn English with Movies | Will Smith - The Pursuit of Happyness', 6254420, 222000),
(11, 1, 'Roz 20min Ka Ye Rouhani Amal Karen | ALRA TV', 348000, 11000),
(12, 2, 'Qasida: Manam Adna | Sayyidi Younus AlGohar | ALRA TV', 17000, 1100),
(13, 3, 'SARKAR GOHAR SHAHI -KARACHI KHITAB - IJAZAT E ZIKR E QALB', 159000, 3700),
(14, 4, 'Syedna Gohar Shahi | UK | 1994', 31000, 1100),
(15, 5, 'Zainab ki Sana | Ep 10 - Imam Mehdi Gohar Shahi ka faiz | Ramadan 2024 | ALRA TV', 2300, 376),
(16, 6, 'Introducing Azure Cosmos DB', 51000, 325),
(17, 7, 'What are the 8 Cybersecurity Domains? | Google Cybersecurity Certificate', 3200, 144),
(18, 8, 'From No Experience to Cloud Engineer | Step by Step Roadmap (2024)', 99000, 4000),
(19, 9, '2024 Cybersecurity Full roadmap: How to get started as a beginner?', 304000, 11000),
(20, 10, 'Learn English with BETTER CALL SAUL', 102000, 4200),
(21, 1, 'Pul e Sirat Ka Raaz | Younus AlGohar | ALRA TV', 1700000, 15000);

-- Creating Playlists table
CREATE TABLE Playlists (
    playlist_id INT PRIMARY KEY,
    channel_id INT,
    title VARCHAR(255),
    videos INT,
    FOREIGN KEY (channel_id) REFERENCES Channels(channel_id)
);

-- Inserting data into Playlists table
INSERT INTO Playlists (playlist_id, channel_id, title, videos) VALUES
(1, 1, 'Zikr e Qalb', 61),
(2, 2, 'Qasida', 7),
(3, 3, 'DEEN E EILAHI  URDU AUDIO', 17),
(4, 4, NULL, NULL),
(5, 5, 'Zainab ki Sana', 10),
(6, 6, 'Azure SQL for beginners', 61),
(7, 7, 'Google Cybersecurity Certificate', 15),
(8, 8, 'Learn Cloud Computing', 24),
(9, 9, 'How to Start A Cloud Career', 12),
(10, 10, 'Learn English with Movies', 107);

-- Creating Comments table
CREATE TABLE Comments (
    comment_id INT PRIMARY KEY,
    video_id INT,
    user_name VARCHAR(255),
    comment_text TEXT,
    FOREIGN KEY (video_id) REFERENCES Videos(video_id)
);

-- Inserting data into Comments table
INSERT INTO Comments (comment_id, video_id, user_name, comment_text) VALUES
(1, 1, 'pathoflove4468', 'Wah Subhan Allah'),
(2, 2, 'IqraIram-mu9qo', 'The greatest sufi master Younus Algohar'),
(3, 3, 'FollowerofImamMehdi', 'What a point! When you are in the fold of true rapturous love, you don''t need to dance or sing physically to show that love - for every fiber of your being is already dancing in the Lord''s love'),
(4, 4, NULL, NULL),
(5, 5, 'ghulammurtaza993', 'wah kiya baat ha haq'),
(6, 6, NULL, NULL),
(7, 7, 'XinYell', 'Lovely to see a company like Google creating educational resources'),
(8, 8, 'deborahquaye-nu4kn', 'Thanks for sharing Caleb.'),
(9, 9, 'JuanRodriguez-qk4oi', 'Been waiting for this one!!'),
(10, 10, 'learnenglishwithsmitha8371', 'Will Smith is such a great actor. I absolutely love watching his movies.');
