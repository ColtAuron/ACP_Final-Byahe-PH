import customtkinter
from tkintermapview import TkinterMapView
import os
import sqlite3

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

#Connect to database
con = sqlite3.connect('bphData.db')
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

customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    APP_NAME = "ByahePH"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

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
        self.frame_left.grid_rowconfigure(6, weight=1)

        # Main frame
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)

        # Sidebar frame
        self.frame_left.grid_rowconfigure(1, weight=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left, text="Clear Markers", command=self.clear_marker_event)
        self.button_2.grid(pady=(10, 10), padx=(20, 20), row=1, column=0)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left, text="Jeep", command=self.show_jeep)
        self.button_3.grid(pady=(10, 10), padx=(20, 20), row=2, column=0)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left, text="Tricycle", command=self.show_tricycle)
        self.button_4.grid(pady=(10, 10), padx=(20, 20), row=3, column=0)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left, text="Bus", command=self.show_bus)
        self.button_5.grid(pady=(10, 10), padx=(20, 20), row=4, column=0)

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

        

        self.entry = customtkinter.CTkEntry(master=self.frame_right, placeholder_text="Type Address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        self.map_widget.add_right_click_menu_command(label="Add Marker", command=self.add_marker_event, pass_coords=True)

        self.bind('<space>', self.toggle_coords)

        # Set default values
        self.map_widget.set_address("Batangas City")
        self.map_widget.set_zoom(11)
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Dark", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.set("Dark")
        self.appearance_mode_optionmenu.grid(row=50, column=0, padx=(20, 20), pady=(10, 10))

        #variables for draw
        self.temp_points = None
        self.start_points = None
        self.drawed_coordinates = []
        for items in Draw_table:
            self.add_to_coords(x=items[0],y=items[1])

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
        self.map_widget.set_address(self.entry.get())

    def add_marker_event(self, coords):
        print("Add marker:", coords)
        new_marker = self.map_widget.set_marker(coords[0], coords[1], text="new marker")
        self.marker_list.append(new_marker)

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def zoom_in_event(self):
        current_zoom = self.map_widget.get_zoom()
        self.map_widget.set_zoom(current_zoom + 1)

    def zoom_out_event(self):
        current_zoom = self.map_widget.get_zoom()
        self.map_widget.set_zoom(current_zoom - 1)

    def show_jeep(self):
        if path_routes:
            for jeepneys in path_routes:
                self.map_widget.delete(jeepneys)
            path_routes.clear()
        else:
            for jeepneys in Route.all:
                if jeepneys.disabled == False:
                    path_routes.append(self.map_widget.set_path(jeepneys.points, color = jeepneys.color, width = 3))
        pass

    def show_tricycle(self):
        if toda_station:
            for toda in toda_station:
                self.map_widget.delete(toda)
            toda_station.clear()
        else:
            for toda in Toda.all:
                if toda.disabled == False:
                    toda_station.append(self.map_widget.set_marker(toda.X(), toda.Y(), text=f"{toda.locName} Toda"))
        pass

    def show_bus(self):
        if bus_terminal:
            for marker in bus_terminal:
                self.map_widget.delete(marker)
            bus_terminal.clear()
        else:
            for termi in Terminal.all:
                if termi.disabled == False:
                    bus_terminal.append(self.map_widget.set_marker(termi.X(), termi.Y(), text=f"{termi.locName} Terminal", marker_color_outside = "#00008B", text_color = "#00008B", marker_color_circle = "#87CEEB" ))
        pass

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()