import customtkinter
import tkinter
from PIL import ImageTk,Image
import sys


app = customtkinter.CTk()
app.title("Byahe PH")
app.geometry('370x520')

font1= ('Segoe Print',19,'bold')
font2= ('Segoe Print',23,'bold')
font3= ('Arial',14,'underline')
font4= ('Arial',13.5)



#import background
img1=ImageTk.PhotoImage(Image.open("map.png"))
bg=customtkinter.CTkLabel(master=app,image=img1)
bg.pack()

#create frame
frame1=customtkinter.CTkFrame(master=bg, width=356, height=430, corner_radius=18)
frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


welcome_label=customtkinter.CTkLabel(frame1,font=font2,text='Welcome to ByahePH!',text_color='#fff')
welcome_label.place(x=50,y=65)

loginsignup_label=customtkinter.CTkLabel(frame1,font=font1,text='Login or Sign Up',text_color='#fff')
loginsignup_label.place(x=98,y=110)

users_entry=customtkinter.CTkEntry(frame1,text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Username",placeholder_text_color='#18191A',width=150,height=10)
users_entry.place(x=100,y=150)


pass_entry=customtkinter.CTkEntry(frame1,show='*',text_color='#18191A', fg_color='#d3d3d3', bg_color='#03045E', border_color='#D3D3D3',border_width=3, placeholder_text="Password",placeholder_text_color='#18191A',width=150,height=10)
pass_entry.place(x=100,y=190)

signup_button = customtkinter.CTkButton(frame1,font=font3, text="Sign Up")
signup_button.place(x=105, y=230)

login_button= customtkinter.CTkButton(frame1, font=font3,text='Log in',text_color='#d3d3d3',cursor='hand2', width=140)
login_button.place(x=105,y=270)
 
option_1=customtkinter.CTkButton(frame1,font=font3, text='About ByahePH')
option_1.place(x=105,y=310)


app.mainloop()