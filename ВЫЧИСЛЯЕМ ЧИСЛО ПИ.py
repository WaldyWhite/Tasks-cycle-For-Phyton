import sys
n = int(sys.argv[1].strip())
p=round(4 * sum((-1.)**k / (2*k + 1) for k in range(n)),5)
print(p)
