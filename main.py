from urllib.request import urlopen
import time

if __name__ != '__main__':
    sys.exit(1)

def get_sentence():
    text = urlopen("https://baconipsum.com/api/?type=meat-and-filler").read(2000).decode()
    text = text[2:text.find(".")]
    return text
    
def give_sentence_to_user():
    print(get_sentence())

def time_method_execution(method):
    start = time.time()
    method()
    end = time.time()
    total_time = end - start
    return total_time

def get_input():
    input()

def begin_game():
    get_username()
    print("Type the following sentence as fast as you can")
    countdown()
    give_sentence_to_user()
    time = time_method_execution(get_input)
    print(f"Nice, that took you: {round(time, 2)} seconds")

def countdown():
    print("3", end="..", flush=True)
    time.sleep(1)
    print("2", end="..", flush=True)
    time.sleep(1)
    print("1", end="..", flush=True)
    time.sleep(1)
    print("GO")

def get_username():
    name = input("Enter your name: ")
begin_game()
