# You have a list of your favourite marvel super heros.
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']



#1. Length of the list
print("Length of array: ", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print("After adding black panther: ", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
# heros[3] = 'black panther'
#better way:
heros.insert(3,'black panther')
print("after adding again after hulk: ", heros)

# 4. Now you don't like thor and hulk because they get angry easily:) So you want to remove thor and hulk from list and replace them with doctor strange(because he is cool). Do that with one line of code.

# heros.remove('hulk')
# heros.remove('thor')
# heros.append('doctor strange')
# better way :
heros[1:3] = ['doctor strange']
print("after removing hulk & thor , adding doctor strange: ",heros)

#5. Sort the heros list in alphabetical order(Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("Sorted List: ",heros)