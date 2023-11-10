from typing import Optional, Tuple, Union
import customtkinter
import tkinter
from PIL import ImageTk,Image
import os
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2) # windows version should >= 8.1

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.app_Width = 500
        self.app_Height = 650
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.CenterX = int((self.screen_width-self.app_Width)/2)
        self.CenterY = int((self.screen_height-self.app_Height)/2)

        self.title("Byahe PH")
        self.geometry(f'{self.app_Width}x{self.app_Height}+{self.CenterX}+{self.CenterY}')
        self.minsize(width=self.app_Width, height=self.app_Height)
        self.maxsize(width=1920, height=1080)

        self.font1= ('Arial',19,'bold')
        self.font2= ('Arial',11)
        self.font3= ('Arial',14,'underline')
        self.font4= ('Arial',13.5)

        #import background
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.img1= customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'map.png')), size=(1920,1080))
        self.submit_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'arrow-right.png')), size=(25,25))
        self.logo_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'icon.png')), size=(100,100))
        self.back_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'arrow-left.png')), size=(25,25))
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

        self.loginsignup_label=customtkinter.CTkLabel(self.frame1,font=self.font1,text='Sign in',text_color='#fff')
        self.loginsignup_label.place(relx=0.5, rely=0.29, anchor=tkinter.CENTER)

        self.users_entry=customtkinter.CTkEntry(self.frame1,text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Username",placeholder_text_color='#18191A',width=230,height=30)
        self.users_entry.place(relx=0.5, rely=0.40, anchor=tkinter.CENTER)

        self.pass_entry=customtkinter.CTkEntry(self.frame1,show='*',text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Password",placeholder_text_color='#18191A',width=230,height=30)
        self.pass_entry.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)

        self.login_button= customtkinter.CTkButton(self.frame1, font=self.font4,text_color='#d3d3d3',cursor='hand2', width=50, height=50, image=self.submit_img, text="", corner_radius=10)
        self.login_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

        self.signup_button = customtkinter.CTkButton(self.frame1, font=self.font3, text="Create an Account", border_width=0, fg_color="transparent", hover_color="#808080", command=self.show_create)
        self.signup_button.place(relx=0.5, rely=0.86, anchor=tkinter.CENTER)
 
        self.option_1=customtkinter.CTkButton(self.frame1,font=self.font3, text='About ByahePH', fg_color="transparent", hover_color="#808080", command=self.show_about)
        self.option_1.place(relx=0.5, rely=0.93, anchor=tkinter.CENTER)

        self.frame1.place_forget() #Remove this

        # FRAME 2 --------------------

        self.frame2=customtkinter.CTkFrame(master=self.bg, width=356, height=600, corner_radius=18)
        self.frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.login_button = customtkinter.CTkButton(self.frame2, font=self.font4,text_color='#d3d3d3',cursor='hand2', width=50, height=50, image=self.back_img, text="", corner_radius=10, fg_color="transparent", hover=False, command=self.show_back)
        self.login_button.place(relx=0.01,rely=0.01,anchor=tkinter.NW)

        self.Register=customtkinter.CTkLabel(self.frame2,font=self.font1,text='Registration',text_color='#fff')
        self.Register.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        self.email_entry=customtkinter.CTkEntry(self.frame2, show="*", text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3', border_width=3, placeholder_text="Email", placeholder_text_color='#18191A', width=230,height=30)
        self.email_entry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        self.user_entry=customtkinter.CTkEntry(self.frame2, text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3', border_width=3, placeholder_text="Username", placeholder_text_color='#18191A', width=230,height=30)
        self.user_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        self.pass_entry=customtkinter.CTkEntry(self.frame2, show="*", text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3', border_width=3, placeholder_text="Password", placeholder_text_color='#18191A', width=230,height=30)
        self.pass_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.conf_entry=customtkinter.CTkEntry(self.frame2, show="*", text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3', border_width=3, placeholder_text="Password Confirmation", placeholder_text_color='#18191A', width=230,height=30)
        self.conf_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

        self.Register=customtkinter.CTkLabel(self.frame2,font=self.font2,text='Email:',text_color='#fff', height=10, bg_color="transparent")
        self.Register.place(relx=0.18, rely=0.22, anchor=tkinter.SW)
        self.Register=customtkinter.CTkLabel(self.frame2,font=self.font2,text='Username:',text_color='#fff', height=10, bg_color="transparent")
        self.Register.place(relx=0.18, rely=0.32, anchor=tkinter.SW)
        self.Register=customtkinter.CTkLabel(self.frame2,font=self.font2,text='Password:',text_color='#fff', height=10, bg_color="transparent")
        self.Register.place(relx=0.18, rely=0.42, anchor=tkinter.SW)
        self.Register=customtkinter.CTkLabel(self.frame2,font=self.font2,text='Password Confirmation:',text_color='#fff', height=10, bg_color="transparent")
        self.Register.place(relx=0.18, rely=0.52, anchor=tkinter.SW)

        self.login_button= customtkinter.CTkButton(self.frame2, cursor='hand2', width=50, height=50, image=self.submit_img, text="", corner_radius=10)
        self.login_button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

        self.frame2.place_forget()

        # FRAME 3 --------------------

        self.frame3 = customtkinter.CTkFrame(self.bg, width=356, height=600, corner_radius=18)
        self.frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.login_button = customtkinter.CTkButton(self.frame3, font=self.font4,text_color='#d3d3d3',cursor='hand2', width=50, height=50, image=self.back_img, text="", corner_radius=10, fg_color="transparent", hover=False, command=self.show_back)
        self.login_button.place(relx=0.01,rely=0.01,anchor=tkinter.NW)

        self.Register=customtkinter.CTkLabel(self.frame3,font=self.font1,text='About Us',text_color='#fff')
        self.Register.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)
        
        
    def show_create(self):
        self.frame1.place_forget()
        self.frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        pass

    def show_about(self):
        self.frame1.place_forget()
        self.frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        pass

    def show_back(self):
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        pass

app = App()
app.mainloop()