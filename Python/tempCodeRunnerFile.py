img= Image.open(r"Python\Images\logo-9.png")
        img= img.resize((425,100), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)
      
        f_label= Label(self.root, image= self.photoimg)
        f_label.place(x=0, y=0, width=425, height= 100)