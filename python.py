import random 
import time 

def speedtest():
    words = ["elephant", "giraffe", "chocloate", "butterfly", "adventure"]
    word = random.choice(words)

    print("___________________________________________________________________")
    print(f"Type: {word}")
    input("press Enter to start")
    print("____________________________________________________________________")

    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"You took {time_taken}")
    else:
        print (f"the correct word is: {word}")

    input("Press enter to play again: ")
    speedtest()

if __name__ == "__main__":
    speedtest()