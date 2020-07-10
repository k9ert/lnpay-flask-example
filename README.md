
```
virtualenv --python=python3.6 .env
. ./.env/bin/activate
pip3 install flask
export FLASK_APP=app.py
export FLASK_DEBUG=true
# signup at https://dashboard.ngrok.com
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

unzip ngrok-stable-linux-amd64.zip 
chmod u+x ngrok
# check https://dashboard.ngrok.com/get-started/setup for your ngrok auth command
./ngrok http 80
```