#!/bin/bash
#This script deletes a request to the URL paased as the first argument
curl -sX DELETE "$1"
