def even_odd_string(n):
    # This function will produce a string of length n
    # for each index i in the string s:
    # if i is even s[i]="0", otherwise s[i]="1"
    this_str = ""
    for i in range(n):
        if i % 2 == 0: # i is even
            this_str += "0"
        else: # i is odd 
            this_str += "1"
    return this_str

str1 = even_odd_string(5)
print(f"str1 = {str1}")

str2 = even_odd_string(4)
print(f"str2 = {str2}")

print(f"str1 + str2 = {str1 + str2}")
