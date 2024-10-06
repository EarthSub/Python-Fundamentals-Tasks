list_of_integers = input().split()
list_of_integers = [int(x) for x in list_of_integers]
remover = int(input())

for _ in range(remover):
    list_of_integers.remove(min(list_of_integers))

print(", ".join(map(str, list_of_integers)))