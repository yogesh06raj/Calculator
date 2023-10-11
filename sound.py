import customtkinter as ctk
import tkinter.messagebox
import sounddevice as sd
import soundfile as sf
import time
import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")




def record_voice():
    file_name = entry.get()
    if not file_name:
        tkinter.messagebox.showinfo("Error", "Please enter file name")
        return

    fs = 44100
    duration = 10

    voice_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
 
    progress_label.configure(text="Recording...")

    sd.wait()
    sf.write(file_name + ".wav", voice_data, fs)

    progress_label.configure(text="Recording saved as " + file_name + ".wav")
    
app = ctk.CTk()
app.title("Voice Recorder")
app.geometry("350x200")

label = ctk.CTkLabel(app, text="Enter a file name:")
label.grid(pady=10, row=0, column=0)

entry = ctk.CTkEntry(app, placeholder_text="Your file name")
entry.grid(row=0,column=1)


button = ctk.CTkButton(app, text="Record", command=record_voice)
button.grid(pady=10, padx=10, row=1, column=0)

progress_label = ctk.CTkLabel(app, text="")
progress_label.grid(pady=10, padx=10)


app.mainloop()
