class Leaderboard(object):
    def __init__(self):
        self.members  = []

    def add(self, name, score, accuracy): 
        self.members.append({"name": name, "score":score, "accuracy": accuracy})

    def show(self):
        for i in range(len(self.members)):
            print(f"name: {self.members[i]['name']}, score: {self.members[i]['score']}, accuracy: {self.members[i]['accuracy']} ")
