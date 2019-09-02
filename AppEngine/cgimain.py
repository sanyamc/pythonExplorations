import os

print 'Content-Type: text/plain'  # done so that browser understands the response type and print it accordingly
print '' 

for env in os.environ:
    print env ,": " , os.environ[env]