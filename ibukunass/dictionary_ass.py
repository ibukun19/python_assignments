
#clear(): This method is used remove all the elements from the dictionary.


Girl = {
    "name" : "Folashade"

    
}
Girl.clear()
print(Girl)

#copy: This method is used to return a copy of the dictionary.


Book = {
     "name" : "The black book",
     "type" : "Fantacy",
     "year" : 2025  
}
Book.copy()
print(Book)


#fromkeys(): This method is used to return a dictionary with the specified keys and value.

A = ('key1'), ('key2'), ('key3')
B = (45), (50), (55)
thisdict = dict.fromkeys (A, B)
print(thisdict)

#get(): This method is used to return the value of the specified key.

Results = {
    "mathematics": "A",
    "physics" : "B",
    "english" : "c"
}
x = Results.get("mathematics")
print(x)


#items: This method is used to return a list containing a tuple for each key value pair.

Book = {
     "name" : "The black book",
     "type" : "Fantacy",
     "year" : 2025  
}
x = Book.items()
print(x)


#keys: This method is used to return a list containing the dictionary's keys.

Results = {
    "mathematics": "A",
    "physics" : "B",
    "english" : "c"
}
x = Results .keys()
print(x)

#pop: This method is used to remove the element with the specified key.


Academy = {
    "organization": "School",
    "name"        : "Surepath",
    "location"    : "Lagos",
    "year"        : 2000

}
Academy.pop("name")
print(Academy)

#popitem: This is used to remove the last inserted key-value pair.


Academy = {
    "organization": "School",
    "name"        : "Surepath",
    "location"    : "Lagos",
    "year"        : 2000

}
Academy.popitem()
print(Academy)


#setdefault(): This method is used to return the value of the specified key. If the key does not exist: insert the key, with the specified value.


Results = {
    "mathematics": "A",
    "physics" : "B",
    "english" : "c"
}
x = Results.setdefault("Business","B")
print(x)


#update(): This method is used to Update the dictionary with the specified key-value pairs.


Girl = {
    "name" : "Folashade"
    
}
Girl.update({"age" : "11"})
print(Girl)


#values(): This method is used to return a list of all the values in the dictionary.


Book = {
     "name" : "The black book",
     "type" : "Fantacy",
     "year" : 2025  
}
x = Book.values()
print(x)
  









