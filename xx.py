import tkinter

canvas = tkinter.Canvas(height= 500, width= 500)
canvas.pack()


x = 20 
w = 500/x

for i in range(1,x+1):

    canvas.create_line(0, 500/x*i,500, 500/x*i)
    canvas.create_line(500/x*i, 0, 500/x*i, 500)

def klik(a):

    print("x",a.x)
    print("y",a.y)

    canvas.create_oval(a.x//w*w, a.y//w*w, a.x//w*w+w, a.y//w*w+w, fill="red")

def klik2(c):

    print("x",c.x)
    print("y",c.y)

    canvas.create_line(c.x//w*w, c.y//w*w, c.x//w*w+w, c.y//w*w+w, fill="green")
    canvas.create_line(c.x//w*w, c.y//w*w, c.x//w*w+w, c.y//w*w+w, fill="green")   


canvas.bind("<Button-1>", klik)
canvas.bind("<Button-3>", klik2)










tkinter.mainloop()
