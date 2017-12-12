import sys
from Tkinter import *
import tkFont

root=Tk()
img = Image("photo", file="icon.png")
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(0,0)
frame=Frame(root)
frame.pack()
root.title('BASIC CALCULATOR')
num=StringVar()
topframe0=Frame(root)
topframe0.pack(side='top')
txtdisplay=Entry(frame,textvariable=num,bd=12,insertwidth=1,font = tkFont.Font(size=12))
txtdisplay.pack(side='top')
def clear():
	txtdisplay.delete(0, END)
def delete():
	txtdisplay.delete(len(txtdisplay.get())-1, 'end')
def setval(a):
	if a==-1:
		s=txtdisplay.get().split('.')
		print(s)
		if len(s)< 2:
			txtdisplay.insert(END,str('.'))
	else:
		txtdisplay.insert(END,str(a))
	#print("hello!!")
op=-1
v1=0.0
def oper(a):
	global op
	op =a
	global v1
	v1=float(str(txtdisplay.get()))
	print(v1)
	txtdisplay.delete(0,END)
def displayanswer():
	global v1
	if op == 0:
		v2=float(str(txtdisplay.get()))
		txtdisplay.delete(0,END)
		print(v2)
		ans=v1+v2
		txtdisplay.insert(END,ans)
	if op == 1:
		v2=float(str(txtdisplay.get()))
		txtdisplay.delete(0,END)
		print(v2)
		ans=v1*v2
		txtdisplay.insert(END,ans)

	if op == 2:
		v2=float(str(txtdisplay.get()))
		txtdisplay.delete(0,END)
		print(v2)
		ans=v1-v2
		txtdisplay.insert(END,ans)

	if op == 3:
		v2=float(str(txtdisplay.get()))
		txtdisplay.delete(0,END)
		print(v2)
		if(v2==0):
			ans='DIVISION WITH ZERO'
			v1=0.0
			txtdisplay.insert(END,ans)
		else:
			ans=v1/v2
			txtdisplay.insert(END,ans)

button0=Button(topframe0,text="C",padx=16,pady=16,bd=3,fg='white',bg='red',command=lambda:clear())
button0.grid(row=0,column=0)
buttond=Button(topframe0,text="DEL",padx=16,pady=16,bd=3,fg='BLACK',bg='green',command=lambda:delete())
buttond.grid(row=0,column=4)
topframe=Frame(root)
topframe.pack(side='top')

button1=Button(topframe,text="1",padx=16,pady=16,bd=3,fg='black',command=lambda:setval(1))
button1.pack(side='left')
button2=Button(topframe,text="2",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(2))
button2.pack(side='left')
button3=Button(topframe,text="3",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(3))
button3.pack(side='left')
button4=Button(topframe,text="+",padx=16,pady=16,fg='black',bd=3,command=lambda:oper(0))
button4.pack(side='left')
topframe1=Frame(root)
topframe1.pack(side='top')
button5=Button(topframe1,text="4",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(4))
button5.pack(side='left')
button6=Button(topframe1,text="5",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(5))
button6.pack(side='left')
button7=Button(topframe1,text="6",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(6))
button7.pack(side='left')
button8=Button(topframe1,text=" X",padx=16,pady=16,fg='black',bd=3,command=lambda:oper(1))
button8.pack(side='left')
topframe2=Frame(root)
topframe2.pack(side='top')
button9=Button(topframe2,text="7",padx=16,pady=16,fg='green',bd=3,command=lambda:setval(7))
button9.pack(side='left')
button10=Button(topframe2,text="8",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(8))
button10.pack(side='left')
button12=Button(topframe2,text="9",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(9))
button12.pack(side='left')
button11=Button(topframe2,text=" - ",padx=16,pady=16,fg='black',bd=3,command=lambda:oper(2))
button11.pack(side='left')
topframe3=Frame(root)
topframe3.pack(side='top')
button13=Button(topframe3,text=" .",padx=16,pady=16,fg='green',bd=3,command=lambda:setval(-1))
button13.pack(side='left')
button14=Button(topframe3,text="0",padx=16,pady=16,fg='black',bd=3,command=lambda:setval(0))
button14.pack(side='left')
button15=Button(topframe3,text=" /",padx=16,pady=16,fg='black',bd=3,command=lambda:oper(3))
button15.pack(side='left')
button16=Button(topframe3,text="=",padx=16,pady=16,fg='black',bd=3,command=lambda:displayanswer())
button16.pack(side='left')

root.mainloop()
