from random import randint
voca_file= open('vocabulary.txt', 'r') //참고하는 파일 열기

DIC_VOCA={} //사전에 보카넣기

for voca in voca_file:
    temp=voca.split(":") //임시적을로 단어 저장
    dic_voca[temp[0].strip()]=temp[1].strip()

index=list(dic_voca.keys()) //key값을 리스트에 저장

while True:
    random_num=randint(0,len(index)-1)
    korean=input("%s: " %index[random_num])

    if dic_voca[index[random_num]]== korean:
        print("맞았습니다!")
    else:
        if korean=="q":
            break

        print("틀렸습니다.정답은 %s입니다" %dic_voca[index[random_num]])


