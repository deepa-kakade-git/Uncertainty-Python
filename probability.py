"""
For each of the following, write a function, and repeatedly use it to simulate the probability of an event occurring with the following chances:

$\frac{2}{7}$
$\frac{1}{10}$
$\frac{1}{100}$
$1$
"""
import random

# Exercise 1
def cal_probability(num_trials:int , p_ratio: int):
    event_counter = 0
    for _ in range (num_trials):
      if random.random() < p_ratio:
       event_counter +=1
    return event_counter / num_trials

print("Probability for frac{2}{7} :" + str(cal_probability(10000, (2/7))))
print("Probability for frac{1}{10} :" + str(cal_probability(10000, (1/10))))
print("Probability for frac{1}{100} :" + str(cal_probability(10000, (1/100))))

# Exercise 2

bag1 = ["Red"] * 4 + ["Green"] * 4
bag2 = ["Red"] * 4 + ["Green"] * 4 + ["Yellow"] * 10
bag3 = ["Red"] * 0 + ["Green"] * 4 + ["Yellow"] * 10

def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)

def simulate_red_prob(bag: list):
    number_of_repetitions = 10000
    samples = [pick_a_token(container=bag) for repetition in range(number_of_repetitions)]
    return sum(token == "Red" for token in samples) / number_of_repetitions


print(" Probability of red token for a bag with 4 red tokens and 4 green tokens :" + str(simulate_red_prob(bag1)))
print(" Probability of red token for a bag with 4 red tokens, 4 green tokens and 10 yellow tokens :" + str(simulate_red_prob(bag2)))
print(" Probability of red token for a bag with 0 red tokens and 4 green tokens :" + str(simulate_red_prob(bag3)))

# Exercise 3

bag4 = ["Red"] * 3 + ["Blue"] * 4

print( "Probability of red token for a bag with 3 red tokens and 4 blue tokens :" + str(simulate_red_prob(bag4)))

def sample_experiment(bag):
    """
    This samples a token from a given bag and then
    selects a coin with a given probability.

    If the sampled token is red then the probability
    of selecting heads is 2/3 otherwise it is 1/2.

    This function returns both the selected token
    and the coin face.
    """
    selected_token = pick_a_token(container=bag)

    if selected_token == "Red":
        probability_of_selecting_heads = 4 / 5
    else:
        probability_of_selecting_heads = 2 / 3

    if random.random() < probability_of_selecting_heads:
        coin = "Heads"
    else:
        coin = "Tails"
    return selected_token, coin

red_counter = 0
head_counter = 0
head_red = 0

for _ in range(10000):
    if pick_a_token(bag4) == "Red":
        red_counter +=1
        if random.random() < (4/5):
            head_counter += 1
            head_red +=1
    else:
        if random.random() < (2/5):
            head_counter += 1



print("Probability of picking a red token is :" + str(red_counter/10000))
print("Probability of obtaining Heads :" + str(head_counter/10000))
print("Probability of having selected a red token if a heads is obtained, approximate the  :" + str(head_red/10000) + "\n")

# Exercise 4
#Probability_car = 1/2 , probability_car_late = 1/5,
#probability_bicycle = 1/6, probability_bicycle_late = 2/5
#probability_foot = 1/3, , probability_foot_late = 1/10


print("Approximate the probability that an individual travels by foot and is late." + str(1/3 *1/10))
print("Approximate the probability that an individual is not late :" + str(1 - (1/5 + 2/5 + 1/10)))
print("Given that an individual is late, approximate the probability that they did not travel on foot. :" + str(1-(1/10)))




