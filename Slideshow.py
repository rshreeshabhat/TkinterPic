import tkinter
from tkinter.constants import DISABLED, E, SUNKEN, W
from PIL import ImageTk, Image
root= tkinter.Tk()
root.title("LoremPicsum")

def forward(n):
    global label1
    global button_2
    global button_3
    label1.grid_forget()
    label1=tkinter.Label(image=image_list[n-1])
    button_3=tkinter.Button(root,text=">>",fg='black',command=lambda:forward(n+1))
    button_2=tkinter.Button(root,text="<<",fg='black',command=lambda:back(n-1))
    if n==6:
        button_3=tkinter.Button(root,text=">>",fg='black',state=DISABLED)
    status=tkinter.Label(root,text="Image "+str(n)+" of "+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    label1.grid(row=0,column=0,columnspan=3)
    button_3.grid(row=1,column=2 )
    button_2.grid(row=1,column=0 )
    
def back(n):
    global label1
    global button_2
    global button_3
    label1.grid_forget()
    label1=tkinter.Label(image=image_list[n-1])
    button_3=tkinter.Button(root,text=">>",fg='black',command=lambda:forward(n+1))
    button_2=tkinter.Button(root,text="<<",fg='black',command=lambda:back(n-1))
    if n==1:
        button_2=tkinter.Button(root,text="<<",fg='black',state=DISABLED)
    status=tkinter.Label(root,text="Image "+str(n)+" of "+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    label1.grid(row=0,column=0,columnspan=3)
    button_3.grid(row=1,column=2 )
    button_2.grid(row=1,column=0 )
button_1=tkinter.Button(root,text="Exit Program",bg='red',fg='white',command=root.quit)
button_2=tkinter.Button(root,text="<<",fg='black',state=DISABLED)
button_3=tkinter.Button(root,text=">>",fg='black',command=lambda:forward(2))
im=ImageTk.PhotoImage(Image.open('Images\img1.jpeg'))
im1=ImageTk.PhotoImage(Image.open('Images\img4.jpg'))
im2=ImageTk.PhotoImage(Image.open('Images\img3.jpg'))
im3=ImageTk.PhotoImage(Image.open('Images\img2.jpg'))
im4=ImageTk.PhotoImage(Image.open('Images\img5.jpg'))
im5=ImageTk.PhotoImage(Image.open('Images\img6.jpg'))
image_list=[im,im1,im2,im3,im4,im5]
status=tkinter.Label(root,text="Image 1 of "+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)
label1=tkinter.Label(image=im)
label1.grid(row=0,column=0,columnspan=3)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_2.grid(row=1,column=0 )
button_1.grid(row=1,column=1 )
button_3.grid(row=1,column=2 )
root.mainloop()