# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево,
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака
# существуют монеты с номиналами 1, 5, 10, 25
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.

cost = int(input())
count = 0
while cost >= 25:
    count += 1
    cost -= 25
while cost >= 10:
    count += 1
    cost -= 10
while cost >= 5:
    count += 1
    cost -= 5
while cost >= 1:
    count += 1
    cost -= 1
print(count)
