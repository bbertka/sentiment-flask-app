#!/bin/bash

# Read the list of items from the file
while IFS= read -r item; do
  # URL encode the item (requires `jq` utility)
  encoded_item=$(jq -nr --arg item "$item" '$item|@uri')
  
  # Execute the curl command
  curl "http://sentiment.k3s.home.lab/sentiment?item=${encoded_item}"
done < ./items.txt
