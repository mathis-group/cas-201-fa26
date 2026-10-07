def odds(n):
    # This function will produce the first n positive odd numbers
    the_odds = []
    i = 0
    while len(the_odds) < n:
        i += 1
        if i % 2 == True:
            the_odds.append(i)
        else:
            print(f"{i} is even")
        
    return the_odds

my_odds = odds(5)
print(f"my_odds = {my_odds}")