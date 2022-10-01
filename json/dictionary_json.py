import json

tweet = {
	"tweetText" : "Hello",
	"likes" : 3,
    "retweets" : 10,
    "timestamp" : "2022-07-01 00:12:03 PM",
	"authorID" : 1,
    "tweetID" : 100
}

#print(tweet["likes"])
#print(tweet["tweetID"])
print(json.dumps(tweet))