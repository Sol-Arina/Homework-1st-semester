def factorial(n):
    if n == 0: 
        return 1
    #print(n)
    return(n * factorial(n - 1))



def permutation(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i in s:
        remaining = [x for x in s if x != i]
        another = permutation(remaining)
        for t in another:
            permutations.append([i] + t)
    return permutations  