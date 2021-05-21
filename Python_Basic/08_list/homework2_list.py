# 4. 2번 문제에서 학생들의 점수를 내림차순으로 출력
scores = []
total = 0
high = 0
stu = int(input('학생 수 입력 :'))
for i in range(stu):
    score = int(input('학생 %d 점수 입력 :'%(i+1)))
    scores.append(score)
    scores.sort(reverse=True)
    total += score
    if score >= 80:
        high += 1

print('총점 : %d' % total)
aver = total / (len(scores))
print('평균 : %.1f' % aver)
print('80점 이상 학생 : %d' % high)
print('점수 내림차순 정렬 :',scores)

print('===================================')
import random
# 5. 사자성어 맞추기 게임
# - 사자성어와 관련 뜻은 리스트 2개로 작성
# - 맞출때 까지 계속

a = ['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
b = ['잘못을 고치고 옮은 길에 들어섬','죽을 고비를 여러 번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람',
     '아무짝에나 쓸모 없는 것','고통과 즐거움을 함께 한다','미리 준비해두면 근심 걱정이 없다',
     '사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
     '생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤 일을 이룰 수 없다']

print('사자성어 맞추기 게임을 시작합니다')
print('-'*40,end='\n')
# ques = random.choice(b)

while True:
    ques = random.choice(b)
    print(ques)
    ans = input('이말의 사자성어는? :')
    if a.index(ans) == b.index(ques):
        print('맞습니다... 게임을 종료합니다')
        break
    else:
        print('틀렸습니다.... 다시 도전!')
        print()