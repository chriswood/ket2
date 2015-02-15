# ket2
I'm re-writing kiteeatingtree.org using django rather than flask. I found myself spending too much time with the framework. This is certainly not an indictment of flask, I just found it not to be the most usefule tool for this particular job.

kiteeatingtree.org is a website I'm getting going to share things with family and friends and allow them to do the same.

TODO: (not prioritized, X = done)
add saving pacman to user edit save
view past/all posts (currently just last 10)
take special feedback posts
Add /feedback view listing all feedback posts
Add growl type notifications, or something
display posts per user
implement picture sharing
add password edit feature
add send someone a private message
add send a request to admin
add email user/users feature
AVATARS!!!
add "conversations" or replies to posts ot something
probably better add tests, even though it is "just" a website :)
move anonymous check to decorator ro something
Have homepage display list of who is logged in

X - let user edit his posts
X - GET RID OF CDN if I'm going to use font awesome. WAY too slow
X - add delete button to post for post owner
X - Revisit "logged in as" thing
X- add admin section with view/edit users function
X - write bash script to rsync with server and touch wsgi file
X- implement posts
X - display all posts
X- round off post corners or something it's tacky
X - add information section/"coming soon"
X - make user form error display not jump to top on error
X - Handle login/session
X - add validated user to session
X - check for validated user
X - Add login decorator
X - Fix when to show logged in as
X - create user
X - Add feedback on form submittal success for user/edit
X - add sqlite db
X - get schema going
X - split home page into posts and info
X - figure out envars
X - fix where edit screwed up create
X - edit user info
X - Fix OBNOXIOUS db permission error (www-data must own
    db file AND directory)
X - add posts to db

Future ideas for app:
-Have posts colors random or rotate complementing values
-Generalize everything, so that someone with little to no programming experience can create their family/group an instance of this
-maybe have design/stationery templates for emails/pages
-Give everyone a way to make todo lists

Run in shell..
import os
import sys
import django
import ket2
sys.path.append('/home/chris/code/ket2')
sys.path.append('/home/chris/code/ket2/ket2')
sys.path.append('/home/chris/code/ket2/ketapp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
