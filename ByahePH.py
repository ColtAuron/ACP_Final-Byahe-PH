import customtkinter
from tkintermapview import TkinterMapView
import config
import os

path_routes = []
toda_station = []
bus_terminal = []

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

        # Set default values
        self.map_widget.set_address("Batangas City")
        self.map_widget.set_zoom(11)
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Dark", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.set("Dark")
        self.appearance_mode_optionmenu.grid(row=50, column=0, padx=(20, 20), pady=(10, 10))

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
        # Implement code to show Jeep on the map
        if path_routes:
            for jeepneys in path_routes:
                self.map_widget.delete(jeepneys)
            path_routes.clear()
        else:
            for jeepneys in config.Route.all:
                if jeepneys.disabled == False:
                    path_routes.append(self.map_widget.set_path(jeepneys.points, color = jeepneys.color, width = 3))
        pass

    def show_tricycle(self):
        if toda_station:
            for toda in toda_station:
                self.map_widget.delete(toda)
            toda_station.clear()
        else:
            for toda in config.Toda.all:
                if toda.disabled == False:
                    toda_station.append(self.map_widget.set_marker(toda.position[0], toda.position[1], text=f"{toda.locName} Toda"))
        pass

    def show_bus(self):
        if bus_terminal:
            for marker in bus_terminal:
                self.map_widget.delete(marker)
            bus_terminal.clear()
        else:
            for marker in config.Terminal.all:
                if marker.disabled == False:
                    bus_terminal.append(self.map_widget.set_marker(marker.position[0], marker.position[1], text=f"{marker.locName} Terminal", marker_color_outside = "#00008B", text_color = "#00008B", marker_color_circle = "#87CEEB" ))
        pass

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()