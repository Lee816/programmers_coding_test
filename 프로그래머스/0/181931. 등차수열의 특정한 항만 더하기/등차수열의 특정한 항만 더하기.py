def solution(a, d, included):
    return sum([a+d*x for x in range(len(included)) if included[x]])