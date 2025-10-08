t = int(input())
results = []
for _ in range(t):
    quiz = str(input())
    total = 0
    score = 1
    for i in range(len(quiz)):
        if(quiz[i] == 'O'):
            total += score
            score += 1
        else:
            score = 1
    results.append(total)

for result in results:
    print(result)
        
