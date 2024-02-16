import random

print("Generating random numbers between 1 and 50")
print("Stopping when total is greater than 100")


total_number_count = 0

if total_number_count < 100:
    for x in range (2):
        print(random.randrange(1,50), end)
        print("Total so far:  ")

print(f'Loop was executed {total_number_count} times.')


