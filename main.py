import tkinter
import tkintermapview
import os
import config
import sqlite3

path_routes = []

#Connect to database

con = sqlite3.connect('bphData.db')
c = con.cursor()
c.execute("PRAGMA foreign_keys = ON")

c.execute("SELECT * FROM POINTS")
points_table = c.fetchall()

c.execute("SELECT * FROM ROUTE")
route_table = c.fetchall()


for items in points_table:
    print(f"Point: {items}")

for items in route_table:
    print(f"Route: {items}")


root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{800}")
root_tk.title("Byahe PH")

#offline
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "batangas.db")

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=800, corner_radius=0, max_zoom=22, use_database_only=False, database_path=database_path)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.pack(fill="both", expand=True)

for jeepneys in route_table:
    if jeepneys[3] == False:
        c.execute(f"SELECT Point_X, Point_Y FROM POINTS WHERE RouteNum = {jeepneys[0]}")
        points = c.fetchall()
        path_routes.append(map_widget.set_path(points, color = jeepneys[2], width = 3))

address = tkintermapview.convert_address_to_coordinates("Batangas City")
map_widget.set_position(address[0], address[1])
map_widget.set_zoom(13)

con.close()

root_tk.mainloop()
