#list is a collection of values
#each value is stored in an element
#can hold different datatypes (including other list)

colors = ["red","blue","green","yellow"]
#display the list
print(colors)

#access elements by index
print(colors[1])

#from the end of a list
print(colors[-2])

#change a value
colors[2] = "white"
print (colors)

#slicing
#get values from a range of indexes
letters = ["a","b","c","d","e"]
print (f"First three letters: {letters[0:3]}")
#with slices the lower boundary is inclusive, the upper boundry is exlusive
#if starting at index 0 you can omit the lower range value
print (f"First three letters: {letters[:3]}")
#same idea from end
print (f"Last three letters: {letters[-3:]}")

#length of a list
print(len(letters))


# print(letters[54]) # Error


