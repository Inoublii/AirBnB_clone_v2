#!/usr/bin/env bash
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown ubuntu:ubuntu -R /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test  /data/web_static/current
location= "\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/ i $location" /etc/nginx/sites-available/default
sudo service nginx restart
