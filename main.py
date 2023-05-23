import tkinter as tk

from utilities.utilities import input_stats

# IMPORTANT
# TODO: load from jsons and build graphs
# TODO: maximums and daily caloric goal bars etc
# TODO: add input meal and stats screens
# TODO: generate LMS and log trend line on graphs
# TODO: add settings screen
# TODO: add settings.json file containing paths to files etc
# TODO: add calendars screens to check meals and stats etc

# LATER
# TODO: add csv support

if __name__ == '__main__':
    window = tk.Tk(className='Training buddy')
    window.geometry('1280x720')
    program_name = tk.Label(text='Training buddy')

    input_meal_btn = tk.Button(text="Input meal", width=25, height=5)
    input_stats_btn = tk.Button(text="Input stats", width=25, height=5)



    program_name.pack()
    input_meal_btn.pack()
    input_stats_btn.pack()

    window.mainloop()