import random

num = int(input("Number of times you want to Flip Coin : "))
heads_count = 0                  # track heads count
tails_count = 0                  # track tails count
chances = 0                      # initially chances is equal to zero

while chances != num:
    coin = random.uniform(0, 1)  # gives a random floating-point number in the range [0.0, 1.0)

    if coin < 0.5:
        tails_count += 1
        chances += 1
    else:
        heads_count += 1
        chances += 1

heads_percent = ((heads_count / (heads_count + tails_count)) * 100)
tails_percent = ((tails_count / (heads_count + tails_count)) * 100)

print("Heads percent: " + str(heads_percent))
print("Tails percent: " + str(tails_percent))