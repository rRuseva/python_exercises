
def queueOR(q1, q2):
    result_q = []
    # result_q = q1 + q2
    # result_q.append(q2)
    for item in q1:
        result_q.append(item)
    for item in q2:
        result_q.append(item)

    return result_q


def queueAND(q1, q2):
    result_q = []

    N = len(q1)
    M = len(q2)

    i = 0
    if(N > M):
        small_q = q2[:]
        big_q = q1[:]
    else:
        small_q = q1[:]
        big_q = q2[:]
    while(small_q):
        curr_item = small_q.pop(0)
        if(curr_item in big_q):
            result_q.append(curr_item)

    return result_q


def queuePnotQ(q1, q2):
    p = q1[:]
    q = q2[:]
    result_q = []

    while(p):
        item = p.pop(0)
        if item not in q:
            result_q.append(item)

    return result_q


if __name__ == '__main__':
    print("hello")
    q1 = [1, 4, 6, 3, 8, 5, 2]
    q2 = [3, 9, 0, 32, 1, 6, 5]

    q_OR = queueOR(q1, q2)
    print("OR: ", q_OR)

    q_AND = queueAND(q1, q2)
    print("AND: ", q_AND)

    print("pNOTq: ", queuePnotQ(q1, q2))
