from urllib.parse import urlparse, parse_qs
address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
print("All Parts: ",parts)
print("Query: ",parts.query, "\n")
query = parse_qs(parts.query)
print("DictionaryValuePairs= ",  query)
print("Query q: ", query['q'])
