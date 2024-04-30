import  customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import  os

def download_video():
    url=url_input.get()
    resolution=resolution_var.get()
    
    progress_label.pack(padx=10,pady=10)
    progress_bar.pack(padx=10,pady=10)
    status_label.pack(padx=10,pady=10)
    
    try:
        yt=YouTube(url,on_progress_callback=on_progress)
        stream=yt.streams.filter(res=resolution).first()
        os.path.join("downloads",f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        status_label.configure(text="Downloaded ", text_color="white",fg_color="green")
    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white",fg_color="red")
    
    
def on_progress(stream,chunk,byte_remaining):
    total_size=stream.filesize
    byte_downloaded=total_size-byte_remaining
    percentage_completed= byte_downloaded/total_size*100
    
    progress_label.configure(text=str(int(percentage_completed))+"%")
    progress_label.update()
    
    progress_bar.set(float(percentage_completed/100))
    
# create root window
root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Title of the window

root.title("Youtube Video Downloader")

# set min and nax widht and height
root.geometry("720x480")
root.minsize(720,480)
root.maxsize(1080,720)

# create a frame
content_frame=ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH,expand=True,padx=10,pady=10)

# create label and the input box for url

url_label=ctk.CTkLabel(content_frame,text="Enter the youtube url here : ")
url_input=ctk.CTkEntry(content_frame,width=400,height=40)
url_label.pack(pady=10,padx=10)
url_input.pack(pady=10,padx=10)


# create a download button

download_btn=ctk.CTkButton(content_frame,text="Download", command=download_video)
download_btn.pack(pady=20,padx=20)

# create a resolution combo box
resolutions=["720p","360p","240p"]
resolution_var=ctk.StringVar()
resolution_combobox=ttk.Combobox(content_frame,values=resolutions,textvariable=resolution_var)
resolution_combobox.pack(pady=10,padx=20)
resolution_combobox.set("720p")

# create a label and the progress bar to display the download progress 
progress_label=ctk.CTkLabel(content_frame,text="0%")

progress_bar=ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)


# create  a status label
status_label=ctk.CTkLabel(content_frame,text="")




# to run the app
root.mainloop()