from curses import wrapper
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(12,50,"Welcome to the Network Automation Tools\nEnter to continue....")
    stdscr.refresh()
    stdscr.getch()          ##to exit the screen
wrapper(main)