from tkinter import*
food =["pizzza", "hamburger", "hotdog"]
def order():
    if(x.get()==0):
        print("You ordered pizaa")
    elif(x.get()==1):
        print("You ordered a hambuger")
    elif (x.get() == 2):
        print("You ordered a hot dog")
    else:
        print("you can come another day")

window =Tk()

pizzaImage =PhotoImage(file="pizza.png")
hamburgerImage =PhotoImage(file="burger.png")
hotdogImage =PhotoImage(file="hotdog.png")
foodImages =[pizzaImage,hamburgerImage,hotdogImage]

x= IntVar()
for index in range(len(food)):
    radiobutton =Radiobutton(window,
                             text=food[index],
                             variable=x,
                             value=index,
                            padx=25,
                              font=("impact",50),
                             image =foodImages[index],
                             compound='left',
                             indicatoron=0,
                             width=375,
                             command=order
                             )


    radiobutton.pack(anchor="w")



window.mainloop()

