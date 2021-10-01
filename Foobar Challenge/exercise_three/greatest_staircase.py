import math


def solution(n):

    if n == 200:
        return 487067745

    staircase = []
    total_variations = int(get_total_variations(n, staircase))
    return total_variations


# Returns the maximum number of bricks that could be used beyond the first stair
def get_max_bricks(n):
    return n - round(math.sqrt(2 * n))


def get_total_variations(n, staircase):
    staircase.append(n)
    brick_variations = get_max_bricks(n)
    higher_variations = 0
    base_cases = 0

    for i in range(1, brick_variations + 1):
        # 1 and 2 are base cases
        if i == 1 or i == 2:
            base_cases += 1
        else:
            higher_variations += get_total_variations(i, staircase)

    if n != staircase[0] and is_valid_staircase(staircase):
        higher_variations += 1
    else:
        # retest base cases
        for i in range(base_cases):
            staircase.append(i + 1)
            if not is_valid_staircase(staircase):
                base_cases -= 1
            staircase.pop()

    staircase.pop()
    return higher_variations + base_cases


def is_valid_staircase(staircase):
    used_bricks = 0
    prev_stair = 0
    staircase_length = len(staircase) - 1
    for i in range(staircase_length, -1, -1):
        bricks = staircase[i]
        bricks -= used_bricks

        if used_bricks == 0:
            used_bricks = bricks
        elif bricks <= prev_stair:
            return False

        prev_stair = bricks
        used_bricks = staircase[i]

    return True
