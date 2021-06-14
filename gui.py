import curses

class Gui:

    def __init__(self):
        # Initialise curses main screen
        self.screen = curses.initscr()
        # Get screen size
        self.maxXY = self.screen.getmaxyx()

        # Set curses settings
        curses.curs_set(0) # Set cursor to invisible
        curses.noecho()    # Don't echo back characters

    def showMM(self):
        self.screen.addstr(1, int((self.maxXY[1]/2)-6), "Sony DVD Remote")
        self.screen.refresh()

        # Quit after one character entered
        self.screen.getch()
        curses.endwin()
