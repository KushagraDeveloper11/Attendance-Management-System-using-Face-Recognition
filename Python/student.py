from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1270x636+0+0")
        # self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #Logo
        img= Image.open(r"Python\Images\logo-9.png")
        img= img.resize((425,100), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)
      
        f_label= Label(self.root, image= self.photoimg)
        f_label.place(x=0, y=0, width=425, height= 100)
        
        #Image 1
        img1= Image.open(r"Python\Images\logo-9.png")
        img1= img1.resize((425,100), Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
      
        f_label= Label(self.root, image= self.photoimg1)
        f_label.place(x=425, y=0, width=425, height= 100)
        
        #Image 2
        img2= Image.open(r"Python\Images\logo-9.png")
        img2= img2.resize((425,100), Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
      
        f_label= Label(self.root, image= self.photoimg2)
        f_label.place(x=850, y=0, width=425, height= 100)
        
         #Bg Image
        img3= Image.open(r"Python\Images\logo-9.png")
        img3= img3.resize((1270,600), Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
      
        bg_img= Label(self.root, image= self.photoimg3)
        bg_img.place(x=0, y=100, width=1270, height= 600)
        
        title_lbl= Label(bg_img, text="STUDENT DETAILS", font=("times new roman", 35, "bold"), bg="black", fg= "green")
        title_lbl.place(x=0, y=0, width=1270, height= 50)
        
        main_frame= Frame(bg_img, bd=2)
        main_frame.place(x=0, y=50, width= 1270, height= 600)
        
if __name__=="__main__":
    root= Tk()
    obj= Student(root)
    root.mainloop()