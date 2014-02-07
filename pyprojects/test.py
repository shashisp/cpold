import requests
import json

# Aman's post time
AFTER = 2014-01-09T20:48:47+0000
TOKEN = 'CAACEdEose0cBAFmEWyu0RK3ZCxWS7ORVZCeEW4NgXlynXoTTFZCybViyZAShYZC2zydPmIU23nbzZCJZBHxMIVzG9foN3ZB7UUbTAwoeEHphbEoKOtxm88fuu2wREHkklKb0szSC6ytUB8Nve2dyydZAEgT11ydA74x8MsEjxwoOZBoSNos8F7OzSQJoFfFzzVpURM9TyzWf55JQZDZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time > 1353233754 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
    """Comments thank you on all posts"""
    #TODO convert to batch request later
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
        message = 'Thanks %s :)' % user['first_name']
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)

        print "Wall post %s done" % wallpost['post_id']

if __name__ == '__main__':
    commentall(get_posts())