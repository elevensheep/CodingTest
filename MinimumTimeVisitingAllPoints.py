# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
# 2D 그래프에, 정수 좌표들 points[i] = [xi, yi]인 n 포인트들이 있다. 주어진 모든 포인트들을 순서대로 방문하는데 걸린 최소시간 (초)를 반환
# You can move according to these rules:
# 너는 룰에 따라 움직일 수 있다.
# In 1 second, you can either:
# 1초에 너는 다음을 할 수 있다 :
# move vertically by one unit,
# 한 단위 수직으로 이동,
# move horizontally by one unit, or
# 한 단위 수평으로 이동 또는
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# 대각선으로 루트2 단위 이동 ( 다른말로 한 단위의 수직과 수평으로 1 초 이동 )
# You have to visit the points in the same order as they appear in the array.
# 너는 지점을 방문해야만 한다 같은 순서로 배열에서 그들이 나타난
# You are allowed to pass through points that appear later in the order, but these do not count as visits.
# 너는 따른다 나중에 나타난 순서의 지점을 관통하는, 그러나 이것은 방문 순서로 세지 않음
# coordinates : 좌표, vertically : 수직으로, horizontally : 수평으로, 
