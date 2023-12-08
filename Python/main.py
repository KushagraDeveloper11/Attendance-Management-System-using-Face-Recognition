from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
      
        img= Image.open(r"Python\Images\logo-9.png")
        img= img.resize((500,130), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)
      
        f_label= Label(self.root, image= self.photoimg)
        f_label.place(x=0, y=0, width=500, height= 150)
        
      
      
        
if __name__=="__main__":
    root= Tk()
    obj= Face_Recognition(root)
    root.mainloop()