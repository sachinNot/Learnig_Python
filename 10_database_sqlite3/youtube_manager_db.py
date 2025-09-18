import sqlite3

# connect to DB (or create if not exists)
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL         
    )
''')

# list videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# add video
def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?, ?)", (name, time))
    conn.commit()

# update video
def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, video_id))
    conn.commit()

# delete video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()

# main app loop
def main():
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    # close DB after loop ends
    conn.close()


if __name__ == "__main__":
    main()
