my_set4={"Hola",23.3,False}
print(my_set4)
empty_set={}
print(type(empty_set))
empty_set=set()
print(type(empty_set))
my_list=[1,1,1,2,3,4,5]
my_set=set(my_list)
print(my_set)
my_tuple=("hola","Hola","Hola",1)
my_set1=set(my_tuple)
print(my_set1)
my_set={1,2,3}
print(my_set)
my_set.add(4)
print(my_set)
my_set.update([1,2,5])
print(my_set)
my_set.update((1,7,2),{6,8})
print(my_set)
my_set.discard(1)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(10)
print(my_set)
#my_set.remove(12)#Da error KeyError, no existe el 12
#print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)
my_set1={3,4,5}
my_set2={5,6,7}
my_set3= my_set1 | my_set2
print(my_set3)
my_set3= my_set1 & my_set2
print(my_set3)
my_set3= my_set1 - my_set2
print(my_set3)
my_set3= my_set2 - my_set1
print(my_set3)
my_set3= my_set1 ^ my_set2
print(my_set3)

