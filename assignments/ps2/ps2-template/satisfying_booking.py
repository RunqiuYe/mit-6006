def mergeBooking(B1, B2):
    """
    For two bookings schedule B1 and B2 consisting of 
    (k,s,t) tuples, merge to form one single booking schedule.
    """
    print(f"B1: {B1}")
    print(f"B2: {B2}")
    res = []
    i, j = 0, 0
    m, n = len(B1), len(B2)
    while (i < m and j < n):
        ki, si, ti = B1[i]
        kj, sj, tj = B2[j]
        if sj >= ti:
            res.append((ki, si, ti))
            i += 1
        elif si >= tj:
            res.append((kj, sj, tj))
            j += 1
        elif sj > si:
            res.append((ki, si, sj))
            B1[i] = (ki, sj, ti)
        elif si > sj:
            res.append((kj, sj, si))
            B2[j] = (kj, si, tj)
        # si = sj
        elif ti < tj:
            res.append((ki + kj, si, ti))
            i += 1
            B2[j] = (kj, ti, tj)
        elif ti > tj:
            res.append((ki + kj, si, tj))
            j += 1
            B1[i] = (ki, tj, ti)
        else:
            res.append((ki + kj, si, ti))
            i += 1
            j += 1
        if len(res) > 1:
            prevk, prevs, prevt = res[-2] 
            curk, curs, curt = res[-1]
            if prevk == curk and prevt == curs:
                res.pop()
                res.pop()
                res.append((prevk, prevs, curt))
    while (i < m):
        res.append(B1[i])
        i += 1
        if len(res) > 1:
            prevk, prevs, prevt = res[-2] 
            curk, curs, curt = res[-1]
            if prevk == curk and prevt == curs:
                res.pop()
                res.pop()
                res.append((prevk, prevs, curt))
    while (j < n):
        res.append(B2[j])
        j += 1
        if len(res) > 1:
            prevk, prevs, prevt = res[-2] 
            curk, curs, curt = res[-1]
            if prevk == curk and prevt == curs:
                res.pop()
                res.pop()
                res.append((prevk, prevs, curt))
    print(f"res: {res}")
    return res


def createBooking(R, lo, hi):
    """
    For request R consists of tuples (s,t), create corresponding 
    booking schedule consists of (k,s,t) tuples.
    """
    if hi - lo < 1:
        return []
    if hi - lo == 1:
        s, t = R[lo]
        return [(1, s, t)]
    mid = lo + (hi - lo) // 2
    left = createBooking(R, lo, mid)
    right = createBooking(R, mid, hi)
    return mergeBooking(left, right)

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    # YOUR CODE HERE #
    ##################
    temp = list(R)
    n = len(R)
    B = createBooking(temp, 0, n)
    return tuple(B)
