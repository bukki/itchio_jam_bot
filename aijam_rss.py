import feedparser, time, tweepy

## AI__JAM application keys
CONSUMER_KEY = 'XBLN4XaLvkaDMiiD5sQOxnB1F'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'MOrzJdvNanHaiAavHnFD2qTUdSh7ea2b49hqIxDelpa3eC3fDs'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3037222146-ERw5JWSggOjhAYD9qkRKTJJGH9mrkP5PIqKkeWw'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'n3UpHGO5DuzXKUmJpsZFbEHeKU5YB91sUQBpFZuY7Lb5e'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

## read AIJAM feed XML document
#d = feedparser.parse('http://itch.io/feed/new.xml')
d = feedparser.parse('http://itch.io/jam/ai-game-jam/feed')

# parse XML
from bs4 import BeautifulSoup
bs = BeautifulSoup(d.feed.summary)

# get date to track
from datetime import datetime
last_check = datetime.now()

while (True):
	time.sleep(900.0) # wait 15 minutes
	print 'woke up!'
	d = feedparser.parse('http://itch.io/jam/ai-game-jam/feed')
	bs = BeautifulSoup(d.feed.summary)
	for c in bs.find_all('a'):
		# check time of event for publishing
		if c.has_attr('class') and ('event_time' in c.get('class')):
			pub_date = datetime.strptime(c.get('title'), '%Y-%m-%d %H:%M:%S')
		#if c.has_attr('class') and ('event_time' in c.get('class')):
		#	pub_date = c.get_text()
		#	pub_delay = re.search(r'[\d]+', pub_date).group(0)
		
		# if new, post name and url
		if c.has_attr('class') and ('object_title' in c.get('class')) and pub_date > last_check:
			print last_check - pub_date
			twt = '@zookae AIJAM game!!! check out %s at %s' % (c.get_text(), c.get('href'))
			print twt
			api.update_status(status=twt)
	last_check = datetime.now() # update time for checking

# ref: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/



#while(true):
#for game in d.entries:
	# test for new
#	pub_date = time.strptime(game.published, '%a, %d %b %Y %H:%M:%S %Z')
	#if pub_date < last_check:
#	if pub_date < last_check:
		# tweet if new since last check
		#twt = 'another game joins the #AIJAM! check out %s at %s' % (game.title, game.link)
#		twt = '@zookae [test] check out %s at %s' % (game.title, game.link)
#		api.update_status(status=twt)

#last_check = time.gmtime()
#time.sleep(300) # wait 5 minutes