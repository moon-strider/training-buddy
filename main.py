from front.windows import tkinterApp

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
    window = tkinterApp()
    window.geometry('1280x720')

    window.mainloop()