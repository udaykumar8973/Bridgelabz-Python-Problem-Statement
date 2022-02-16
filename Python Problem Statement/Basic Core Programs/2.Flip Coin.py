import random

n = int(input("Number of times you want to Flip Coin : "))
heads_count = 0
tails_count = 0
chances = 0

while chances != n:
    y = random.uniform(0, 1)

    if y < 0.5:
        tails_count += 1
        chances += 1
    else:
        heads_count += 1
        chances += 1

heads_percent = ((heads_count / (heads_count + tails_count)) * 100)
tails_percent = ((tails_count / (heads_count + tails_count)) * 100)

print("Heads percent: " + str(heads_percent))
print("Tails percent: " + str(tails_percent))