# On the first line, you will be given the population (numbers separated by comma and space ", ").
# On the second line, you will be given the minimum wealth. You should distribute the wealth so
# that no part of the population has less than the minimum wealth. To do that, you should always take wealth
# from the wealthiest part of the population.

# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".


#              Example

# Input                       Output

# 2, 3, 5, 15, 75             [5, 5, 5, 15, 70]
# 5

# 2, 3, 5, 15, 75             [20, 20, 20, 20, 20]
# 20

# 2, 3, 5, 45, 45             No equal distribution possible
# 30


population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
total_wealth = sum(population)
while True:
    if total_wealth < len(population) * minimum_wealth:
        print("No equal distribution possible")
        break
    for number in range(len(population)):
        if population[number] < minimum_wealth:
            points_needed = minimum_wealth - population[number]
            population[number] += points_needed
            max_index = population.index(max(population))
            population[max_index] -= points_needed

    print(population)
    break
