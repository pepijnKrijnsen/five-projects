#############
#### API ####
# Let's build an API frontend to a very simple .csv file!
# Goal: an API that can be used by any IO device (web, local GUI) to interface 
# with a .csv file of people and animals.

#################
#### IMPORTS ####


######################
#### HAUGHTY CORE ####

class retrieve:
    
    def connect(self, db):
        f = open(db)
        return f
    
#    def query(self, f):
        
c = retrieve()
fiob = c.connect("family.csv")
file = fiob.read()
print(file)
