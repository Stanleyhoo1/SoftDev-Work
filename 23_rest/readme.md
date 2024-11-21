DISCO: 
You can load images and text from the API request by indexing into the JSON dictionary
response.read() reads the data that is recieved in JSON format, then use json.loads() to convert it to dictionary
requests.urlopen() opens the url

QCC:
Are all the JSON formats the same or do they differ from each request?