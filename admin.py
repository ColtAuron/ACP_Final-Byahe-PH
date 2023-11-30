import customtkinter
import tkinter
import sqlite3
import os
from PIL import ImageTk,Image
from CTkTable import *
from CTkMessagebox import CTkMessagebox
from coltinputdialog import ColtInputDialog
import re
from tkintermapview import TkinterMapView

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

        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

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

        #--------- Side bar ----------

        self.APlabel=customtkinter.CTkLabel(master=self.sidebar, font=self.font1, text='Admin Panel', text_color='#fff')
        self.APlabel.place(relx=0.5, rely=.045, anchor=tkinter.N)

        self.overview=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Dashboard', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showoverview)
        self.overview.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)
        self.users=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Users', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showusers)
        self.users.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        self.requests=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Requests', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showrequests)
        self.requests.place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        self.routes=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Jeep Routes', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showroutes)
        self.routes.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)
        self.todas=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Toda Pins', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showtodas)
        self.todas.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
        self.bus=customtkinter.CTkButton(self.sidebar, font=self.font2, text='Bus Pins', fg_color="transparent", hover_color="#808080", corner_radius=0, width=270, height=50, command=self.showbus)
        self.bus.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)

        #--------- OV Frame ----------

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
        
        #--------- Users Frame ----------

        self.usersframe=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)
        usersvalues = [['ID', 'Email', 'Username', 'Admin']]
        self.userstitle=CTkTable(master=self.usersframe, width=160, height=10, values=usersvalues)
        self.userstitle.place(relx=.420, rely=.13, anchor=tkinter.CENTER)
        self.userscroll= customtkinter.CTkScrollableFrame(self.usersframe, width=810, height=500)
        self.userscroll.place(relx=.505, rely=.15, anchor=tkinter.N)
        self.userstable=CTkTable(master=self.userscroll, width=200, height=10, values=[[1,2,3,4,5]], command=self.usertableclick)

        #--------- Requests Frame ----------
        self.requestsframe=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)
        requestsvalues = [['Route Number', 'Name', 'Color', 'Author']]
        self.requeststitle=CTkTable(master=self.requestsframe, width=113, height=10, values=requestsvalues)
        self.requeststitle.place(relx=.328, rely=.13, anchor=tkinter.CENTER)
        self.requestscroll= customtkinter.CTkScrollableFrame(self.requestsframe, width=810, height=500)
        self.requestscroll.place(relx=.505, rely=.15, anchor=tkinter.N)
        self.requesttable=CTkTable(master=self.requestscroll, width=200, height=10, values=[[1,2,3,4,5]], command=self.reqtableclick)

        #--------- Jeep Routes Frame ----------
        self.jeepframe=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)

        #--------- Toda Pins Frame ----------
        self.todaframe=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)

        #--------- Bus Pins Frame ----------
        self.busframe=customtkinter.CTkFrame(master=self.mainframe, width=1000, height=700, corner_radius=20)

        self.showrequests()

    
    #----------- OV ------------

    def showoverview(self):
        self.unshowall()
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

    #----------- users ------------

    def showusers(self):
        self.unshowall()
        self.usersframe.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.users.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        self.refreshusers()

    def refreshusers(self):
        updated_table = list()
        self.c.execute("SELECT ID, Email, User, Admin FROM ACCOUNT")
        table = self.c.fetchall()
        for items in table:
            updated_table.append((items[0],items[1],items[2],items[3],'DELETE'))
        self.userstable=CTkTable(master=self.userscroll, width=200, height=10, values=updated_table, command=self.usertableclick) #self.usertableclick returns values rows, colm, args
        self.userstable.pack()

    def usertableclick(self, args): #stored in the first argument
        if args["value"] == 'DELETE': #calls the value with key "value"
            user = self.userstable.get_row(row=args["row"])[2] #"Grabs the column 2 which is the username"
            id = int(self.userstable.get_row(row=args["row"])[0]) #Grabs the column 0 which is the ID
            msg = CTkMessagebox(title="Delete?", message=f"Delete user: {user} id: {id} ?", icon="question", option_1="No", option_3="Yes") #Asks for confirmation
            response = msg.get() #Waits and grabs information
            if response=="Yes": #Self explanatory DUUUHH
                self.c.execute("DELETE from ACCOUNT WHERE ID=?", (id,)) #Delete query
                self.con.commit() #Commit and save changes
                CTkMessagebox(title="DELETED!", message="Successfully Deleted") #Alert User
        elif args["column"] == 0: #Checks if the column is equal to 0 meaning its an ID
            CTkMessagebox(title="Error", message="Altering IDs are not allowed", icon="cancel") #Alert User
        else:
            text = "Alter: " 
            title = "Change "
            if args["column"] == 3: #Check if the column is for admin type
                text = "Alter: 1 = True, 0 = False" #Then display this
                title = "Give Administrator"
            tochange = args["value"] #Grabs value of the clicked
            id = int(self.userstable.get_row(row=args["row"])[0]) 
            dialog = ColtInputDialog(text=text, title=title, placeholder_text=tochange) #Prompt user for change
            output = dialog.get_input() 
            if output and output != tochange:
                if args["column"] == 3:  #Check if the column is for admin type
                    number = int(output)
                    if number == 1 or number == 0: #Check if its only 1 or 0
                        self.c.execute("UPDATE ACCOUNT SET Admin = ? WHERE ID=?", (number, id)) #Change Query
                        self.con.commit()
                    else:
                        CTkMessagebox(title="Error", message="Input only 1 or 2", icon="cancel") #Alert User
                else:
                    if args["column"] == 1:#Checks if the column is for email type
                        self.c.execute("SELECT Email FROM ACCOUNT WHERE Email=?", (output,))
                        email_table = self.c.fetchall()
                        if (re.fullmatch(self.regex, output)):
                            if email_table == []:
                                self.c.execute("UPDATE ACCOUNT SET Email = ? WHERE ID=?", (output, id)) #Change Query
                                self.con.commit()
                            else:
                                CTkMessagebox(title="Error", message="Email Already Taken", icon="cancel")
                        else:
                            CTkMessagebox(title="Error", message="Invalid Email", icon="cancel") #Alert User
                    else:
                        self.c.execute("SELECT User FROM ACCOUNT WHERE User=?", (output,))
                        username_table = self.c.fetchall()
                        if username_table == []:
                            self.c.execute("UPDATE ACCOUNT SET User = ? WHERE ID=?", (output, id)) #Change Query
                            self.con.commit()
                        else:
                            CTkMessagebox(title="Error", message="Username Already Taken", icon="cancel")
        self.userstable.destroy() #Destroys current table
        self.refreshusers() #Creates and build from the database
    
    def unshowusers(self):
        self.userstable.destroy()
        self.usersframe.place_forget()
        self.users.configure(state='normal', fg_color='transparent',)

    #--------------- Requests -------------

    def showrequests(self):
        self.unshowall()
        self.requestsframe.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.requests.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        self.refreshrequests()

    def unshowrequests(self):
        self.requesttable.destroy()
        self.requestsframe.place_forget()
        self.requests.configure(state='normal', fg_color='transparent',)
        pass

    def refreshrequests(self):
        updated_table = list()
        self.c.execute("SELECT RouteNum, Name, Color, Author FROM REQUESTROUTE")
        table = self.c.fetchall()
        for items in table:
            self.c.execute("SELECT User FROM ACCOUNT WHERE ID=?", (items[3],))
            author = self.c.fetchall()
            updated_table.append((items[0],items[1],items[2],author,'INSPECT','ACCEPT', 'DELETE'))
        self.requesttable=CTkTable(master=self.requestscroll, width=150, height=10, values=updated_table, command=self.reqtableclick) #self.usertableclick returns values rows, colm, args
        self.requesttable.pack()
        pass

    def reqtableclick(self, args):
        name = self.requesttable.get_row(row=args["row"])[1]
        id = int(self.requesttable.get_row(row=args["row"])[0])
        if args["value"] == 'DELETE': 
            msg = CTkMessagebox(title="Delete?", message=f"Delete Route: {name}, RNum = {id} ?", icon="question", option_1="No", option_3="Yes")
            response = msg.get()
            if response=="Yes":
                self.c.execute("DELETE from REQUESTROUTE WHERE RouteNum=?", (id,)) 
                self.con.commit() 
                CTkMessagebox(title="DELETED!", message="Successfully Deleted") 
        elif args["value"] == 'ACCEPT':
            msg = CTkMessagebox(title="ACCEPT?", message=f"Accept Route Name: {name}, \nRNum = {id} ?", icon="question", option_1="No", option_3="Yes")
            response = msg.get()
            if response=="Yes":
                color = self.requesttable.get_row(row=args["row"])[2]
                self.c.execute("SELECT Point_X, Point_Y FROM REQUESTPOINTS WHERE RouteNum=?", (id,))
                points = self.c.fetchall()
                self.c.execute("INSERT INTO ROUTE (Name, Color) VALUES (?,?)", (name, color))
                self.con.commit()
                self.c.execute("SELECT Max(RouteNum) FROM ROUTE")
                newID = self.c.fetchall()[0][0]
                for point in points:
                    self.c.execute("INSERT INTO POINTS (Point_X, Point_Y, RouteNum) VALUES (?,?,?)", (point[0], point[1], newID))
                    self.con.commit()
                CTkMessagebox(title="COMMITED!", message="Successfully Added!")
        elif args["value"] == 'INSPECT':
            self.c.execute("SELECT Point_X, Point_Y FROM REQUESTPOINTS WHERE RouteNum=?", (id,))
            points = self.c.fetchall()
            color = self.requesttable.get_row(row=args["row"])[2]
            InspectWindow = ColtInspect(points, name, color)
            InspectWindow.after(100, InspectWindow.lift)
            InspectWindow.wait_window()
        elif args["column"] == 0: 
            CTkMessagebox(title="Error", message="Altering IDs are not allowed", icon="cancel") 
        elif args["column"] == 3:
            CTkMessagebox(title="Error", message="Altering Authors are not allowed", icon="cancel") 
        else:
            text = "Enter Route Name" 
            title = "Change Name"
            if args["column"] == 2: 
                text = "Change Route Color: (HEX OR VALID COLOR) \n VALID HEX: #rgb #rrggbb #rrrgggbbb \n (EXAMPLE: #F00 = RED)" 
                title = "Change Color"
            tochange = args["value"] 
            dialog = ColtInputDialog(text=text, title=title, placeholder_text=tochange) #Prompt user for change
            output = dialog.get_input()
            if output and output != tochange:
                if args["column"] == 2: #route color
                    self.c.execute("UPDATE REQUESTROUTE SET Color = ? WHERE RouteNum=?", (output, id)) #Change Query
                    self.con.commit()
                    CTkMessagebox(title="COMMITED!", message="Successfully Changed!")
                else:
                    self.c.execute("SELECT Name FROM REQUESTROUTE WHERE Name=?", (output,))
                    username_table = self.c.fetchall()
                    if username_table == []:
                        self.c.execute("UPDATE REQUESTROUTE SET Name = ? WHERE RouteNum=?", (output, id)) #Change Query
                        self.con.commit()
                        CTkMessagebox(title="COMMITED!", message="Successfully Changed!")
                    else:
                        CTkMessagebox(title="Error", message="Username Already Taken", icon="cancel")
        self.requesttable.destroy()
        self.refreshrequests()
        pass

    #--------------- Routes ---------------

    def showroutes(self):
        self.unshowall()
        self.jeepframe.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.routes.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        pass

    def unshowroutes(self):
        self.jeepframe.place_forget()
        self.routes.configure(state='normal', fg_color='transparent',)
        pass

    #--------------- Todas ----------------

    def showtodas(self):
        self.unshowall()
        self.todaframe.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.todas.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        pass

    def unshowtodas(self):
        self.todaframe.place_forget()
        self.todas.configure(state='normal', fg_color='transparent',)
        pass

    #-------------- Bus -------------------

    def showbus(self):
        self.unshowall()
        self.busframe.place(relx=0.6, rely=.5, anchor=tkinter.CENTER)
        self.bus.configure(state='disabled', fg_color='#808080', text_color_disabled='#ffffff')
        pass

    def unshowbus(self):
        self.busframe.place_forget()
        self.bus.configure(state='normal', fg_color='transparent',)
        pass

    #------------- Misc ------------------

    def unshowall(self):
        self.unshowoverview()
        self.unshowusers()
        self.unshowrequests()
        self.unshowroutes()
        self.unshowtodas()
        self.unshowbus()
        pass

class ColtInspect(customtkinter.CTkToplevel):
    def __init__(self, points, name, color = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.CenterX = int((self.screen_width-800)/2) #-200
        self.CenterY = int((self.screen_height-600)/2) #-200
        self.geometry(f"{800}x{600}+{self.CenterX}+{self.CenterY}")
        self.maxsize(width=800, height=600)
        self.minsize(width=800, height=600)
        self.grab_set()
        title = "Route"
        if len(points) == 1:
            title = "Point"
        self.title(f"{name} {title}")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "batangas.db")

        self.map_widget = TkinterMapView(self, width=800, height=600,database_path=self.db_path, use_database_only=False)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map_widget.set_position(deg_x=points[0][0],deg_y=points[0][1])

        if len(points) == 1:
            self.obj = self.map_widget.set_marker(deg_x=points[0][0], deg_y=points[0][1], text=name)
        else:
            self.obj = self.map_widget.set_path(position_list=points, color=color, width=3)

    def _on_closing(self):
        self.map_widget.delete(self.obj)
        self.grab_release
        self.destroy()
        




App().mainloop()
