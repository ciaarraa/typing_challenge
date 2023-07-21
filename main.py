from urllib.request import urlopen
from difflib import SequenceMatcher
import time
import sys
from models.leaderboard import Leaderboard

if __name__ != '__main__':
    sys.exit(1)

def get_sentence():
     try:
             sentence =  urlopen("https://baconipsum.com/api/?type=meat-and-filler&sentences=1").read(2000).decode()
             sentence = sentence[2:sentence.find(".")]
     except:
         sentence = "Bacon has gone horribly wrong"
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
    leaderboard = Leaderboard()
    play_game = "y"
    while play_game == "y":
        start_game(leaderboard)
        play_game = input("Press y to play again and any other key to exit\n")
    leaderboard.show()

def start_game(leaderboard):
    name = get_username()
    print("Type the following sentence as fast as you can")
    countdown()
    sentence = give_sentence_to_user()
    time_and_answer = time_method_execution(get_input)
    accuracy  = calcualte_user_score(sentence, time_and_answer[1])
    print(f"Your accuracy was {accuracy}")
    score = calculate_score(time_and_answer[0], accuracy)
    print(f"Your score is: {score}")
    print(f"Nice, that took you: {round(time_and_answer[0], 2)} seconds")
    leaderboard.add(name, score, accuracy)

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
    return name

def calcualte_user_score(sentence, answer):
     score = SequenceMatcher(lambda x: x in " ", sentence, answer)
     return score.ratio()

def calculate_score(time, accuracy):
    score = 100*(1/time) + 100 * accuracy
    return round(score,2)

begin_game()

