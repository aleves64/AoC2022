import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

handscores = {'A':1,'B':2,'C':3}
resultscores = {'X':0,'Y':3,'Z':6}
strategy = {
    ('X', 'A'): 'C',
    ('X', 'B'): 'A',
    ('X', 'C'): 'B',
    ('Y', 'A'): 'A',
    ('Y', 'B'): 'B',
    ('Y', 'C'): 'C',
    ('Z', 'A'): 'B',
    ('Z', 'B'): 'C',
    ('Z', 'C'): 'A'
}

totalscore = 0
for play in myinput:
    opponent = play[0]
    me = play[-1]
    roundscore = handscores[strategy[me,opponent]] + resultscores[me]
    totalscore += roundscore
print(totalscore)