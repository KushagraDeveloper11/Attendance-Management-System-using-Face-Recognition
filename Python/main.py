from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1270x636+0+0")
        # self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
      
        #Logo
        img= Image.open(r"Python/Images/logo-9.png")
        img= img.resize((200,100), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)
      
        f_label= Label(self.root, image= self.photoimg)
        f_label.place(x=0, y=0, width=200, height= 100)
        
        #Image 1
        img1= Image.open(r"Python/Images/background2.png")
        img1= img1.resize((425,100), Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
      
        f_label= Label(self.root, image= self.photoimg1)
        f_label.place(x=200, y=0, width=1080, height= 100)
        
        # Image 2
        img2= Image.open(r"Python/Images/background2.png")
        img2= img2.resize((425,100), Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
      
        f_label= Label(self.root, image= self.photoimg2)
        f_label.place(x=850, y=0, width=425, height= 100)
      
        #Bg Image
        img3= Image.open(r"Python/Images/background.jpg")
        img3= img3.resize((1270,600), Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
      
        bg_img= Label(self.root, image= self.photoimg3)
        bg_img.place(x=0, y=100, width=1270, height= 600)
        
        title_lbl= Label(bg_img, text="SMART ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="black", fg= "green")
        title_lbl.place(x=0, y=0, width=1270, height= 50)

        #student-button
        bimg= Image.open(r"Python/Images/student-details.jpg")
        bimg= bimg.resize((200,120), Image.LANCZOS)
        self.photobimg= ImageTk.PhotoImage(bimg)
        
        b1= Button(bg_img, image=self.photobimg, cursor="hand2")
        b1.place(x=100, y=100, width=200, height=120)
        
        b1_1= Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_1.place(x=100, y=220, width=200, height=30)
        
        #Detect Face
        fimg= Image.open(r"Python/Images/detect-face.png")
        fimg= fimg.resize((120,120), Image.LANCZOS)
        self.photoimgf= ImageTk.PhotoImage(fimg)
        
        b2= Button(bg_img, image=self.photoimgf, cursor="hand2")
        b2.place(x=100, y=300, width=200, height=120)
        
        b2_1= Button(bg_img, text="Detect Face", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b2_1.place(x=100, y=420, width=200, height=30)
        
        #Attendance
        Aimg= Image.open(r"Python/Images/attendance.jpg")
        Aimg= Aimg.resize((120,120), Image.LANCZOS)
        self.photoimgA= ImageTk.PhotoImage(Aimg)
        
        b3= Button(bg_img, image=self.photoimgA, cursor="hand2")
        b3.place(x=400, y=300, width=200, height=120)
        
        b3_1= Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b3_1.place(x=400, y=420, width=200, height=30)
        
        #Help-button
        Himg= Image.open(r"Python/Images/help.png")
        Himg= Himg.resize((120,120), Image.LANCZOS)
        self.photoHimg= ImageTk.PhotoImage(Himg)
        
        bH= Button(bg_img, image=self.photoHimg, cursor="hand2")
        bH.place(x=400, y=100, width=200, height=120)
        
        b1_H= Button(bg_img, text="Guide", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_H.place(x=400, y=220, width=200, height=30)
        
        #Train-button
        Timg= Image.open(r"Python/Images/train-data-1.png")
        Timg= Timg.resize((120,120), Image.LANCZOS)
        self.photoTimg= ImageTk.PhotoImage(Timg)
        
        tH= Button(bg_img, image=self.photoTimg, cursor="hand2")
        tH.place(x=700, y=100, width=200, height=120)
        
        b1_T= Button(bg_img, text="Train", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_T.place(x=700, y=220, width=200, height=30)
        
        #Button-1
        img_1= Image.open(r"Python/Images/developer.png")
        img_1= img_1.resize((200,120), Image.LANCZOS)
        self.photoimg_1= ImageTk.PhotoImage(img_1)
        
        b11= Button(bg_img, image=self.photoimg_1, cursor="hand2")
        b11.place(x=1000, y=100, width=200, height=120)
        
        b1_11= Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_11.place(x=1000, y=220, width=200, height=30)
        
        #Button-2
        img_2= Image.open(r"Python/Images/user-guide.png")
        img_2= img_2.resize((120,120), Image.LANCZOS)
        self.photoimg_2= ImageTk.PhotoImage(img_2)
        
        b22= Button(bg_img, image=self.photoimg_2, cursor="hand2")
        b22.place(x=700, y=300, width=200, height=120)
        
        b1_22= Button(bg_img, text="Guide", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_22.place(x=700, y=420, width=200, height=30)
        
        #Button-3
        img_3= Image.open(r"Python/Images/photos.png")
        img_3= img_3.resize((120,120), Image.LANCZOS)
        self.photoimg_3= ImageTk.PhotoImage(img_3)
        
        b_3= Button(bg_img, image=self.photoimg_3, cursor="hand2")
        b_3.place(x=1000, y=300, width=200, height=120)
        
        b1_33= Button(bg_img, text="Guide", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg= "white")
        b1_33.place(x=1000, y=420, width=200, height=30)
        
if __name__=="__main__":
    root= Tk()
    obj= Face_Recognition(root)
    root.mainloop()