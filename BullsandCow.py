from random import *

# 배열
random_numbers = []  # 서로 다른 세 숫자의 배열

# 세개 뽑을때까지 반복
while len(random_numbers) < 3:
    new_number = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_number in random_numbers:
        new_number = randint(0, 9)
    random_numbers.append(new_number)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print(random_numbers)

# 변수
strike = 0  # 스트라이크의 수
count = 1
try_count = 0 #시도횟수 카운트

while strike != 3:

    user_numbers = []  # 사용자가 입력한 임의의 숫자의 배열
    print("세 수를 하나씩 차례대로 입력하세요.")

    while len(user_numbers) < 3:
        temp = int(input("%d번째 수를 입력하세요: " % count))

        if temp in user_numbers:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        elif temp > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        else:
            user_numbers.append(temp)
            count += 1

    print(user_numbers)

    # 변수
    random_count = 0
    user_count = 0
    strike = 0
    ball = 0

    while random_count < 3:
        if random_numbers[random_count] == user_numbers[random_count]:
            strike+=1
        elif random_numbers[random_count] in user_numbers:
            ball+=1

        random_count += 1

    print("%dS %dB" % (strike, ball))

    try_count += 1
    count = 1

print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % try_count)
