from typing import Optional, Tuple, Union
import customtkinter
import tkinter
from PIL import ImageTk,Image
import os
import ctypes
import sqlite3
from cryptography.fernet import Fernet

ctypes.windll.shcore.SetProcessDpiAwareness(2) # windows version should >= 8.1

class App(customtkinter.CTkToplevel):
    
    APP_NAME = "ByahePH"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.encoding = "utf-8"

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "bphData.db")
        self.con = sqlite3.connect(self.db_path)
        self.c = self.con.cursor()

        self.c.execute("SELECT * FROM KEY")
        key_table = self.c.fetchall()
        key = key_table[0][0]
        self.cipher_suit = Fernet(bytes(key, self.encoding))
        self.app_Width = 500
        self.app_Height = 650
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.CenterX = int((self.screen_width-self.app_Width)/2) #-200
        self.CenterY = int((self.screen_height-self.app_Height)/2) #-200

        self.title((App.APP_NAME))
     
        self.width = int(self.winfo_screenwidth()/2.5)
        self.height = int(self.winfo_screenheight()/2)
        self.geometry(f"{self.width}x{self.height})")
        self.minsize(500,500)
        self.bind("<1>", lambda event: event.widget.focus_set())
        self.iconpath=customtkinter.CTkImage(light_image=Image.open(os.path.join(self.BASE_DIR, 'images', 'jeep.ico')))
        self.wm_iconbitmap()
        self.iconphoto(False, ImageTk.PhotoImage(self.iconpath._light_image)) 

        self.geometry(f'{self.app_Width}x{self.app_Height}+{self.CenterX}+{self.CenterY}')
        self.minsize(width=self.app_Width, height=self.app_Height)
        self.maxsize(width=self.screen_width, height=self.screen_height)
        self.lift()
        self.grab_set()
    
        self.font1= ('Arial',19,'bold')
        self.font2= ('Arial',11)
        self.font3= ('Arial',14,'underline')
        self.font4= ('Arial',13.5)

        #import background
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.img1= customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'images', 'map.png')), size=(1920,1080))
        self.submit_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path,'images', 'arrow-right.png')), size=(25,25))
        self.logo_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path,'images', 'icon.png')), size=(100,100))
        self.back_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path,'images', 'arrow-left.png')), size=(25,25))
        self.bg=customtkinter.CTkLabel(master=self,image=self.img1, text="")
        self.bg.pack()

        #BG FRAME ----------
        self.steady=customtkinter.CTkFrame(master=self.bg, width=356, height=600, corner_radius=18)
        self.steady.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # FRAME 1 --------------------

        self.frame1=customtkinter.CTkFrame(master=self.bg, width=356, height=600, corner_radius=18)
        self.frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.logo = customtkinter.CTkLabel(self.frame1,image=self.logo_img, text="")
        self.logo.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)

        self.loginsignup_label=customtkinter.CTkLabel(self.frame1,font=self.font1,text='Admin Sign in',text_color='#fff')
        self.loginsignup_label.place(relx=0.5, rely=0.28, anchor=tkinter.CENTER)

        self.loginuser_entry=customtkinter.CTkEntry(self.frame1,text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Username",placeholder_text_color='#18191A',width=230,height=30)
        self.loginuser_entry.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)

        self.loginpass_entry=customtkinter.CTkEntry(self.frame1,show='*',text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Password",placeholder_text_color='#18191A',width=230,height=30)
        self.loginpass_entry.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)

        self.login_button= customtkinter.CTkButton(self.frame1, font=self.font4,text_color='#d3d3d3',cursor='hand2', width=50, height=50, image=self.submit_img, text="", corner_radius=10, command=self.login)
        self.login_button.place(relx=0.5, rely=0.72, anchor=tkinter.CENTER)

        self.loginerror=customtkinter.CTkLabel(self.frame1,font=self.font3,text='',text_color='#f00', height=10, bg_color="transparent")
        self.loginerror.place(relx=0.5, rely=0.36, anchor=tkinter.CENTER)

        self.frame1.place()

        self.access = False

    def login(self):
        if self.loginuser_entry.get() and self.loginpass_entry.get():
            Login_name = self.loginuser_entry.get()
            Login_pass = self.loginpass_entry.get()
            self.c.execute("SELECT * FROM ACCOUNT WHERE USER = ?", (Login_name,))
            login_query = self.c.fetchall()
            if login_query:
                if login_query[0][2] == Login_name and self.cipher_suit.decrypt(login_query[0][3]) == bytes(Login_pass, self.encoding):
                    if int(login_query[0][4]) == 1:
                        self.access=True
                        self.destroy()
                    else:
                       self.loginerror.configure(text="Access Denied") 
                else:
                    self.loginerror.configure(text="Wrong username or password")
            else:
                self.loginerror.configure(text="Wrong username or password")
        else:
            self.loginerror.configure(text="Please fill up missing blanks.")
        pass

    def start(self):
        App().mainloop()

    def get_input(self):
        self.master.wait_window(self)
        return self.access