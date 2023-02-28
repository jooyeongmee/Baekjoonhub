import sys

T = int(input())
for i in range(T):
  M = int(sys.stdin.readline())
  data = []
  for j in range(int(M/10) + 1):
    input_list = sys.stdin.readline().split()
    data.append(input_list)
  data = sum(data, [])
  data = list(map(int, data))
  # print(data)
  
  medians = []
  for j in range(len(data)):
    if j % 2 == 0:
      new_list = sorted(data[:j+1])
      medians.append(new_list[int(j/2)])
  # print(medians)

  len_medians = len(medians)
  print(len_medians)
  if len_medians <= 10:
    print(' '.join(map(str, medians)))
  else:
    while int(len(medians) / 10) != 0: 
      print(' '.join(map(str, medians[:10])))
      medians = medians[10:]
    print(' '.join(map(str, medians)))
    
      
      
