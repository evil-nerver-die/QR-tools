import qrcode
from qrcode import image
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Create window
wnd = Tk()
wnd.title('KoNs QR generator')
wnd.geometry('800x600')
wnd.config(bg='HotPink4')

headingFrame = Frame(wnd,bg="HotPink",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame,text="KoNs QR Generator", bg='LightPink', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

Frame1 = Frame(wnd,bg='HotPink4')
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1 = Label(Frame1,text="Enter text/URL: ",bg='HotPink4',fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)
text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(wnd,bg='HotPink4')
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
label2 = Label(Frame2,text="Enter location to save the QR Code: ",bg='HotPink4',fg='azure',font=('Courier',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)
loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=0.85, relheight=0.2)

def selectLoc():
    file = filedialog.askdirectory()
    loc.insert(0,str(file))

browse_butt = Button(Frame2,text="...",font=('Courier',13,'bold'),command=selectLoc)
browse_butt.place(relx=0.92,rely=0.4,relwidth=0.08,relheight=0.2)

Frame3 = Frame(wnd,bg='HotPink4')
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)
label3 = Label(Frame3,text="Enter name of QR code: ",bg='HotPink4',fg='azure',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)
name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame4 = Frame(wnd,bg='HotPink4')
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)
label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg='HotPink4',fg='azure',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)
size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)

def generateCode():
    qr = qrcode.QRCode(version=size.get(),
                        box_size=10,
                        border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img=qr.make_image()
    fileDirect=loc.get()+'\\'+name.get()
    img.save(f'{fileDirect}.png')
    messagebox.showinfo("KoNs QR Generator","QR Code is saved successfully !!")

button = Button(wnd, text='Generate Code',font=('Courier',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

wnd.mainloop()

