# 1
# 🚨 이 부분은 고치지 마세요 👇
two_digit_number = input("두 자리 숫자를 입력: \n")
# 🚨 이 부분은 고치지 마세요 👆

####################################
# 아래에 코드를 작성합니다. 👇
x = two_digit_number[0]
y = two_digit_number[1]
z = int(x) + int(y)
print(f'두 자리의 합은 {z}입니다.')

# 2
# 🚨 여기는 그대로 👇
height = input("키를 미터 단위로 입력하세요 : ")
weight = input("몸무게를 킬로 단위로 입력하세요 : ")
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
BMI = float(weight) / float(height)**2
print(f'당신의 BMI는 {round(BMI,2)} 입니다.')