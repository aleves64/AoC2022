import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

handscores = {'X':1,'Y':2,'Z':3}
resultscores = {
    ('X', 'A'): 3,
    ('X', 'B'): 0,
    ('X', 'C'): 6,
    ('Y', 'A'): 6,
    ('Y', 'B'): 3,
    ('Y', 'C'): 0,
    ('Z', 'A'): 0,
    ('Z', 'B'): 6,
    ('Z', 'C'): 3
}

totalscore = 0
for play in myinput:
    opponent = play[0]
    me = play[-1]
    roundscore = resultscores[(me,opponent)] + handscores[me]
    totalscore += roundscore
print(totalscore)