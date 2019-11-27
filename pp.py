import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fbox
list=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto",
      "if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned",
      "volatile","while","void"]
window=tk.Tk()
window.title("C text Editor")
window.geometry("1000x800")
menu1=tk.Menu(window)
window.config(menu=menu1)
fileMenu=tk.Menu(menu1)
editMenu=tk.Menu(menu1)
menu1.add_cascade(label="File",underline=0,menu=fileMenu)
menu1.add_cascade(label="Edit",underline=0,menu=editMenu)
def openfile():
    filename=fbox.askopenfilename(initialdir=r"./",title="Open file",filetypes=[("All files","*.*")] )
def save():
    filename=fbox.asksaveasfilename(initialdir=r"./",title="Save file",filetypes=[("All files","*.*")] )

Lb = tk.Listbox(window) 
Lb.insert(1, 'C')

Lb.insert(3, ' Java') 
Lb.insert(5, 'C++') 
Lb.insert(7, 'Python 3') 
Lb.insert(9, 'Python') 
Lb.insert(11, 'C#') 
Lb.insert(13, 'Scala') 
Lb.insert(15, 'Javascript') 
Lb.selection_set( first = 0 )
textbox=tk.Text(window,wrap=tk.NONE,width=300,height=29)
inputtextbox=tk.Text(window,wrap=tk.NONE,width=30,height=10)
outputtextbox=tk.Text(window,wrap=tk.NONE,width=60,height=2)
input_text=textbox.get('1.0','10.0')
print(input_text)

#str1="""Enter Your Code Here..."""
#textbox.insert(tk.INSERT,str1)
#textbox.tag_add("str", "1.0", "1.4")
#textbox.tag_config("str", background="yellow", foreground="blue")

fileMenu.add_command(label="New",underline=0,command=openfile)
fileMenu.add_command(label="Open",underline=1,command=openfile)
fileMenu.add_command(label="Save",underline=2,command=openfile)
fileMenu.add_command(label="Save as",underline=3,command=save)
fileMenu.add_command(label="Close",underline=4,command=openfile)
label1 = tk.Label(window, text='INPUT',height=6) 
label2 = tk.Label(window, text='OUTPUT',height=4)
#Output Button
Run =tk.Button(window,text="Run",bg="burlywood1",width=10,height=3)
#grid
Lb.grid(row=0,column=0,ipadx=10,ipady=10,sticky='ns'); 
textbox.grid(row=0,column=1,columnspan=20,sticky='nw',padx=10)

label1.grid(row=1,column=0,sticky='e')
inputtextbox.grid(row=1,column=1,pady=20)
Run.grid(row=1,column=2,padx=2)
label2.grid(row=2,column=0,sticky='e')
outputtextbox.grid(row=2,column=1,padx=2)

window.mainloop()