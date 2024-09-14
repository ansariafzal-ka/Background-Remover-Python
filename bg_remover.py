import tkinter as tk
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog

def open_image():
    global input_path, user_img
    
    input_path = filedialog.askopenfilename(title="Open Image", filetypes=(("PNG Files", ".png"), ("All Files", "*.*")))
    
    if input_path:
        user_img = ImageTk.PhotoImage(Image.open(input_path))
        pic_label.config(image=user_img, bg="black")

def remove_background():
    output_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".png", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))

    
    input = Image.open(input_path)
    output = remove(input)
    
    output.save(output_path, "PNG")
    
    global user_img
    
    user_img = ImageTk.PhotoImage(Image.open(output_path))
    pic_label.config(image=user_img)

window = tk.Tk()

window.title("Background Remover")
window.geometry("500x700")

pic_label = tk.Label(window, text="")
pic_label.pack(pady=20)

open_btn = tk.Button(window, text="Open Image", command=open_image)
open_btn.pack(pady=20)

remove_btn = tk.Button(window, text="Remove Background", command=remove_background)
remove_btn.pack(pady=20)

window.mainloop()