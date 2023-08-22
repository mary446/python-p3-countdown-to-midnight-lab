import time
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    return "HAPPY NEW YEAR!"


def countdown_with_sleep(number = '1'):
    while number > 0:
        time.sleep(number)
        print(f'{number} SECOND(S)!')
        number -= 1
    return "HAPPY NEW YEAR!" 