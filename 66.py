import math
result = 0;
pmax = 0;

for D in range (2, 1001):
    limit = int(math.sqrt(D))

    if (limit * limit == D):
        continue

    m = 0;
    d = 1;
    a = limit;
    numm1 = 1;
    num = a;
    denm1 = 0;
    den = 1;

    while(num*num - D*den*den != 1):
        m = d * a - m
        d = (D - m * m) / d
        a = (limit + m) / d

        numm2 = numm1
        numm1 = num
        denm2 = denm1
        denm1 = den

        num = a*numm1 + numm2
        den = a * denm1 + denm2
        if num > pmax:
            pmax = num
            result = D


print(result)
