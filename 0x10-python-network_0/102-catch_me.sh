#!/bin/bash
#This script sends a request to a server that causes the server to respond with You got me!
curl -s -X PUT -H "origin: HolbertonSchool" -d"User_id=98" 0.0.0.0:5000/catch_me
