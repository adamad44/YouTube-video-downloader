import os
import tkinter as tk
from tkinter import filedialog
import threading
import time
import subprocess
from pytube import YouTube

# Create the main application window
root = tk.Tk()
root.title('YouTube Video Downloader')
root.config(bg='#12171C')

# Function to initiate the video download
def click():
    threading.Thread(target=main_download_video).start()

# Function to download the video
def main_download_video():
    try:
        # Ask the user to select a directory for the video download
        ask_open = filedialog.askdirectory(initialdir=os.getcwd())
        selected_file = ask_open

        # Disable the download button and update the UI
        download_button.config(text='This won\'t take too long...', state=tk.DISABLED)
        root.update()

        # Get the YouTube URL from the entry widget
        url = str(link_entry.get())

        # Download the video with the highest resolution available to the selected directory
        video = YouTube(url)
        video.streams.get_highest_resolution().download(output_path=selected_file)

        # Enable the download button and update the UI
        download_button.config(text='Download', state=tk.NORMAL)
        root.update()

        # Open the file explorer with the downloaded video selected
        abc = os.path.join(str(selected_file), f"{video.title}.mp4")
        subprocess.Popen(f'explorer /select,"{abc}"')
    except Exception as e:
        print(e)
        # Show an error message on the download button and update the UI
        download_button.config(text='ERROR', fg='red', state=tk.NORMAL)
        root.update()
        time.sleep(1)
        download_button.config(text='Download', state=tk.NORMAL)

# Create the main title label
title = tk.Label(root, text='YouTube to MP4 Converter', font='Helvetica 30 bold', bg='#12171C', fg='#758A9B')
title.pack(pady=20)

# Create a subtitle label
subtitle1 = tk.Label(root, text='Download YouTube videos in mp4 format for offline watching', bg='#12171C', fg='#758A9B', font='Helvetica 12')
subtitle1.pack()

# Create an entry widget for the user to input the YouTube URL
link_entry = tk.Entry(root, bg='#12171C', fg='#758A9B', font='Helvetica 16', width=50, bd=0, highlightthickness=2, highlightbackground='#758A9B')
link_entry.pack(pady=20)

# Create the download button
download_button = tk.Button(root, text='Download', command=click, bg='#758A9B', fg='#12171C', font='Helvetica 16 bold', relief=tk.FLAT)
download_button.pack(pady=10)

# Start the main event loop
root.mainloop()
