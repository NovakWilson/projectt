import tkinter as tk
from PIL import Image, ImageTk, EpsImagePlugin
import pyautogui
from app.cv import processing

class Drawing(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=1920, height=1080, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonPress-3>", self.on_button3_press)
        self.canvas.bind("<Motion>", self.on_move)

        self.line = None

        self.start_x = None
        self.start_y = None

        self.old_x = None
        self.old_y = None

        self.first_x = None
        self.first_y = None

        self._draw_image()

    def _draw_image(self):
        self.im = Image.open('screenshot.jpg')
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_im)

    def on_button_press(self, event):
        self.old_x = self.start_x
        self.old_y = self.start_y
        self.start_x = event.x
        self.start_y = event.y
        if self.old_x is not None:
            if abs(event.x - self.first_x) <= 10 and abs(event.y - self.first_y) <= 10:
                self.canvas.create_line(self.old_x, self.old_y, self.first_x, self.first_y, fill='red', tag="lines")
                self.line = None
                self.start_x = None
                self.start_y = None
                self.old_x = None
                self.old_y = None
                self.first_x = None
                self.first_y = None
                img = Image.open('screenshot.jpg')
                EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.56.1\bin\gswin64c'
                self.canvas.postscript(file='polygon' + '.eps')
                img = Image.open('polygon' + '.eps')
                img.save('polygon' + '.png', 'png')
                img = Image.open('polygon' + '.png')
                processing(img)
            else:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, fill='red', tag="lines")

        else:
            self.first_x = self.start_x
            self.first_y = self.start_y

        if not self.line:
            self.line = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill='red', tag="lines")

    def on_move(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        if self.start_x is not None:
            self.canvas.coords(self.line, self.start_x, self.start_y, curX, curY)

    def on_button3_press(self, event):
        self.canvas.delete('lines')
        self.line = None
        self.start_x = None
        self.start_y = None
        self.old_x = None
        self.old_y = None
        self.first_x = None
        self.first_y = None


def main():
    pyautogui.screenshot('screenshot.jpg', region=(0, 0, 1920, 1080))
    draw = Drawing()
    draw.mainloop()
