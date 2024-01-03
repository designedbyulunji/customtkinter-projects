import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube

# LOGIC
def download_video():
  url = entry_widget.get()
  resolutions = resolutions_var.get()

  try:
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(res = resolutions).first()

    stream.download()

  except Exception as e:
    pass


  progress_label.pack()
  status_label.pack()

def on_progress(stream, chunk, bytes_remaining):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  perctage_completed = bytes_downloaded / total_size * 100
  
  print(perctage_completed)

# ROOT WINDOW
root_window = ctk.CTk()

# SYSTEM SETTINGS
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# WINDOW TITLE
root_window.title("YouTube Video Downloader")

# SET MAX SCREEN DIMENSIONS
root_window.minsize(720, 480)
root_window.maxsize(1080, 720)
root_window.geometry("720x480")

# MAIN FRAME
main_frame = ctk.CTkFrame(master=root_window)
main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)

# LABEL WIDGET
url_label = ctk.CTkLabel(master=main_frame, text="Enter YouTube URL",
                         font=ctk.CTkFont("roboto", size=18))
url_label.pack(pady=(0, 10))

# ENTRY WIDGET
entry_widget = ctk.CTkEntry(master=main_frame, width=500, height=30)
entry_widget.pack(pady=(0, 10))

# DOWNLOAD BUTTON
download_button = ctk.CTkButton(master=main_frame, text="Download", command=download_video)
download_button.pack(pady=(10,0))

# COMBOBOX
resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
resolutions_var = ctk.StringVar()
resolutions_combobox = ttk.Combobox(master=main_frame, values=resolutions, textvariable=resolutions_var)
resolutions_combobox.pack(pady=(10,10))
resolutions_combobox.set("1080px")

# PROGRESS BAR WIDGET
progress_label =  ctk.CTkLabel(master=main_frame, text="0%",
                         font=ctk.CTkFont("roboto", size=18))

progress_bar =  ctk.CTkProgressBar(master=main_frame, width=500)
progress_bar.set(0.2)
progress_bar.pack(pady=(10,10))

# STATUS LABEL
status_label =  ctk.CTkLabel(master=main_frame, text="Download complete!",
                         font=ctk.CTkFont("roboto", size=18))

# RUN APP
root_window.mainloop()