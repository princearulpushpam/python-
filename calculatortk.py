#caculator program

from tkinter import *
root=Tk()

root.config(width=500,height=600)
root.resizable(0,0)
root.title('calculator')

exp=''

def btn_click(item):

    global exp
    exp=exp+str(item)
    input_txt.set(exp)

def btn_clear():

    global exp
    exp=""
    input_txt.set("")


def btn_equal():

    global exp
    result=str(eval(exp))
    input_txt.set(result)
    exp=""

input_txt=StringVar()

in_frame=Frame(root,width=100,height=50,bg="white")

in_frame.pack(side=TOP)

in_field=Entry(in_frame,font=('Times 18 bold'),textvariable=input_txt,width=50,bg="#eee",justify=RIGHT)

in_field.grid(row=0,column=0)
in_field.pack(ipady=10)

btn_frame=Frame(root,width=312,height=272,bg="gray")
btn_frame.pack()

#row 0 clear/divide button

clear=Button(btn_frame,text='Clear',fg='black',width=32,height=3,bg='#eee',command=lambda:btn_clear())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide=Button(btn_frame,text= '/',fg="black",width=10,height=3,bg="#eee",command=lambda:btn_click("/"))
divide.grid(row=0,column=3,padx=1,pady=1)


#######   row 1 , 7,8,9,* buttons

seven=Button(btn_frame,text='7',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('7'))
seven.grid(row=1,column=0,padx=1,pady=1)


eight=Button(btn_frame,text='8',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('8'))
eight.grid(row=1,column=1,padx=1,pady=1)


nine=Button(btn_frame,text='9',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('9'))
nine.grid(row=1,column=2,padx=1,pady=1)


mul=Button(btn_frame,text='*',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('*'))
mul.grid(row=1,column=3,padx=1,pady=1)

############    row 2 4,5,6 buttons

four=Button(btn_frame,text='4',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('4'))
four.grid(row=2,column=0,padx=1,pady=1)


five=Button(btn_frame,text='5',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('5'))
five.grid(row=2,column=1,padx=1,pady=1)


six=Button(btn_frame,text='6',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('6'))
six.grid(row=2,column=2,padx=1,pady=1)


sub=Button(btn_frame,text='-',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('-'))
sub.grid(row=2,column=3,padx=1,pady=1)


################## row 3 1,2,3 buttons

one=Button(btn_frame,text='1',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('1'))
one.grid(row=3,column=0,padx=1,pady=1)


two=Button(btn_frame,text='2',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('2'))
two.grid(row=3,column=1,padx=1,pady=1)


three=Button(btn_frame,text='3',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('3'))
three.grid(row=3,column=2,padx=1,pady=1)


add=Button(btn_frame,text='+',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('+'))
add.grid(row=3,column=3,padx=1,pady=1)


##################  row 4 0,.,= buttons

zero=Button(btn_frame,text='0',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('0'))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)


point=Button(btn_frame,text='.',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_click('.'))
point.grid(row=4,column=2,padx=1,pady=1)


equ=Button(btn_frame,text='=',fg="black",width=10,height=3,bg="#fff",command=lambda:btn_equal())
equ.grid(row=4,column=3,padx=1,pady=1)


root.mainloop()