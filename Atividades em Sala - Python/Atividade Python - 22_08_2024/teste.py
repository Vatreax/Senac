import tkinter as tk
from tkinter import ttk

restaurante_do_ederson = tk.Tk()
restaurante_do_ederson.resizable(False, False)
restaurante_do_ederson.geometry('600x300')
restaurante_do_ederson.title("Restaurante do Ederson")

# apply the grid layout
restaurante_do_ederson.grid_columnconfigure(0, weight=5)
restaurante_do_ederson.grid_rowconfigure(0, weight=5)

# create the text widget
text = tk.Text(restaurante_do_ederson, height=10)
text.grid(row=0, column=0, sticky=tk.EW)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(restaurante_do_ederson, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# add sample text to the text widget to show the screen
for i in range(1,50):
    position = f'{i}.0'
    text.insert(position,f'Lanche {i}\n');

restaurante_do_ederson.mainloop()