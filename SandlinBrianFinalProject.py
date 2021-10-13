import tkinter
from tkinter.constants import DISABLED  # to disable the Original Pizza checkbox
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame,
                                    text='Sandlins Pizzeria'
                                         '\n "SALE $15.00 PIZZA!"')

        # Create three IntVar objects to use with
        # the Checkbuttons.
        self.cb_var0 = tkinter.IntVar()
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        # Set the intVar objects to 0.
        # !!! CHANGE 1, set var0 to 1 to get selected as default !!!
        self.cb_var0.set(1)
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)

        # Create the Checkbutton widgets in the top_frame.
        # !!! CHANGE 2, set the state to DISABLED to avoid changes by user
        self.cb0 = tkinter.Checkbutton(self.top_frame,
                                       text='Original Pizza $15.00',
                                       variable=self.cb_var0,
                                       state=DISABLED
                                       )
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Pepperoni $1.50',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Pineapple $0.75',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Anchovy $1.50',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='Jalapeno $0.50',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Mushroom $0.50',
                                       variable=self.cb_var5)

        # Pack the Checkbuttons.
        self.label1.pack(side='top')
        self.cb0.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Submit',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.

    def show_choice(self):
        # Create a message string.
        self.message = 'Your Pizza Topping Order Summary:\n'
        # total
        total = 0

        # Determine which Checkbuttons are selected and
        # build the message string accordingly and
        # add the price of toppings to the total.
        if self.cb_var0.get() == 1:
            self.message = self.message + 'Pizza\n'
            total += 15.00
        if self.cb_var1.get() == 1:
            self.message = self.message + 'Pepperoni\n'
            total += 1.50
        if self.cb_var2.get() == 1:
            self.message = self.message + 'Pineapple\n'
            total += 0.75
        if self.cb_var3.get() == 1:
            self.message = self.message + 'Anchovy\n'
            total += 1.50
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Jalapeno\n'
            total += 0.50
        if self.cb_var5.get() == 1:
            self.message = self.message + 'Mushroom\n'
            total += 0.50
        # print total with two digits after the decimal
        self.message = self.message + "Total : $%.2f" % total

        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Checkout', self.message)


# Create an instance of the MyGUI class.
my_gui = MyGUI()