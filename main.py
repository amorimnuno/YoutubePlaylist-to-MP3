from pytube import YouTube
import os


def download_youtube_audio(url):

    try:

        yt = YouTube(url)
        fileName = yt.title
        mp3_filename = f"{fileName}.mp3"
        if os.path.exists(fileName):
            print(f"File '{fileName}' already exists. Deleting...")
            os.remove(fileName)
            print(f"Existing file deleted.")

        output_file = yt.streams.filter(only_audio=True).first().download(filename=fileName)
        os.rename(output_file, mp3_filename)

        print(f"Successfully downloaded: {mp3_filename}")

    except Exception as e:

        print(f"An error occurred: {str(e)}")

url = input("Enter YouTube URL: ")
download_youtube_audio(url)

print("Done")
input("Press Enter to Exit")
