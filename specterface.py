import tkinter as tk
import sys
import cv2
import PIL
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# implement a text message on the window as a class

class TMessage(tk.Frame):
    def __init__(self,parent,message):
        super(TMessage,self).__init__(parent)

        self.label = tk.Label(self,text=message)
        self.label.pack(padx=20,pady=20)


class Button(tk.Frame):
    def __init__(self,parent,comm,txt,is_quit):
        super(Button,self).__init__(parent)

        if is_quit:
            self.button = tk.Button(parent,text='quit',command=self.quit)
        else:
            self.button = tk.Button(parent,text=txt,command=comm)
        self.button.pack()

    def quit(self):
        sys.exit()

# function to get frame from camera
def frame_capture():
    cap = cv2.VideoCapture(0)
    retval,image = cap.read()

    return image

class FrameCanvas(tk.Frame):
    def __init__(self,fig,ax,parent):
        super(FrameCanvas,self).__init__(parent)
        self.fig = fig
        self.ax = ax

        self.canvas = FigureCanvasTkAgg(self.fig,master=parent)
        self.canvas.get_tk_widget().pack()

    def update_canvas(self,img):
        self.ax.imshow(img)
        self.canvas.draw()

class Spec_Main():
    def __init__(self,root):
        root.attributes('-type', 'dialog')
        self.create_figax()

        t_mess = TMessage(root,"Spectropy")
        t_mess.pack(side=tk.TOP)

        canv = FrameCanvas(self.fig,self.ax,root)
        canv.pack(side=tk.LEFT)

        frbut = Button(root,lambda: self.take_pic(canv),"Take spectrum",False)
        frbut.pack(side=tk.RIGHT)

        qbut = Button(root,None,None,True)
        qbut.pack(side=tk.BOTTOM)

    def create_figax(self):
        self.fig,self.ax = plt.subplots()

    def take_pic(self,canv):
        canv.update_canvas(frame_capture())


if __name__ == "__main__":

    root = tk.Tk()
    sm = Spec_Main(root)
    root.mainloop()

