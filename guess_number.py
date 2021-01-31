# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴使用者 比答案大or小
import random
r = random.randint(1, 100)
while True:
	x = input('請輸入數字: ')
	x = int(x)
	if x == r:
		print('恭喜!猜對了!')
		break
	elif x > r:
		print('答錯了，比答案大。')
	elif x < r:
		print('答錯了，比答案小。')
