# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.
chicken=open('data/chicken.txt','r')
sum=0
count=0
for i in chicken:
    test=i.split(": ")
    sum=int(test[1])+sum
    count= count +1

print(sum/count)

# 파일 닫기
