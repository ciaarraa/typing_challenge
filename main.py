from urllib.request import urlopen
from difflib import SequenceMatcher
import time
import sys

if __name__ != '__main__':
    sys.exit(1)

def get_sentence():
     try:{
             sentence :=  urlopen("https://baconipsum.com/api/?type=meat-and-filler").read(2000).decode(),
             sentence := sentence[2:text.find(".")]
             }
     except:{
             sentence := "Bacon has gone horribly wrong"
             }
     return sentence

def give_sentence_to_user():
    sentence = get_sentence()
    print(sentence)
    return sentence

def time_method_execution(method):
    start = time.time()
    answer = method()
    end = time.time()
    total_time = end - start
    return [total_time, answer]

def get_input():
    return input()

def begin_game():
    play_game = "y"
    while play_game == "y":
        start_game()
        play_game = input("Press y to play again\n")
    sys.exit(0)

def start_game():
    get_username()
    print("Type the following sentence as fast as you can")
    countdown()
    sentence = give_sentence_to_user()
    time = time_method_execution(get_input)
    score = calcualte_user_score(sentence, time[1])
    print(f"Your score is: {score}")
    print(f"Nice, that took you: {round(time[0], 2)} seconds")

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

def calcualte_user_score(sentence, answer):
     score = SequenceMatcher(lambda x: x in " ", sentence, answer)
     return score.ratio()

begin_game()
