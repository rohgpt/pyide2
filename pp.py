import tkinter as tk
from tkinter import ttk
import tkinter.colorchooser as colbox
import tkinter.filedialog as fbox
#KEYWORD******************************************************************************************************
list=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto",
      "if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned",
      "volatile","while","void"]
#creating window************************************************************************************************
window=tk.Tk()
window.title("C text Editor")
window.geometry("1000x800")

#creating Menubar *********************************************************************************************
menu1=tk.Menu(window)
window.config(menu=menu1,bg="brown4")
fileMenu=tk.Menu(menu1,tearoff=False)
editMenu=tk.Menu(menu1,tearoff=False)

def aboutus():
      frame2 = tk.Toplevel(window)
      display = tk.Label(frame2, text="This is Text Editor Designed for Coding in All the Language....",width=50,height=20)
      
      display.pack()    
theme=tk.Menu(menu1,tearoff=False)
about=tk.Menu(menu1,tearoff=False)
menu1.add_cascade(label="File",menu=fileMenu)
menu1.add_cascade(label="Edit",menu=editMenu)
menu1.add_cascade(label="Theme",menu=theme)
menu1.add_cascade(label="About",menu=about)
about.add_command(label="Info",command=aboutus)

#adding function to file menu************************************************
def openfile(event):
    filename=fbox.askopenfilename(initialdir=r"./",title="Open file",filetypes=[("All files","*.*")] )
def save(event):
    filename=fbox.asksaveasfilename(initialdir=r"./",title="Save file",filetypes=[("All files","*.*")] )
#children of file menu***************************************************************************
fileMenu.add_command(label="New",accelerator='Ctrl+N',command=lambda event:textbox.delete(1.0,tk.END))
window.bind("<Control-n>", lambda:textbox.delete(1.0,tk.END))


fileMenu.add_command(label="Open",accelerator='Ctrl+o',command=openfile)
window.bind("<Control-o>", openfile)
fileMenu.add_command(label="Save",accelerator='Ctrl+s',command=save)
window.bind("<Control-s>", save)
fileMenu.add_command(label="Save as",accelerator='Ctrl+Shift+s',command=save)
window.bind("<Control-Shift-s>", save)
fileMenu.add_separator() 
fileMenu.add_command(label="Close",underline=4,command=window.quit)


#adding children and function to edit menu ***************************************************************
editMenu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda:textbox.event_generate("<Control c>"))
editMenu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda:textbox.event_generate("<Control v>"))
editMenu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda:textbox.event_generate("<Control x>"))
editMenu.add_command(label='Clear All', accelerator='Ctrl+Alt+X', command= lambda:textbox.delete(1.0, tk.END))

#creating list box************************************************************************

Lb = tk.Listbox(window,font=('Arial',15,'bold'),)
Lb.insert(1, ' C')
Lb.insert(2, '\n\n')
Lb.insert(3, ' Java') 
Lb.insert(4, '\n\n')
Lb.insert(5, ' C++') 
Lb.insert(6, '\n\n')
Lb.insert(7, ' Python 3') 
Lb.insert(8, '\n\n')
Lb.insert(9, ' Python') 
Lb.insert(10, '\n\n')
Lb.insert(11, ' C#') 
Lb.insert(12, '\n\n')
Lb.insert(13, ' Scala') 
Lb.insert(14, '\n\n')
Lb.insert(15, ' Javascript') 
Lb.selection_set( first = 0 )
#creating scroll bar and source code textbox*****************************************
frame1=tk.Frame(window)

#scrollbar
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
#text box
l1="1.0"
def retrieve_input(event):
    z=textbox.index(tk.INSERT)
    global l1
    inputValue=textbox.get( l1,z)
    l1=z
    l=inputValue.split()
   # textbox.tag_configure( foreground="black")
    
    for i in l:
          
          if i in list:

                 textbox.tag_add(i,"%d.%d" % (int(z[0]),int(z[2])-len(i)-1), "%d.%d" %( int(z[0]),int(z[2]) ))
                 textbox.tag_configure(i, foreground="blue", font='bold')
          

      
    
      
                
  
   # textbox.insert(tk.INSERT,inputValue)
           
   

textbox=tk.Text(frame1,wrap=tk.NONE,yscrollcommand = scrollbar.set ,width=75,height=22,bg="black",foreground="white",highlightcolor="yellow",font=('Arial',15),insertbackground="Yellow")

window.bind("<space>", retrieve_input)
#input_text=tk.Text.index(1,4)
#print(input_text)
scrollbar.config( command = textbox.yview )
#input-output textbox

inputtextbox=tk.Text(window,wrap=tk.CHAR,width=30,height=10,bg="black",foreground="white")
outputtextbox=tk.Text(window,wrap=tk.CHAR,width=60,height=2,bg="black")


#str1="""Enter Your Code Here..."""
#textbox.insert(tk.INSERT,str1)
#textbox.tag_add("str", "1.0", "1.4")
#textbox.tag_config("str", background="yellow", foreground="blue")
#theme ***********************************************
def choosecolor1():
      color=colbox.askcolor()
      textbox.config(bg=color[1])
      if(color=="white"):
            window.config(bg="white")
      else:
           window.config(bg="brown4") 
def choosecolor():
      color=colbox.askcolor()
      textbox.config(foreground=color[1])
theme.add_command(label="Text editor Color",command=choosecolor1)
theme.add_command(label="Text Color",command=choosecolor)
#label for input output and Run button***************************************************
label1 = tk.Label(window, text='INPUT',height=6,bg="yellow") 
label2 = tk.Label(window, text='OUTPUT',height=4,bg="yellowgreen")
#Output Button 
Run =tk.Button(window,text="Run",bg="burlywood1",width=10,height=3)

#alignment of list box and Source code textbox******************************************
Lb.grid(row=0,column=0,ipadx=10,ipady=10,sticky='ns'); 
textbox.pack(side=tk.LEFT)
frame1.grid(row=0,column=1,columnspan=20,padx=10)
#alignment of input output box,un button,label********************************
label1.grid(row=1,column=0,sticky='e')
inputtextbox.grid(row=1,column=1,pady=20)
Run.grid(row=1,column=2,padx=2)
label2.grid(row=2,column=0,sticky='e')
outputtextbox.grid(row=2,column=1,padx=2)
#***************************************************************************
window.mainloop()