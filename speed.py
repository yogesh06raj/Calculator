import customtkinter as ctk
import random
import time

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "This can be accomplished using one or both thumbs.",
    "Driving from own state to nearby states would help to expand our limited funds.",
    "Some people combine touch typing and hunt and peck by using a buffering method.",
    "Editing is a growing field of work in the service industry."
]

def start_test():
    global text
    text = random.choice(texts)
    text2.configure(text=text)
    
    entry.delete(0, "end")
    btn1.configure(state="disabled")
    entry.configure(state="normal")
    
    entry.focus()
    global start_time
    start_time = time.time()

def end_test(event):
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    typed_text = entry.get()
    
    accuracy = 0
    for i in range(min(len(text), len(typed_text))):
        if text[i] == typed_text[i]:
            accuracy += 1
    accuracy = (accuracy / len(text)) * 100
    
    speed = (len(typed_text) / 5) / (elapsed_time / 60)
    
    time_label.configure(text=f"Time: {elapsed_time:.2f} seconds")
    acuracy.configure(text=f"Accuracy: {accuracy:.2f} %")
    Speed.configure(text=f"Speed: {speed:.2f} words per minute")
    
    btn1.configure(state="disabled")
    btn2.configure(state="normal")
    entry.configure(state="disabled")

app=ctk.CTk()


frame= ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="both", expand=True)

heading=ctk.CTkLabel(frame, text="Type the text below as fast and accurate as you can and press Enter when done.", bg_color="cyan", text_color="red")
heading.pack(padx=10, pady=10)

text2=ctk.CTkLabel(frame, text="")
text2.pack(padx=10, pady=10)

entry=ctk.CTkEntry(frame, width=400)
entry.pack(padx=10, pady=20)
entry.bind("<Return>", end_test)
entry.configure(state="disabled")

btn1=ctk.CTkButton(frame, text="Start", command=start_test)
btn1.pack(pady=10)
btn2=ctk.CTkButton(frame, text="ReStart", command=start_test)
btn2.pack(pady=10)


frame2= ctk.CTkFrame(app)
frame2.pack(fill="both", expand=True, padx=10, pady=5)

time_label = ctk.CTkLabel(frame2, text="")
time_label.pack(pady=10)
acuracy = ctk.CTkLabel(frame2, text="")
acuracy.pack(pady=10)
Speed = ctk.CTkLabel(frame2, text="")
Speed.pack(pady=10)


app.mainloop()