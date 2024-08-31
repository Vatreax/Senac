from tkinter import *
root = Tk()     #you must create an instance of Tk() first

image = PhotoImage(file=r'c:\Users\RafaelMontiel\Documents\imagens\bebidas\\agua_de_coco.png')
larger_image = image.zoom(2, 2)         #create a new image twice as large as the original
smaller_image = image.subsample(2, 2)   #create a new image half as large as the original

root.mainloop()