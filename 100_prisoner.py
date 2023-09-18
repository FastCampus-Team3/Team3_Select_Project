# 세 번째 파트: 성공률 계산 및 출력
def calculate_success_rate(runs=10000):
    successes = sum(will_all_prisoners_survive(create_random_drawers()) for _ in range(runs))
    print(f"Success rate over {runs} runs: {successes / runs * 100}%")
if __name__ == "__main__":
    calculate_success_rate()
