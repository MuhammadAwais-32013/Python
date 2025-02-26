import sqlite3

con=sqlite3.connect('youtube_manager.db')
cursor=con.cursor()

cursor.execute('''
    create table  if not exists video ( 
    id integer primary key,
    name text not null,         
    duration text not null ,        
    language text not null         
   )            
''')  

              
def list_videos():
   cursor.execute('select * from video')
   con.commit()
   for video in cursor.fetchall():
       print(video)
def add_video(name,duration, language):
    cursor.execute('insert into video (name, duration, language) values(?,?,?)',(name,duration,language))
    con.commit()
        
            
def update_video(Vid,name,duration, language):
    cursor.execute('update  video set name=?, duration=?, language=? where id=?',(name,duration,language,Vid))
    con.commit()
def del_video(id):
     cursor.execute('delete from video where id=?',(id,))
     con.commit()
        

def main():
    # videos=
    while True:
        print(" Well Come to youtube manager ")
        print('1. List all videos ')
        print('2. Add  video')
        print('3. Update video ')
        print('4. Delete video ')
        print('5. Exit ')
        
        choice=int(input('Enter your choice: '))
        
        match choice:
            case 1:
                list_videos()
            case 2:
                name = input("Enter the video name: ")
                duration = input("Enter the video time: ")
                language = input("Enter the video language: ")
                add_video(name,duration, language)
            case 3:
                list_videos()
                V_id = int(input("Enter the video id: "))
                name = input("Enter the video name: ")
                duration = input("Enter the video time: ")
                language = input("Enter the video language: ")
                update_video(V_id,name,duration, language)
            case 4:
                list_videos()
                V_id = input("Enter the video id to delete: ")
                del_video(V_id)
            case 5:
                break
            case _:
                print('Invalid Choice')

if __name__=='__main__':
    main()