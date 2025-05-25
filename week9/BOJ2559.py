n, k = map(int, input().split())
temperature = list(map(int, input().split()))

for i in range(1, n):
    temperature[i] += temperature[i-1]
if n == k:
    print(temperature[-1])
    exit()

diff = set()

temperature = [0] + temperature
for i in range(k, n+1):
    num = temperature[i] - temperature[i-k]
    diff.add(num)

print(max(diff))