# import required libraries
import tkinter

# create the window
window = tkinter.Tk() # instance
window.title("MilesMeter: Mile(s) to Km Converter") # application title
window.config(background="white",padx=10,pady=30) # background color, padding
window.minsize(300,100) # height


# create a welcome label
# welcome_label = tkinter.Label()
# welcome_label["text"] = ""
# welcome_label.config(bg='white', fg='black',font = ("Courier New", 15,'bold'))
# welcome_label.grid(row=0,column=0)

# create a miles label
miles_label = tkinter.Label()
miles_label["text"] = "Miles"
miles_label.config(bg='white', fg='black',font = ("Courier New", 15))
miles_label.grid(row=1,column=3)

# create a text entry box to collect miles
miles_input = tkinter.Entry()
miles_input.grid(row=1,column=2)
miles_input.config(bg='white', fg='black',font = ("Courier New", 15),width=5)

# is equal to label
equal_to_label = tkinter.Label()
equal_to_label["text"] = "is equal to"
equal_to_label.config(bg='white', fg='black',font = ("Courier New", 15))
equal_to_label.grid(row=6,column=0)

# result label
result_label = tkinter.Label()
result_label["text"] = "0"
result_label.config(bg='white', fg='black',font = ("Courier New", 15))
result_label.grid(row=6,column=2)

# run a constant while loop to keep the window listening
window.mainloop()