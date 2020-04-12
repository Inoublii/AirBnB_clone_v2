# Redo the task #0 but by using Puppet:
exec { 'execute':
  command => 'sudo apt-get update -y;
              sudo apt-get install nginx -y;
              sudo mkdir -p /data/web_static/shared/;
              sudo mkdir -p /data/web_static/releases/test/;
              sudo touch /data/web_static/releases/test/index.html;
              sudo echo "Hello Holberton School" > /data/web_static/releases/test/index.html;
              sudo ln -sf /data/web_static/releases/test /data/web_static/current;
              sudo chown -R ubuntu:ubuntu /data/;
              sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default;
              sudo service nginx restart',
  provider => shell,
}
