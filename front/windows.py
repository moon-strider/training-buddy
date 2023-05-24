import tkinter as tk
from tkinter import ttk

LARGEFONT = ('Verdana', 35)

BASE_WIDTH = 1280
BASE_HEIGHT = 720
  
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
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT):
        tk.Frame.__init__(self, parent, width=width, height=height)

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
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.title = 'Input Meal'

        back_btn, title_label = generate_header(self, controller, self.title)

        calories_label = tk.Label(self, text='Calories')
        carbs_label = tk.Label(self, text='Carbs')
        proteins_label = tk.Label(self, text='Proteins')
        fats_label = tk.Label(self, text='Fats')
        is_healthy_label = tk.Label(self, text='Is healthy')

        calories_entry = tk.Entry(self)
        carbs_entry = tk.Entry(self)
        proteins_entry = tk.Entry(self)
        fats_entry = tk.Entry(self)
        is_healthy_entry = tk.Entry(self)      # load it from prev

        for i, item in enumerate([calories_label, carbs_label, proteins_label, fats_label, is_healthy_label]):
            item.grid(row=i+1, column=0, padx=190, pady=20, columnspan=2)

        for i, item in enumerate([calories_entry, carbs_entry, proteins_entry, fats_entry, is_healthy_entry]):
            item.grid(row=i+1, column=1, padx=10, pady=20)


class InputStats(tk.Frame):
    def __init__(self, parent, controller, width=BASE_WIDTH, height=BASE_HEIGHT):
        tk.Frame.__init__(self, parent, width=width, height=height)
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