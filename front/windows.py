import tkinter as tk

from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import ttk
from datetime import datetime

from utilities.utilities import input_meal, input_stats

LARGEFONT = ('Verdana', 35)

BASE_WIDTH = 1280
BASE_HEIGHT = 720

# FIXME: add date selection (calendar widget?) to inputs
  
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self, width=BASE_WIDTH, height=BASE_HEIGHT) 
        container.pack(side = 'top', fill = 'both', expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {} 
  
        for F in (StartPage, InputMeal, InputStats):
            frame = F(container, self, width=BASE_WIDTH, height=BASE_HEIGHT)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ='nsew')
  
        self.show_frame(StartPage)
  

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

  
class StartPage(tk.Frame):
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT, bg="black"):
        tk.Frame.__init__(self, parent, width=width, height=height, bg=bg)

        label = ttk.Label(self, text ='Training buddy', font = LARGEFONT)

        label.grid(row = 0, column = 1, padx = 450, pady = 10)

        input_meal_btn = tk.Button(self, text ='Input Meal',
            command = lambda : controller.show_frame(InputMeal), width=40, height=3)
        input_meal_btn.grid(row = 1, column = 1, padx = 250, pady = 40)

        input_stats_btn = tk.Button(self, text ='Input Stats',
            command = lambda : controller.show_frame(InputStats), width=40, height=3)
        input_stats_btn.grid(row = 2, column = 1, padx = 250, pady = 40)


def generate_header(parent, controller, title: str):
    back_btn = tk.Button(parent, text ='Back',
        command = lambda : controller.show_frame(StartPage), width=40, height=3)
    back_btn.grid(row = 0, column = 0, padx = 20, pady = 20)

    title_label = ttk.Label(parent, text=title, font = LARGEFONT)
    title_label.grid(row = 0, column = 1, padx = 180, pady = 20)

    return back_btn, title_label


class InputMeal(tk.Frame):
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT, bg="black"):
        tk.Frame.__init__(self, parent, width=width, height=height, bg=bg)

        self.types = {
            'date': str,
            'calories': int,
            'carbs': int,
            'proteins': int,
            'fats': int,
            'is_healthy': lambda x: False if x == 'No' else True,
        }

        self.title = 'Input Meal'
        back_btn, title_label = generate_header(self, controller, self.title)

        date_label = tk.Label(self, text='Date')
        calories_label = tk.Label(self, text='Calories')
        carbs_label = tk.Label(self, text='Carbs')
        proteins_label = tk.Label(self, text='Proteins')
        fats_label = tk.Label(self, text='Fats')
        is_healthy_label = tk.Label(self, text='Is healthy')

        date_entry = DateEntry(self)
        calories_entry = tk.Entry(self)
        carbs_entry = tk.Entry(self)
        proteins_entry = tk.Entry(self)
        fats_entry = tk.Entry(self)
        is_healthy_entry = tk.Entry(self)

        self.names = ['date', 'calories', 'carbs', 'proteins', 'fats', 'is_healthy']
        self.labels = [date_label, calories_label, carbs_label, proteins_label, fats_label, is_healthy_label]
        self.entries = [date_entry, calories_entry, carbs_entry, proteins_entry, fats_entry, is_healthy_entry]

        for i, item in enumerate(self.labels):
            item.grid(row=i+1, column=0, padx=190, pady=20, columnspan=2)

        for i, item in enumerate(self.entries):
            item.grid(row=i+1, column=1, padx=10, pady=20)

        (yyyy, mm, dd) = list(map(lambda x: int(x), datetime.today().strftime('%Y-%m-%d').split('-')))
        self.calendar = Calendar(self, selectmode = 'day', year = yyyy, month = mm, day = dd)
        #self.calendar.grid(row=1, column=2, rowspan=7)

        btn_enter = tk.Button(self, text='Enter', width=20, height=2, command=lambda: self.enter())
        btn_enter.grid(row=7, column=1, pady=50)

    def enter(self):
        payload = []
        for i, entry in enumerate(self.entries):
            name = self.names[i]
            try:
                payload.append(self.types[name](entry.get()))
            except Exception:
                showwarning(title="Warning!", message=f"Make sure that the {name} entry is correct")
                return
        
        (mm, dd, yyyy) = self.calendar.get_date().split('/')
        date = f'{dd if len(dd) == 2 else "0" + dd}.{mm if len(dd) == 2 else "0" + mm}.{"20" + yyyy}'

        try:
            input_meal(date, *payload)
        except Exception as e:
            showerror('Error', e)


class InputStats(tk.Frame): # TODO: copy from input stats
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT, bg="black"):
        tk.Frame.__init__(self, parent, width=width, height=height, bg=bg)

        self.title = 'Input Stats'
        back_btn, title_label = generate_header(self, controller, self.title)

        date_label = tk.Label(self, text='Date')
        weight_label = tk.Label(self, text='Weight')
        hr_label = tk.Label(self, text='HR')
        steps_label = tk.Label(self, text='Steps')
        age_label = tk.Label(self, text='Age')

        date_entry = tk.Entry(self)
        weight_entry = tk.Entry(self)
        hr_entry = tk.Entry(self)
        steps_entry = tk.Entry(self)
        age_entry = tk.Entry(self)      # load it from prev

        for i, item in enumerate([date_label, weight_label, hr_label, steps_label, age_label]):
            item.grid(row=i+1, column=0, padx=190, pady=20, columnspan=2)

        for i, item in enumerate([date_entry, weight_entry, hr_entry, steps_entry, age_entry]):
            item.grid(row=i+1, column=1, padx=10, pady=20)

        btn_enter = tk.Button(self, text='Enter', width=20, height=2)
        btn_enter.grid(row=7, column=1, pady=50)


# TODO: add input exercise with a list of exercises and their respective caloric costs