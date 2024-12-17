import time

def sequence_sum(n):
    total = 0
    for i in range(n):
        next_num = i + 1
        current_sum = i + next_num
        total += current_sum
        print(f"{i} + {next_num} = {current_sum} (total = {total})")
        time.sleep(0.05)  # Add a 0.05-second delay between iterations

# Input and validation
while True:
    try:
        i = int(input("Введіть ціле додатнє число: "))
        if i <= 0:
            print("Число має бути додатнім!")
            continue
        sequence_sum(i)
        break
    except ValueError:
        print("Введіть коректне ціле число!")