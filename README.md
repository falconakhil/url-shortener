# URL-Shortener

Backend for URL shortener in django

API:\
1.POST: Can be sent to /add/ . Expects json object with 'long_url'\
2.DELETE: Can be sent to /delete/ . Expects json object with 'key' as unique key.\
3.GET: Can be sent to /get/ .   Needs any one of 'long_url', "short_url' or 'key' and returns json  object of all three.