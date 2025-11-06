"""Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false

SOLUTION:

How i got the result:
1.- Looking for string methods in google.
2.- The most useful method was endswith()
3.- I use an if operator to validate the end of the first string and returns True or False depending if the first string
    ends with the second string.

"""



def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

    pass
