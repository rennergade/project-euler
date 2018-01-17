def d(n):
  sum = 0
  for i in range(1,n):
    if n % i == 0:
      sum += i
  return sum

total = 0
for k in range(0,10001):
    if d(d(k)) == k and k != d(k):
        total += k

print total
