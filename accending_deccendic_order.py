
accend_deccend={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}


l=list(accend_deccend.items())
l.sort()          
print('Ascending order is',l) 
l=list(accend_deccend.items())
l.sort(reverse=True) 
print('Descending order is',l)
# dict=dict(l) 
# print("Dictionary",dict) 
