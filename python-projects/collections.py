lst = [10,20,30,40,50]
lst.append(5) # add int to end of list
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40) # remove given value
lst.pop(2) # remove value at given index
print(lst)

lst.reverse() # reverses order of values in list, does not alter original list
print(lst)

lst.sort() # puts the list in ascending order
print(lst)


lst[0] = 500 # change value at given index
print(lst)

lst = lst[1:] # starts list at index 1 (slicing)
print(lst)

index3 = lst.index(7) # index(given value) like a getindex method
print(index3)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)

num20 = lst.count(20) #count(given value) returns number of times value occurs in list
print(num20)

lst_copy = lst # changing either changes the other, they are both pointing to same memory
print(lst_copy)
lst_copy[1] = 99
print(lst_copy)
print("original list", str(lst))


new_copy = lst.copy()
print(new_copy)
new_copy[0] = 1000
print(lst)
print(new_copy)

new_copy = lst[:]

empty_lst = []
for val in lst: # for each loop
    empty_lst.append(val)
print(empty_lst)


empty_lst = [0] * 10
print(empty_lst)
empty_lst[1] = 100
print(empty_lst)


squares = []
for i in range(1,10):
    squares.append(i**2)
print(squares)

plus_5 = [val + 5 for val in lst]
print(plus_5)

small_vals = [val for val in lst if val < 20]
print(small_vals)

fav_foods = {"Kathleen" : "pizza", "Maya" : "ice cream", "Tom" : "ice cream", "Eric" : "steak"} # crly brackets create dictionary
print(fav_foods)
mff = fav_foods["Maya"]
print(mff)

for key in fav_foods : 
    print(f"{key}'s favorite food is {fav_foods[key]}") 

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)