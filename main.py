from tkinter import *
root=Tk()
root.title=('Centimeter to inch')
root.geometry=('400x400')
l1=Label(root,text='Enter The Inch')
e1=Entry(root)
def cent():
    inch=int(e1.get())
    c=inch*2.54

    l4=Label(root,text=c)    

    l4.grid(row=1,column=0)

b1=Button(root,text='Convert',command=cent)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b1.grid(row=2,column=1)
root.mainloop()



