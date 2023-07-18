from tkinter import *
def submit():
    print("The temp is:"+ str(scale.get())+ " degrees C")

window =Tk()
hotImage =PhotoImage(file="burner.png")
hotLabel =Label(image=hotImage)
hotLabel.pack()
scale =Scale(window, from_=100,
             to=0,
             length=600,
             orient=VERTICAL,
             font=('Consolas',20),
             tickinterval=10,
             # ,showvalue=0,
             resolution=5,
             troughcolor="#69FAFF",
             fg="#FF1c00",
             bg="black"

             )
scale.set((scale["from"] - scale["to"]) / 2 + scale["to"])
scale.pack()

coldImage =PhotoImage(file="burger.png")
coldLabel =Label(image=coldImage)
coldLabel.pack()
button =Button(window, text="submit", command=submit)
button.pack()
window.mainloop()