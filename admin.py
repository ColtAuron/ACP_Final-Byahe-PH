import customtkinter
import tkinter
import sqlite3
import os
from PIL import ImageTk,Image


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "bphData.db")
        self.con = sqlite3.connect(self.db_path)
        self.c = self.con.cursor()

        self.app_Width = 1500
        self.app_Height = 900
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.CenterX = int((self.screen_width-self.app_Width)/2) #-200
        self.CenterY = int((self.screen_height-self.app_Height)/2) #-200

        self.title("Byahe PH Admin")
        self.geometry(f'{self.app_Width}x{self.app_Height}+{self.CenterX}+{self.CenterY}')
        self.minsize(width=self.app_Width, height=self.app_Height)
        self.maxsize(width=self.screen_width, height=self.screen_height)

        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.img1= customtkinter.CTkImage(light_image=Image.open(os.path.join(self.current_path, 'images', 'map.png')), size=(1920,1080))
        self.bg=customtkinter.CTkLabel(master=self,image=self.img1, text="")
        self.bg.pack()

        self.mainframe=customtkinter.CTkFrame(master=self.bg, width=1400, height=800, corner_radius=18)
        self.mainframe.place(relx=0.5, rely=.5, anchor=tkinter.CENTER)

        self.sidebar=customtkinter.CTkFrame(master=self.mainframe, width=270, height=800, border_color="grey")
        self.sidebar.place(relx=0, rely=.5, anchor=tkinter.W)
        
        self.font1= ('Arial',25,'bold')
        self.font2= ('Arial',18)
        self.fontnumber=('Arial',75)

        self.APlabel=customtkinter.CTkLabel(master=self.sidebar, font=self.font1, text='Admin Panel', text_color='#fff')
        self.APlabel.place(relx=0.5, rely=.045, anchor=tkinter.N)

        self.overview=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Dashboard', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showoverview)
        self.overview.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)
        self.extra1=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Extra1', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showextra1)
        self.extra1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        self.extra2=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Extra2', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showextra2)
        self.extra2.place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        
        self.OVFrame=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)

        self.OVlabel=customtkinter.CTkLabel(master=self.OVFrame, font=self.font1, text='Overview', text_color='#fff')
        self.OVlabel.place(relx=.04, rely=.04, anchor=tkinter.NW)

        self.OVUser=customtkinter.CTkFrame(master=self.OVFrame, width=200, height=250, corner_radius=20)
        self.OVUser.place(relx=0.33, rely=.30, anchor=tkinter.CENTER)
        self.OVUserlabel=customtkinter.CTkLabel(master=self.OVUser, font=self.font1, text='Users', text_color='#fff')
        self.OVUserlabel.place(relx=.5, rely=.15, anchor=tkinter.N)
        self.OVUsernum=customtkinter.CTkLabel(master=self.OVUser, font=self.fontnumber, text='0', text_color='#fff')
        self.OVUsernum.place(relx=.5, rely=.65, anchor=tkinter.CENTER)

        self.OVRequest=customtkinter.CTkFrame(master=self.OVFrame, width=200, height=250, corner_radius=20)
        self.OVRequest.place(relx=0.66, rely=.30, anchor=tkinter.CENTER)
        self.OVRequestlabel=customtkinter.CTkLabel(master=self.OVRequest, font=self.font1, text='Requests', text_color='#fff')
        self.OVRequestlabel.place(relx=.5, rely=.15, anchor=tkinter.N)
        self.OVReqnum=customtkinter.CTkLabel(master=self.OVRequest, font=self.fontnumber, text='0', text_color='#fff')
        self.OVReqnum.place(relx=.5, rely=.65, anchor=tkinter.CENTER)

        self.OVjeep=customtkinter.CTkFrame(master=self.OVFrame, width=200, height=250, corner_radius=20)
        self.OVjeep.place(relx=0.20, rely=.75, anchor=tkinter.CENTER)
        self.OVjeeplabel=customtkinter.CTkLabel(master=self.OVjeep, font=self.font1, text='Jeep Routes', text_color='#fff')
        self.OVjeeplabel.place(relx=.5, rely=.15, anchor=tkinter.N)
        self.OVjeepnum=customtkinter.CTkLabel(master=self.OVjeep, font=self.fontnumber, text='0', text_color='#fff')
        self.OVjeepnum.place(relx=.5, rely=.65, anchor=tkinter.CENTER)

        self.OVtrike=customtkinter.CTkFrame(master=self.OVFrame, width=200, height=250, corner_radius=20)
        self.OVtrike.place(relx=0.50, rely=.75, anchor=tkinter.CENTER)
        self.OVtrikelabel=customtkinter.CTkLabel(master=self.OVtrike, font=self.font1, text='Toda Pins', text_color='#fff')
        self.OVtrikelabel.place(relx=.5, rely=.15, anchor=tkinter.N)
        self.OVtrikenum=customtkinter.CTkLabel(master=self.OVtrike, font=self.fontnumber, text='0', text_color='#fff')
        self.OVtrikenum.place(relx=.5, rely=.65, anchor=tkinter.CENTER)

        self.OVbus=customtkinter.CTkFrame(master=self.OVFrame, width=200, height=250, corner_radius=20)
        self.OVbus.place(relx=0.80, rely=.75, anchor=tkinter.CENTER)
        self.OVbuslabel=customtkinter.CTkLabel(master=self.OVbus, font=self.font1, text='Bus Pins', text_color='#fff')
        self.OVbuslabel.place(relx=.5, rely=.15, anchor=tkinter.N)
        self.OVbusnum=customtkinter.CTkLabel(master=self.OVbus, font=self.fontnumber, text='0', text_color='#fff')
        self.OVbusnum.place(relx=.5, rely=.65, anchor=tkinter.CENTER)
        
        self.showoverview()

    def showoverview(self):
        self.OVFrame.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.overview.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        self.c.execute("SELECT COUNT(*) FROM ACCOUNT")
        self.OVUsernum.configure(text=str(self.c.fetchall()[0][0]))
        self.c.execute("SELECT COUNT(*) FROM REQUESTROUTE")
        self.OVReqnum.configure(text=str(self.c.fetchall()[0][0]))
        self.c.execute("SELECT COUNT(*) FROM ROUTE")
        self.OVjeepnum.configure(text=str(self.c.fetchall()[0][0]))
        self.c.execute("SELECT COUNT(*) FROM TODA")
        self.OVtrikenum.configure(text=str(self.c.fetchall()[0][0]))
        self.c.execute("SELECT COUNT(*) FROM TERMINAL")
        self.OVbusnum.configure(text=str(self.c.fetchall()[0][0]))

    def unshowoverview(self):
        self.OVFrame.place_forget()
        self.overview.configure(state='normal', fg_color='transparent',)

    def showextra1(self):
        self.unshowoverview()
    def showextra2(self):
        self.unshowoverview()


App().mainloop()