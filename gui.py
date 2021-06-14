from comms import Comms
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
        
        # Start serial communication
        self.comms = Comms()

    def showMM(self):
        """Shows the main menu and asks allows the user to press a key.
        Each key press results in the corresponding serial command being sent."""

        # Add main elements to screen
        self.screen.addstr(1, int((self.maxXY[1]/2)-6), "Sony DVD Remote")
        menuOptions = ["[o] Power", "[c] Play", "[s] Stop", "[p] Pause", "[b] Next", "[B] Previous"]
        menuMappings = {'o': 0x15,
                        'c': 0x32,
                        's': 0x38,
                        'p': 0x39,
                        'b': 0x31,
                        'B': 0x70}

        for i in range(0, 6, 2):
            # Add left
            self.screen.addstr(i+5, int(self.maxXY[1]/10), menuOptions[i])
            # Add right
            self.screen.addstr(i+5, int((self.maxXY[1]/10)*9)-len(menuOptions[i+1]), menuOptions[i+1])

        # Update screen
        self.screen.refresh()

        while True:
            sel = self.screen.getkey()[0]
            if (sel == 'q'):
                break

            value = menuMappings.get(sel)
            if (value == None):
                # Flash to alert user their choice was not an option
                curses.flash()
            else:
                self.comms.sendMessage(value)            

            self.screen.addch(self.maxXY[0] - 1, 1, sel)
            self.screen.refresh()

        curses.endwin()
