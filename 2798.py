# combinations 사용으로 조합 구하기
from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

result = 0

for combo in combinations(card, 3):
    card_sum = sum(combo)
    if card_sum <= m:
        result = max(result, card_sum)

print(result)
