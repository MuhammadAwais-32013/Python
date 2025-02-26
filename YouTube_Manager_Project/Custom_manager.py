import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            content=file.read()
            if not content:
                return []
            else:
                return json.loads(content)
    except FileNotFoundError:
        return []
 
def save_data(video)->bool:
        try:
            with open('youtube.txt', 'w') as file:
                json.dump(video,file)
                return True
        except FileNotFoundError:
            return False
              
def list_videos(videos):
    print('\n')
    print("*" * 80)
    for key, video in enumerate(videos, start=1):
        print(f"{key}. Name: {video['name']} Duration: {video['duration']} Language: {video['language']}  ")
    print("*" * 80)
    print('\n') 
def add_video(video):
    name=input('Enter video name: ')
    duration=input('Enter video duration: ')
    language=input('Enter video language: ')
    
    video.append({'name':name, 'duration':duration, 'language':language})
    if(save_data(video)):
        print('\n')
        print('*' * 50)
        print('Data Sucessfully Update Press 1 To check ')
        print('*' * 50)
        print('\n')
            
def update_video(video):
    list_videos(video)
    index = int(input("Enter the video number to update : "))
    if 1<=index <= len(video):
        name = input("Enter the new video name : ")
        duration = input("Enter the new video time : ")
        language = input("Enter the new video language : ")
        video[index-1]={'name':name, 'duration':duration,'language':language}
        if(save_data(video)):
            print('\n')
            print('*' * 50)
            print('Data Sucessfully Update Press 1 To check ')
            print('*' * 50)
            print('\n')
    else:
        print('invalid video number')

def del_video(video):
    
    list_videos(video)
    index = int(input("Enter the video number to Delete : "))
    if 1<=index <= len(video):
      del video[index -1]
      if(save_data(video)):
            print('\n')
            print('*' * 50)
            print('Data Sucessfully Deleted Press 1 To check ')
            print('*' * 50)
            print('\n')  
    else:
        print('invalid video number')
        

def main():
    videos=load_data()
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
                list_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                del_video(videos)
            case 5:
                break
            case _:
                print('Invalid Choice')

if __name__=='__main__':
    main()