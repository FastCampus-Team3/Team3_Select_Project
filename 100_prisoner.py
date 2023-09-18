import random

# 첫 번째 파트: 서랍 생성
def create_random_drawers():
    drawers = list(range(100))
    random.shuffle(drawers)
    return drawers

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
  
# 세 번째 파트: 성공률 계산 및 출력
def calculate_success_rate(runs=10000):
    successes = sum(will_all_prisoners_survive(create_random_drawers()) for _ in range(runs))
    print(f"Success rate over {runs} runs: {successes / runs * 100}%")
if __name__ == "__main__":
    calculate_success_rate()

