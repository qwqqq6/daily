# 修改颜色

from tkinter import *

window = Tk()
window.title('color')
window.geometry('500x500+460+40')


def bgColor(a):
    print(a)
    window.config(bg=('#%02x%02x%02x' % (rSlider.get(), gSlider.get(), bSlider.get())))


rSlider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=255, command=bgColor)
gSlider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=255, command=bgColor)
bSlider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=255, command=bgColor)
rSlider.pack(anchor=W)
gSlider.pack(anchor=W)
bSlider.pack(anchor=W)

window.mainloop()