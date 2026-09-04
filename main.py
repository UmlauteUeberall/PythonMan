# This is a sample Python script.
import curses
from Program import Program


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program = Program()
    curses.wrapper(program.Run)



