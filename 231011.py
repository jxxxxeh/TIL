import random

def get_number():
    return random.randrange(1, 46)

def set_lotto_number():
    lotto = []
    while len(lotto) <= 6:
        num = get_number()
        if num not in lotto:
            lotto.append(num)
    return lotto
    
def match_numbers(user_inputs, lotto_numbers):
    same_numbers = (set(user_inputs) & set(lotto_numbers))
    return same_numbers

def check_prize(same_numbers):
    if len(same_numbers) == 6:
        print('1st prize!')
    elif len(same_numbers) == 5:
        print('2nd prize!')
    elif len(same_numbers) == 4:
        print('3rd prize!')
    elif len(same_numbers) == 3:
        print('4th prize!')
    else:
        print('try next week!')


num = 0

print('** Start Lotto **')
print('1) Set the lotto numbers')
lotto_numbers = set_lotto_number()

print('2) Set the user inputs')
user_inputs = []

while True:
    num = int(input('Enter %d-number: '%(len(user_inputs)+1)))
    if num < 1 or num > 46:
        print('No valid number')
        continue
    if user_inputs.count(num) == 0:
        user_inputs.append(num)
    else:
        print('Same number')
        continue
    if len(user_inputs) >= 6:
        break

print('3) Match the numbers')
same_numbers = match_numbers(user_inputs, lotto_numbers)

print('4) Check the prize')
check_prize(same_numbers)

print('5) Sort the lists')
lotto_numbers.sort()
user_inputs.sort()

print('=== Summary ===')
print('Lotto numbers: ', *lotto_numbers)
print('User numbers: ', *user_inputs)