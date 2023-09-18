# 두 번째 파트: 시뮬레이션
def will_all_prisoners_survive(drawers):
    for start in range(100):
        seen = set()
        i = start
        for _ in range(50):
            if i == start:
                break
            seen.add(i)
            i = drawers[i]
        else:
            if len(seen) == 50 and i not in seen:
                return False
    return True
