# Галкин Андрей
# Задача "Всё не так уж просто"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

#is_prime = True

for i in numbers:
    if i == 2:
        primes.append(i)
    for j in range (2, i):
        if i % j != 0 and i != j+1:
            continue
        elif i == j+1:
            primes.append(i)
        else:
            not_primes.append(i)
            break

print('Primes:', primes)
print('Not Primes:', not_primes)