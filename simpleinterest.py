from tkinter import *
window=Tk()

# add widgets here


window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Enter Weight", fg = "black", bg = "lightcyan", font=("Calibri", 12))
height_label.place(x=20, y=140)
height_entry = Entry(window, text = "",bd=2, width=15)
height_entry.place(x=150, y=142)

weight_label=Label(window, text="Enter Weight", fg = "black", bg = "lightcyan", font=("Calibri", 12))
weight_label.place(x=20, y=25)
weight_entry = Entry(window, text = "",bd=2, width=15)
weight_entry.place(x=150, y=187)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

outputMessage=Label(result_frame,text=name + "your bmi is" + str(bmi) + message, bg = "lightcyan", font=("Calibri", 12), width=42)
outputMessage.place(x=20,y=40)
outputMessage.pack()

calculateButton=Button(window, text="Caculate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=4,command=calculate_bmi())
calculateButton.place(x=20, y=250)
window.mainloop()

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi,1)
    name = username.get()

result_label.destroy()
message = ""
if bmi < 18.5:
    message = "You are underweight"
elif bmi > 18.5 and bmi <= 24.9:
    message = "This is normal"
elif bmi > 25 and bmi < 29.9:
    message = "You are overweight"
elif bmi > 30:
    message = "you are obese"
else:
    message = "something is wrong"