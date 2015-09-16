#
# Database access functions for the web forum.
#

import psycopg2
import time

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    pg = psycopg2.connect("dbname=forum")
    c = pg.cursor()
    query = "select time, content from posts order by time;"
    c.execute(query)
    results = c.fetchall()
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in results]
    pg.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    pg = psycopg2.connect("dbname=forum")
    c = pg.cursor()
    query = "insert into posts(content) values('%s');" % content
    c.execute(query)
    pg.commit()
    pg.close()
