import sys
#집합 S의 문자열 개수 N과 검사해야 하는 문자열 개수 M을 int 타입으로 입력 받는다.
N, M = map(int, input().split()) 


S = []   #집합 S
count = 0    #M개의 문자열 중 총 몇 개가 집합 S에 포함되어 있는지 세는 변수
for i in range(N):
  str = sys.stdin.readline().strip()
  S.append(str)

for i in range(M):
  tosearch = sys.stdin.readline().strip()
  if tosearch in S:
    count += 1

print(count)
    