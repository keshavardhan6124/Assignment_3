import random

def throw_die():
    return random.randint(1, 6)

def simulate_trials(num_trials):
    successes = 0
    for _ in range(num_trials):
        throws = [throw_die() for _ in range(6)]
        odd_count = sum(1 for throw in throws if throw % 2 != 0)
        if odd_count == 5:
            successes += 1
    return successes / num_trials

# Probability of 5 successes
num_trials = 1000000
prob_5_successes = simulate_trials(num_trials)
print(f"Probability of 5 successes: {prob_5_successes}")

# Probability of at least 5 successes
success_count = 0
for _ in range(num_trials):
    throws = [throw_die() for _ in range(6)]
    odd_count = sum(1 for throw in throws if throw % 2 != 0)
    if odd_count >= 5:
        success_count += 1
prob_at_least_5_successes = success_count / num_trials
print(f"Probability of at least 5 successes: {prob_at_least_5_successes}")

# Probability of at most 5 successes
success_count = 0
for _ in range(num_trials):
    throws = [throw_die() for _ in range(6)]
    odd_count = sum(1 for throw in throws if throw % 2 != 0)
    if odd_count <= 5:
        success_count += 1
prob_at_most_5_successes = success_count / num_trials
print(f"Probability of at most 5 successes: {prob_at_most_5_successes}")

