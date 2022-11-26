# 1-1 출력 연습1
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# 1-2 한 줄로 작성하며 줄 바꾸기
print("Hello world!\nHello world!")

# 1-3 출력 연습2
print("Day 1 - String Manipulation"
      + '\nString Concatenation is done with the "+" sign.'
      + '\ne.g. print("Hello " + "word"'
      + "\nNew lines can be created with a backslash and n.")

# 1-4 input 함수
print("Hello " + input("What is your name?"))

# 1-5 len 함수
print(len(input("What is your name?")))

# 1-6 변수1
name = input("What is your name?")
length = len(name)
print(length)

# 1-7 변수2
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)

# 촤종 미션 - 밴드명 생성기
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
name = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + name)