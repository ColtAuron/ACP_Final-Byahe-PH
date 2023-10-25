import tkinter
import tkintermapview
import os
import config

path_routes = []

root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{800}")
root_tk.title("Byahe PH")

#offline
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "batangas.db")

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=800, corner_radius=0, max_zoom=22, use_database_only=False, database_path=database_path)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.pack(fill="both", expand=True)

for jeepneys in config.Route.all:
    if jeepneys.disabled == False:
        path_routes.append(map_widget.set_path(jeepneys.points, color = jeepneys.color, width = 3))

address = tkintermapview.convert_address_to_coordinates("Batangas City")
map_widget.set_position(address[0], address[1])
map_widget.set_zoom(13)

root_tk.mainloop()
