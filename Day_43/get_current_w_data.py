import json, requests, sys

if len(sys.argv) <2:
    print("location")
    sys.exit()
location = " ".join(sys.argv[1:])