nums = []

for i in range(20):
    n = int(input(f'Digite o {i+1}° número: '))
    nums.append(n)

par = [x for x in nums if x % 2 == 0]
impar = [x for x in nums if x % 2 != 0]

print("Todos:", nums)
print("Par:", par)
print("Ímpar:", impar)
