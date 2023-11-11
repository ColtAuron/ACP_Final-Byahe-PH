import customtkinter
from tkintermapview import TkinterMapView
import os
import sqlite3
from PIL import Image, ImageTk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

class Route:
    all = []
    def __init__(self, points, color:str, name:str, disabled=True):
        self.points = points
        self.color = color
        self.name = name
        self.disabled = disabled
        Route.all.append(self)

class Toda:
    all = []
    def __init__(self, position, locName:str, disabled=True):
        self.position = position
        self.locName = locName
        self.disabled = disabled
        Toda.all.append(self)

    def X(self):
        return self.position[0]
    
    def Y(self):
        return self.position[1]

class Terminal:
    all = []
    def __init__(self, position, locName: str, disabled=True):
        self.position = position
        self.locName = locName
        self.disabled = disabled
        Terminal.all.append(self)

    def X(self):
        return self.position[0]
    
    def Y(self):
        return self.position[1]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bphData.db")
con = sqlite3.connect(db_path)
c = con.cursor()

#Load tables
c.execute("SELECT * FROM POINTS")
points_table = c.fetchall()

c.execute("SELECT * FROM ROUTE")
route_table = c.fetchall()

c.execute("SELECT * FROM TODA")
toda_table = c.fetchall()

c.execute("SELECT * FROM TERMINAL")
terminal_table = c.fetchall()

#input tables information to classes

for jeepneys in route_table:
    c.execute(f"SELECT Point_X, Point_Y FROM POINTS WHERE RouteNum = {jeepneys[0]}") 
    points = c.fetchall()
    Route(points, jeepneys[2], jeepneys[1], jeepneys[3])
for toda in toda_table:
    Toda((toda[1],toda[2]),toda[3],toda[4])
for termi in terminal_table:
    Terminal((termi[1],termi[2]),termi[3],termi[4])

path_routes = []
toda_station = []
bus_terminal = []

command = ('''CREATE TABLE IF NOT EXISTS DRAWPOINTS(
           Id INTEGER PRIMARY KEY,
           Point_X FLOAT(3, 7),
           Point_Y FLOAT(3, 7)
)''')

c.execute(command)

c.execute("SELECT Point_X, Point_Y FROM DRAWPOINTS")
Draw_table = c.fetchall()

customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    APP_NAME = "ByahePH"
    WIDTH = 1400
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.CenterX = int((self.screen_width-App.WIDTH-375)/2)
        self.CenterY = int((self.screen_height-App.HEIGHT-250)/2)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{self.CenterX}+{self.CenterY}")
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        
        self.tmarker_image = ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, 'Tric.png')).resize((100, 150)))
        self.bmarker_image= ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, 'Bus.png')).resize((100, 150)))
       
        self.jeep_button=customtkinter.CTkImage(light_image=Image.open(os.path.join(BASE_DIR, 'jeep.png')), size=(50,50))    
        self.tric_button=customtkinter.CTkImage(light_image=Image.open(os.path.join(BASE_DIR, 'tricycle.png')), size=(50,50)) 
        self.bus_button=customtkinter.CTkImage(light_image=Image.open(os.path.join(BASE_DIR, 'buss.png')), size=(50,50)) 

        self.jeep_active =0
        self.tric_active =0
        self.bus_active =0
        
        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # Sidebar frame
        self.frame_left = customtkinter.CTkFrame(master=self, width=400, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.frame_left.grid_rowconfigure(9, weight=1)

        # Main frame
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        # Sidebar frame
        self.frame_left.grid_rowconfigure(1, weight=0)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left, text="Suggest Route", command=self.show_suggest)
        self.button_1.grid(pady=(10, 10), padx=(20, 20), row=1, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left, text="Jeep", image=self.jeep_button, command=self.show_jeep)
        self.button_2.grid(pady=(10, 10), padx=(20, 20), row=2, column=0)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,text="Tricycle", image=self.tric_button, command=self.show_tricycle) 
        self.button_3.grid(pady=(10, 10), padx=(20, 20), row=3, column=0)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left, text="Bus", image=self.bus_button, command=self.show_bus)
        self.button_4.grid(pady=(10, 10), padx=(20, 20), row=4, column=0)

        self.textbox1 = customtkinter.CTkTextbox(master=self.frame_left, width=150, height=100)
        
        self.textbox2 = customtkinter.CTkTextbox(master=self.frame_left, width=150, height=100)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Route name/Jeep name", width=130)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Route Colour", width=130)
       
        self.button_5 = customtkinter.CTkButton(master=self.frame_left, text="Submit", command=self.show_submit)
        

        # Main frame
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)
        
        script_directory = os.path.dirname(os.path.abspath(__file__))
        database_path = os.path.join(script_directory, "batangas.db")
    
        self.map_widget = TkinterMapView(self.frame_right, database_path=database_path, use_database_only=False)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))
        self.map_widget.configure(height=600, width=900)  # Set the map size
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_right, placeholder_text="Type Address")
        self.entry_3.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry_3.bind("<Return>", self.search_event)

        self.button_6 = customtkinter.CTkButton(master=self.frame_right, text="Search", width=90, command=self.search_event)
        self.button_6.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        self.button_7 = customtkinter.CTkButton(master=self.frame_right, text="Log-in", command=self.show_login)
        self.button_7.grid(row=0, column=2, sticky="e", padx=(12, 12), pady=12)

        # Set default values
        #self.map_widget.set_address("Batangas City")
        self.map_widget.set_position(deg_x=13.7582328,deg_y=121.0726133)
        self.map_widget.set_zoom(13)
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Dark", "Light", "System"], command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.set("Dark")
        self.appearance_mode_optionmenu.grid(row=50, column=0, padx=(20, 20), pady=(10, 10))
        
        #variables for draw
        self.suggestion_active = 0
        self.temp_points = None
        self.start_points = None
        self.drawed_coordinates = []
        self.marker_coords = None
        for items in Draw_table:
            self.add_to_coords(x=items[0],y=items[1])
        
    def show_suggest(self):
        if self.suggestion_active == 0:
            self.bind('<space>', self.toggle_coords)
            self.suggestion_active = 1 #Suggestion is active
            self.button_1._fg_color = 'blue' #pag pinindot #14304a
            self.textbox1.grid(row=5, column=0, padx=(15, 15), pady=(20, 0), sticky="nw")
            self.textbox1.insert("0.0", "\n""Click to create/draw.""\n""Ctrl+Z to undo""\n""Space to toggle draw""\n")
            self.textbox1.configure(state="disabled")
            self.entry_1.grid(row=6, column=0, sticky="we", padx=(12, 12), pady=12)
            self.entry_2.grid(row=7, column=0, sticky="we", padx=(12, 12), pady=12)
            self.button_5.grid(pady=(10, 10), padx=(20, 20), row=8, column=0)
        else:
            self.unbind('<space>')
            self.map_widget.canvas.config(cursor="arrow")
            self.map_widget.canvas.unbind("<Button-1>")
            self.unbind("<Control-z>")
            self.map_widget.canvas.bind("<B1-Motion>", self.map_widget.mouse_move)
            self.map_widget.canvas.bind("<Button-1>", self.map_widget.mouse_click)
            self.suggestion_active = 0 #Suggestion is inactive
            self.button_1._fg_color = list(('#3a7ebf','#1f538d')) #pag di pinindot
            if self.marker_coords:
                self.marker_coords.delete()
            self.drawed_coordinates.clear()
            self.start_points = None
            if self.temp_points:
                self.temp_points.delete()
            self.temp_points = None
            c.execute("DELETE FROM DRAWPOINTS")
            con.commit()
            self.textbox1.pack_forget()
            self.textbox1.grid_forget()
            self.entry_1.pack_forget()
            self.entry_1.grid_forget()
            self.entry_2.pack_forget()
            self.entry_2.grid_forget()
            self.button_5.pack_forget()
            self.button_5.grid_forget()
        pass

    def show_image(self):
        pass

    def show_login(self):
        pass

    def show_submit(self):
        pass

    def toggle_coords(self, event=None):
        if self.map_widget.canvas.cget('cursor') == "arrow":
            self.map_widget.canvas.config(cursor="tcross")
            self.map_widget.canvas.unbind("<B1-Motion>")
            self.map_widget.canvas.unbind("<Button-1>")
            self.map_widget.canvas.bind("<Button-1>", self.draw_coords)
            self.bind("<Control-z>", self.undo_draw_coords)
        else:
            self.map_widget.canvas.config(cursor="arrow")
            self.map_widget.canvas.unbind("<Button-1>")
            self.unbind("<Control-z>")
            self.map_widget.canvas.bind("<B1-Motion>", self.map_widget.mouse_move)
            self.map_widget.canvas.bind("<Button-1>", self.map_widget.mouse_click)

    def draw_coords(self, event=(0,0)):
        raw_mouse = self.map_widget.convert_canvas_coords_to_decimal_coords(canvas_x=event.x,canvas_y=event.y)
        mouse_pos = tuple((round(raw_mouse[0], 7),round(raw_mouse[1], 7)))
        c.execute("INSERT INTO DRAWPOINTS (Point_X, Point_Y) values (?,?)", mouse_pos)
        con.commit()
        self.add_to_coords(x=mouse_pos[0], y=mouse_pos[1])

    def add_to_coords(self, x, y):
        self.drawed_coordinates.append(tuple((x, y)))
        if self.start_points:
            if self.temp_points:
                self.temp_points.add_position(x, y)
            else:
                self.marker_coords.delete()
                self.temp_points = self.map_widget.set_path([self.start_points, tuple((x,y))], color='Black', width = 3)
        else:   
            self.start_points = tuple((x, y))
            self.marker_coords = self.map_widget.set_marker(x, y, text="Starting Point")


    def undo_draw_coords(self, event=None):
        if self.start_points:
            last_coord = self.drawed_coordinates[-1]
            c.execute("DELETE FROM DRAWPOINTS WHERE Id = (SELECT Max(Id) FROM DRAWPOINTS)")
            con.commit()
            if len(self.drawed_coordinates) > 2:
                self.temp_points.remove_position(last_coord[0], last_coord[1])
                self.drawed_coordinates.pop()
            elif len(self.drawed_coordinates) > 1:
                self.temp_points.delete()
                self.temp_points = None
                self.drawed_coordinates.pop()
                self.marker_coords = self.map_widget.set_marker(self.start_points[0], self.start_points[1], text="Starting Point")
            else:
                self.marker_coords.delete()
                self.drawed_coordinates.clear()
                self.start_points = None
                self.temp_points = None
                
    def search_event(self, event=None):
        self.map_widget.set_address(self.entry_3.get())

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def zoom_in_event(self):
        current_zoom = self.map_widget.get_zoom()
        self.map_widget.set_zoom(current_zoom + 1)

    def zoom_out_event(self):
        current_zoom = self.map_widget.get_zoom()
        self.map_widget.set_zoom(current_zoom - 1)

        #var for highlighting buttons
        self.jeep_active = 0
        self.tric_active = 0
        self.bus_active = 0

    def show_jeep(self):
        if path_routes:
            for jeepneys in path_routes:
                self.map_widget.delete(jeepneys)
            path_routes.clear()
        else:
            for jeepneys in Route.all:
                if jeepneys.disabled == False:
                    path_routes.append(self.map_widget.set_path(jeepneys.points, color = jeepneys.color, width = 3))
    
        if self.jeep_active == 1:
            self.jeep_active = 0  # button is active
            self.button_2._fg_color = list(('#3a7ebf', '#1f538d'))  # pag di pinindot
            
            self.textbox2.pack_forget()
            self.textbox2.grid_forget()
        else:
            self.jeep_active = 1  # button is inactive
            self.button_2._fg_color = 'blue'  # pag pinindot
            self.textbox2.grid(row=9, column=0, padx=(15, 15), pady=(20, 0), sticky="nw")
            self.textbox2.insert("0.0", "Blue =\nYellow =\nGreen =\nGray =")
            self.textbox2.configure(state="disabled")
    pass

    def show_tricycle(self):
        if toda_station:
            for toda in toda_station:
                self.map_widget.delete(toda)
            toda_station.clear()
        else:
            for toda in Toda.all:
                if toda.disabled == False:
                    toda_station.append(self.map_widget.set_marker(toda.X(), toda.Y(), text=f"{toda.locName} Toda", icon=self.tmarker_image, text_color = "#8B0000"))

        if self.tric_active == 1:
            self.tric_active = 0  # button is active
            self.button_3._fg_color = list(('#3a7ebf', '#1f538d'))  # pag di pinindot
        else:
            self.tric_active = 1  # button is inactive
            self.button_3._fg_color = 'blue'  # pag pinindot
    pass

    def show_bus(self):
        if bus_terminal:
            for marker in bus_terminal:
                self.map_widget.delete(marker)
            bus_terminal.clear()
        else:
            for termi in Terminal.all:
                if termi.disabled == False:
                    bus_terminal.append(self.map_widget.set_marker(termi.X(), termi.Y(), text=f"{termi.locName} Terminal", marker_color_outside = "#00008B", text_color = "#00008B", marker_color_circle = "#87CEEB", icon=self.bmarker_image))
        if self.bus_active == 1:
            self.bus_active = 0  # button is active
            self.button_4._fg_color = list(('#3a7ebf', '#1f538d'))  # pag di pinindot
        else:
            self.bus_active = 1  # button is inactive
            self.button_4._fg_color = 'blue'  # pag pinindot
    pass

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()