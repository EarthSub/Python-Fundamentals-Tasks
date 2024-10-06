money_string = input().split(", ")
number_of_beggars = int(input())
money_string = [int(money) for money in money_string]
beggar_index = 0
list_of_money_of_the_beggars = []

for _ in range(number_of_beggars):
    beggars_sum = 0
    for num in range(beggar_index, len(money_string), number_of_beggars):
        beggars_sum += money_string[num]
    beggar_index += 1
    list_of_money_of_the_beggars.append(beggars_sum)

print(list_of_money_of_the_beggars)