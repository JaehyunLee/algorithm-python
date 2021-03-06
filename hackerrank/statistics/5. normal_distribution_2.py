# Day 5: Normal Distribution 2 - 정규 분포
# 평균이 m이고 표준편차가 s일때 엔트로피를 최대화하는 확률 분포


def normal_distributions(mean, std, x):
    from math import erf
    return 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))


m, s = map(float, input().split())
a = float(input())
b = float(input())

print(round((1 - normal_distributions(m, s, a)) * 100, 2))
print(round((1 - normal_distributions(m, s, b)) * 100, 2))
print(round(normal_distributions(m, s, b) * 100, 2))
