# ket2
I'm re-writing kiteeatingtree.org using django rather than flask. I found myself spending too much time with the framework. This is certainly not an indictment of flask, I just found it not to be the most usefule tool for this particular job.

kiteeatingtree.org is a website I'm getting going to share things with family and friends and allow them to do the same.

TODO: (not prioritized, X = done) 
take special feedback posts 
Add /feedback view listing all feedback posts 
Add growl type notifications, or something 
add information section/"coming soon" 
X - make user form error display not jump to top on error 
implement posts
add delete button to post for post owner 
display all posts
display posts per user 
let user edit his posts 
implement picture sharing 
add password edit feature 
add send someone a private message 
add send a request to admin 
add email user/users feature 
write bash script to rsync with server and touch wsgi file
add admin section with view/edit users function 
AVATARS!!! 
round off post corners or something it's tacky 
add "conversations" or replies to posts ot something
probably better add tests, even though it is "just" a website :)
move anonymous check to decorator ro something

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


-----APACHE CONF
domain: kiteeatingtree.org
public: /var/www/kiteeatingtree.org/public_html/

# Admin email, Server Name (domain name), and any aliases ServerAdmin chris@kiteeatingtree.org ServerName www.kiteeatingtree.org ServerAlias kiteeatingtree.org

# Index file and Document Root (where the public files are located) 
DirectoryIndex index.html DocumentRoot /var/www/kiteeatingtree.org/ket
# Log file locations
LogLevel warn CustomLog /var/www/kiteeatingtree.org/ket/log/access.log combined

# All files below document root should be handled by application.wsgi
# Reload processes on wsgi file edit
WSGIDaemonProcess ket user=www-data group=www-data threads=5 WSGIScriptAlias / /var/www/kiteeatingtree.org/ket/application.wsgi WSGIScriptReloading On

WSGIProcessGroup ket WSGIApplicationGroup %{GLOBAL} 
Order deny,allow Allow from all

Alias /static /var/www/kiteeatingtree.org/ket/static Order allow,deny Allow from all Alias /images /var/www/kiteeatingtree.org/ket/static/images Order allow,deny Allow from all

