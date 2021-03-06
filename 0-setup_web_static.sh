#!/usr/bin/env bash
#set up web static deploy
sudo apt-get update
sudo apt-get -y install nginx

ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html>
     <head>
	<title>
	Holberton School
	</title>
     </head>
     <body>
     </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
service nginx restart
