rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "Ng", 
"Country" :"USA"
}
id1 = id(rec)
del rec

rec = {
    "Name" : "Python", 
    "Age":"20", 
    "Addr" : "Ng", 
    "Country" : "USA"
    }
id2 = id(rec)
print(id1 == id2)
 