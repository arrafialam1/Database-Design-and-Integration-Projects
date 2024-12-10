import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='tc7@3*G5h9Bx%W%',
                              host='localhost',
                              port='5432',
                              database='Test')
cursor = connection.cursor()

# Count of rows of each table
tables = ['Channels', 'Videos', 'Playlists', 'Comments']
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"Count of rows in {table}: {count}")

# Show a sample of 3 rows from each table
tables = ['Channels', 'Videos', 'Playlists', 'Comments']
for table in tables:
    cursor.execute(f"SELECT * FROM {table} LIMIT 3")
    rows = cursor.fetchall()
    print(f"Sample rows from {table}:")
    for row in rows:
        print(row)

# Left Join
print("\nLeft Join Result:")
cursor.execute("""
    SELECT Videos.video_id, Videos.title, Channels.channel_name
    FROM Videos
    LEFT JOIN Channels ON Videos.channel_id = Channels.channel_id
""")
left_join_result = cursor.fetchall()
for row in left_join_result:
    print(row)

# Close cursor and connection

cursor.close()
connection.close()
