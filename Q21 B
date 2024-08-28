##write a user defined functionin python named Puzzle(W,N) which takes the arguement W as an english word and N as an integer and returns the string where every Nth alphabet of the word W is replaced with an underscore 

def Puzzle(W, N):
    result = ''
    for i in range(len(W)):
        if (i + 1) % N == 0:  # Every Nth position
            result += '_'
        else:
            result += W[i]
    return result

# Example usage:
print(Puzzle("abcdefghij", 3))  # Output: "ab_def_ghi_"
