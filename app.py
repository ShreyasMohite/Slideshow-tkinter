from tkinter import *
from PIL import Image
import tkinter.messagebox
from PIL import ImageTk
from PIL import *
from tkinter import filedialog
import threading
from tkinter.ttk import Combobox
from PIL import ImageFilter
from os import listdir
import os
import time





class Img_filter:
    def __init__(self,root):
        self.root=root
        self.root.title("Image Slideshow")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo733.ico")
        self.root.resizable(0,0)





        def browse():
            try:

                global filename
                global photo_image
                file_path=tkinter.filedialog.askdirectory(title="choose folder")
                filename =file_path
                
            except Exception as e:
                print(e)
                tkinter.messagebox.showerror("Error","Please Use Images only")
     

       
        start=0
        def slideshow():          
            try:
                nonlocal start             
                extensions=('.png','.jpg')
                imgs=[]
                for fname in os.listdir(filename):
                    if not fname.endswith(extensions):
                        continue
                    imgs.append(fname)
                length_of_imgs=len(imgs)
                for x in range(length_of_imgs):
                    
                    if start==length_of_imgs:
                        start=0
                    img=filename+"/"+imgs[start]
                    self.original = Image.open(img)
                    resized = self.original.resize((355,180),Image.ANTIALIAS)
                    self.image = ImageTk.PhotoImage(resized)
                    photo_image=Label(firstframe,image=self.image,bd=2)
                    photo_image.place(x=65,y=65)
                start+=1
                root.after(2000,slideshow)          
            except Exception as e:
                print(e)
        
        slideshow()

      

        """
        start=0
        def hello():
            nonlocal start
            if start==4+1:
                start=0
            print(start)
            start+=1
            root.after(2000,hello)
        hello()
       """

        

   
        
       





        



        def on_enter1(e):
            but_convert_ascii['background']="black"
            but_convert_ascii['foreground']="cyan"  
        def on_leave1(e):
            but_convert_ascii['background']="SystemButtonFace"
            but_convert_ascii['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_Browse['background']="black"
            but_Browse['foreground']="cyan"  
        def on_leave3(e):
            but_Browse['background']="SystemButtonFace"
            but_Browse['foreground']="SystemButtonText"





        def clear():
            photo_image.config(image="")
            


#==========================frame=================================================#

        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=350,relief="ridge",bd=3,bg="black")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=45,relief="ridge",bd=3)
        secondframe.place(x=0,y=350)

#===========================firstframe==================================================#
        
        but_Browse=Button(firstframe,text="Browse",width=15,font=('times new roman',12),cursor="hand2",command=browse)
        but_Browse.place(x=170,y=10)
        but_Browse.bind("<Enter>",on_enter3)
        but_Browse.bind("<Leave>",on_leave3)


        global photo_image
        self.original = Image.open("C:/Users/SHREYAS/Desktop/shreyas python/img_ascii/black.png")
        resized = self.original.resize((355,180),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image=Label(firstframe,image=self.image,bd=2)
        photo_image.place(x=65,y=65)



        

    

#=========================secondframe==================================================#
        but_convert_ascii=Button(secondframe,width=18,text="Slide Show",font=('times new roman',12),cursor="hand2",command=slideshow)
        but_convert_ascii.place(x=40,y=5)
        but_convert_ascii.bind("<Enter>",on_enter1)
        but_convert_ascii.bind("<Leave>",on_leave1)

        but_clear=Button(secondframe,width=18,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=5)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)



        


   





if __name__ == "__main__":
    root=Tk()
    Img_filter(root)
    root.mainloop()
