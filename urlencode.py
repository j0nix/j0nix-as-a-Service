import urllib.parse, sys
the_string = " ".join(sys.argv[1:])
print(urllib.parse.quote(the_string))
