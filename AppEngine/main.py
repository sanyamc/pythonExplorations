import os

print 'Content-Type: text/plain' 
print '' 

for env in os.environ:
    print env ,": " , os.environ[env]