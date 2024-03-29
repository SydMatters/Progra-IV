import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import CTk, CTkFrame
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

'''
    Initialize the main window of the application.

    Args :
            title (str): Title of the window.
            size (tuple): Size of the window.

'''

class mainWindow(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')   
        self.minsize(size[0], size[1])

        self.menu = menu(self)
        self.graph = graph(self, self.menu)
        self.cuanti = table(self, self.menu)

        self.protocol("WM_DELETE_WINDOW", self.onCloseWindow)
        
    def onCloseWindow(self):
        self.destroy()  #Properly close window
        

#Create the menu and widgets
class menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=8, border_color='black', border_width=2)
        self.place(relx=0.02, rely=0.9, relwidth=0.5, relheight=0.08, anchor='nw')

        #Variables for the wave
        self.time = ctk.DoubleVar(value=1)
        self.amplitude = ctk.DoubleVar(value=1)
        self.freq = ctk.DoubleVar(value=60)
        
        self.create_widgets()


    #Create the widgets of the window.
    def create_widgets(self):
        time_label = ctk.CTkLabel(self, text='Time:', width=50, height=25, corner_radius=8)
        time_entry = ctk.CTkEntry(self, width=80, height=25, corner_radius=8, border_color='lime green', textvariable=self.time)
        time_scale = ctk.CTkSlider(self, width=160, height=18, from_=0, to=3,number_of_steps=2000, button_color='lime green', button_hover_color='lime green', variable=self.time,)
        amplitude_label = ctk.CTkLabel(self,text='Amplitude: ', width=120, height=25, corner_radius=8)
        amplitude_entry = ctk.CTkEntry(self,width=80,height=25,corner_radius=8,border_color='DodgerBlue4',textvariable=self.amplitude)
        amplitude_scale = ctk.CTkSlider(self,width=160,height=18,from_=1,to=6,number_of_steps=1000,variable=self.amplitude)
        frequency_label = ctk.CTkLabel(self,text='Frequency: ', width=120, height=25, corner_radius=8)
        frequency_entry = ctk.CTkEntry(self,width=80,height=25,corner_radius=8,border_color='red3',textvariable=self.freq)
        frequency_scale = ctk.CTkSlider(self,width=160,height=18,from_=1,to=240,number_of_steps=1000,button_color='red3',button_hover_color='red3',variable=self.freq)

        time_label.place(relx=0.07,rely=0.1,anchor='n')
        time_entry.place(relx=0.2,rely=0.1,anchor='n')
        time_scale.place(relx=0.17,rely=0.55,anchor='n')
        amplitude_label.place(relx=0.40,rely=0.1,anchor='n')
        amplitude_entry.place(relx=0.56,rely=0.1,anchor='n')
        amplitude_scale.place(relx= 0.48,rely=0.55,anchor ='n')
        frequency_label.place(relx= 0.75,rely=0.1,anchor= 'n' )
        frequency_entry.place(relx = 0.89,rely=0.1,anchor= 'n')
        frequency_scale.place(relx=0.79,rely=0.55,anchor='n' )

#Creates the graph.
class graph(ctk.CTkFrame):
    def __init__(self, parent, menu_instance):
        super().__init__(parent, corner_radius=8, fg_color='white', border_color='black', border_width=2)
        self.place(relx=0.02, rely=0.02, relwidth=0.5, relheight=0.87, anchor='nw')
        
        #Bring the variables from the menu
        self.menu = menu_instance
        self.menu.time.trace_add('write',self.createGraph)
        self.menu.amplitude.trace_add('write',self.createGraph)
        self.menu.freq.trace_add('write',self.createGraph)

        #Plot the axis
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self) 
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    #Plot the graph
    def createGraph (self, *args):
        time = self.menu.time.get()
        amplitude = self.menu.amplitude.get()
        freq = self.menu.freq.get()
        
        period = 1/freq

        timeArrange = np.arange(0,time,period/1000)
        signal = [sin(ti,amplitude,freq) for ti in timeArrange]

        self.ax.clear()
        self.ax.plot(timeArrange, signal, label='Signal', color='blue')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Señal Sinosoidal')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()
"""
Inicialize the table frame

Args: 
        parent (ctk.CTkFrame): The parent frame.
        menu_instance (ctk.CTkFrame): The menu instance.
"""
class table(ctk.CTkFrame):
    def __init__(self, parent, menu_instance):
        super().__init__(parent, corner_radius=8, fg_color='white', border_color='black', border_width=2)
        self.place(relx=0.53, rely=0.02, relwidth=0.45, relheight=0.96, anchor='nw')

        self.menu = menu_instance

        #Bring the variables from the menu
        self.menu.time.trace_add('write',self.codification)
        self.menu.amplitude.trace_add('write',self.codification)
        self.menu.freq.trace_add('write',self.codification)

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        self.tree = ttk.Treeview(self,columns=("Time","Signal","Codi"), yscrollcommand=scrollbar.set)

        self.tree.column('#0',anchor='center',width=50)
        self.tree.column("Time",anchor='center',width=150)
        self.tree.column("Signal",anchor='center',width=150)
        self.tree.column("Codi",anchor='center',width=150)

        self.tree.heading("#0",text="N",anchor='center')
        self.tree.heading("Time",text="Time",anchor='center')
        self.tree.heading("Signal",text="Signal",anchor='center')
        self.tree.heading("Codi",text="Codification",anchor='center')

        scrollbar.config(command=self.tree.yview)
        self.tree.pack(fill='both',expand=True)
    """
    This method takes the values from the menu and codifies them into binary format.
    It also creates the treeview with the values.
    """
    def codification(self, *args):
        time = self.menu.time.get()
        amplitude = self.menu.amplitude.get()
        freq = self.menu.freq.get()

        timeArrange = np.linspace(0, time, 1000)
        n = np.arange(0, 1000, 1)
        signal = [sin(ti, amplitude, freq) for ti in timeArrange]

        min_val = min(signal)
        max_val = max(signal)
    
        # Handle the case where max_val and min_val are equal
        if max_val == min_val:
            delta = 1
        else:
            delta = (max_val - min_val) / 16

        cuantiSignal = np.round((signal - min_val) / delta)

        # Handle the case where delta is zero
        if delta == 0:
            n_bits = 1
        else:
            maxCodi = np.nanmax(cuantiSignal)
            if np.isnan(maxCodi):
                n_bits = 1
            else:
                n_bits = int(np.ceil(np.log2(maxCodi + 1)))

        codiSignal = [format(int(val), f'0{n_bits}b') for val in cuantiSignal]

        self.tree.delete(*self.tree.get_children())

        for a, t, s, c in zip(n, timeArrange, signal, codiSignal):
            self.tree.insert("", "end", text=a, values=(f"{t:.3f}", f"{s:.3f}", c))


'''
Return sine of time with the given amplitude and frequency

Args:
    time (float): Time at wich to evaluate the sine.
    amplitude (float): Amplitude of the sine wave.
    frequency (float): Frequency of the sine wave.
'''
def sin(time,amplitude,frequency):
    omega = 2*np.pi*frequency
    return amplitude*np.sin(time * omega)

if __name__ == "__main__":
    app = mainWindow('Recuperación Parcial 2 Fisica III', (1080, 720))
    app.mainloop()
