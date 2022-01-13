from time import sleep
from selenium_handlers import Handler

def main():
    # Change sleeps so everything loads
    handler = Handler()

    continue_to_race = input()
    while continue_to_race != "q":
        handler.race()

    # End program by pressing enter in the console
    input()
    handler.quit()

if __name__ == "__main__":
    main()
