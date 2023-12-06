from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class face_recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
      
        img= Image.open(r"Python\Images\logo-9.png")
        img= img.resize((500,130),Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)
      
      
      
      
      
        
if __name__=="__main__":
    root= Tk()
    obj= face_recognition(root)
    root.mainloop()