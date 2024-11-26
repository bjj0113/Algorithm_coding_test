# 설탕문제
num = int(input())
bag = 0
 # num = 5x + 3y 로 이루어져있음
 # num - 3y = 5x <-가 최대가 될 수 있게..
 # x가 최대가 되게, 불가능하면 -1 출력

while num >= 0: 
    if num % 5 == 0: #5kg로만 나누어 떨어지면 출력
        bag += (num // 5)
        print(bag)
        break
  
    num -= 3 # 3kg 빼주고 가방개수 1늘린 후 다시
    bag += 1
  
else: #모든 경우가 안되면 -1 출력
    print(-1)