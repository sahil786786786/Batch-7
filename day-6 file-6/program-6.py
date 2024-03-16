# 1.) Python program to capitalize the first and last character of each
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
'''


def capitalize_first_and_last(string):
    words = string.split()
    capitalized_words = []

    for word in words:
        if len(word) > 1:
            capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            capitalized_word = word.upper()
        capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)

# Example usage:
input_string = input("Enter a string: ")
output_string = capitalize_first_and_last(input_string)
print("Result:", output_string)


def check_conditions(num):
    if num % 1 == 0 and num % 2 == 0 and num % 8 == 0:
        return "Yes"
    else:
        return "No"

# Test with input 128
num=int(input("enter the number"))
output = check_conditions(num)
print("Output:", output)

'''

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

# Add corresponding elements of l1 and l2
ans = [l1[i] + l2[i] for i in range(len(l1))]

print("ans =", ans)
















