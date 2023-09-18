import random

# 첫 번째 파트: 서랍 생성
def create_random_drawers():
    drawers = list(range(100))
    random.shuffle(drawers)
    return drawers
