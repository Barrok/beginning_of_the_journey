#Library pygal is needed, because im going to show frequency of results on histogram
import pygal as pg

#I need function randint, so there's no reason to import whole random module
from random import randint

#At first let's make a class of our dices
class Dice():
    def __init__(self, faces = 8):
        self.faces = faces

    def roll(self):
        return randint(1, self.faces)

#there's no die roll without dice, so make 2
dice_1 = Dice()
dice_2 = Dice()

#Ok, we have 2 dices, but now we're gong to make 10k rolls and put result in list 'results'
results = []
for roll in range(10000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#Analysis of results
frequency = []
max_result = dice_1.faces + dice_2.faces
for value in range(2, max_result + 1):
    freq = results.count(value)
    frequency.append(freq)

#Now it's time to make a histogram
hist = pg.Bar()
hist.force_uri_protocol = 'http'

#hist exist, but it's 'raw' and now i have to put some information on it
hist.title = 'Result of 10k rolls of 2 octagonal dices'
hist.x_labels = ['2', '3', '4', '5', '6', '7','8','9','10','11','12','13','14','15','16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of results'
hist.add('D8+D8', frequency)

#All that's left is to save this histogram as svg file
hist.render_to_file('two_D8_rolls.svg')
