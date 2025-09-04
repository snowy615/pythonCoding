def count_cow(Glis, Hlis):
    count = 0
    front = Glis[0]
    back = Glis[1]-Glis[0]-1
    if front + back >= 2:
        count += front*back
    front = Glis[-1] - Glis[-2] - 1
    back = n-Glis[-1]-1
    if front + back >= 2:
        count += front * back

    for i in range(1, len(Glis)-1):
        back = (Glis[i+1] - Glis[i] - 1)
        front = (Glis[i]-Glis[i-1]-1)
        if back == 0 and front>=2:
            count += front-1
        elif front == 0 and back >= 2:
            count += back-1
        elif back == 1:
            count += (front-1)*2+1
        elif front == 1:
            count += (back-1)*2-1
        else:
            count += (front+1)*(back+1)-3

    front = Hlis[0]
    back = Hlis[1] - Hlis[0] - 1
    if front + back >= 2:
        count += front * back
    front = Hlis[-1] - Hlis[-2] - 1
    back = n - Hlis[-1] - 1
    if front + back >= 2:
        count += front * back

    for i in range(1, len(Hlis)-1):
        back = (Hlis[i + 1] - Hlis[i] - 1)
        front = (Hlis[i] - Hlis[i - 1] - 1)
        if back == 0 and front>=2:
            count += front-1
        elif front == 0 and back >= 2:
            count += back-1
        elif back == 1:
            count += (front - 1) * 2 + 1
        elif front == 1:
            count += (back - 1) * 2 - 1
        else:
            count += (front + 1) * (back + 1) - 3
    return count