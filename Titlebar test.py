import customtkinter
import tkinter

WHITE = "#FFFFFF"
GRAY = "#282424"

class TitleBar(Frame):
    def __init__(self, parent, title: str, icon_path=None):
        self.root = parent
        self.root.overrideredirect(True)
        super().__init__(parent, bg=GRAY)

        self.profile_pic=customtkinter.CTkImage(light_image=Image.open(os.path.join(BASE_DIR, 'images', 'profile-icon.png')), size=(30,30)) 

        self.nav_title = Label(self, text=title, foreground=WHITE, background=GRAY)
        self.nav_title.bind("<ButtonPress-1>", self.oldxyset_label)
        self.nav_title.bind("<B1-Motion>", self.move)
        self.nav_title.pack(side="left", padx=(10))

        CTkButton(self, text='✕', cursor="hand2", corner_radius=0, fg_color=GRAY,
                  hover_color=GRAY, width=40, command=self.close_window).pack(side="right")

        self.bind("<ButtonPress-1>", self.oldxyset)
        self.bind("<B1-Motion>", self.move)

    def oldxyset(self, event):
        self.oldx = event.x 
        self.oldy = event.y

    def oldxyset_label(self, event):
        self.oldx = event.x + self.nav_title.winfo_x()
        self.oldy = event.y + self.nav_title.winfo_y()

    def move(self, event):
        self.y = event.y_root - self.oldy
        self.x = event.x_root - self.oldx
        self.root.geometry(f"+{self.x}+{self.y}")

    def close_window(self):
        self.root.destroy()

# Window Setup
window = CTk()
window.geometry("450x250")

# Set Title Bar with Icon
jeep_icon = r"C:/Users/RemmiaVenus Espiritu/Documents/GitHub/Byahe-PH/images/jeep.png"
titlebar = TitleBar(window, title="Byahe-PH", icon_path=jeep_icon)
titlebar.pack(fill="both")

# Run
window.mainloop()
