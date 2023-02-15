import os
try:
    os.makedirs("./in")
except:
    print("in folder already exist")

try:
    os.makedirs("./out")
except:
    print("out folder already exists")