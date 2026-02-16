import time
import winsound



def playWinBeepSound(frequency=3000, duration=1000):
    try:
        winsound.Beep(frequency, duration)
    except RuntimeError as e:
         print(f"Error: {e}")


def countdown_timer(seconds):
    while seconds > 0:
        print(f" {seconds} ")
        playWinBeepSound()
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    playWinBeepSound(2000, 1000)

i = int(input("Enter the number of seconds to count down: "))
countdown_timer(i)