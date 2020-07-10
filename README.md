This repo showcases the use of [lnpay](https://lnpay.co) paywall-feature
with python flask.
So we're protecting here a "Hello World!" Document with a paywall.

Here is a step by step explanation how to use this. We will need Accounts on, obviously, [lnpay](https://lnpay.co) but also [ngrok](https://dashboard.ngrok.com). We won't register a DNS-name but the webhook which is used needs a publicly available URL. So we "fake" that with a http-reverse-tunnel.


```
virtualenv --python=python3.6 .env
. ./.env/bin/activate
pip3 install flask
export FLASK_APP=app.py
export FLASK_DEBUG=true
flask run # this won't come back ... so ...

# ... in a new terminal
# signup at https://dashboard.ngrok.com
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

unzip ngrok-stable-linux-amd64.zip 
chmod u+x ngrok
# check https://dashboard.ngrok.com/get-started/setup for your ngrok auth command
./ngrok http 5000
```

Your application is now up&running and available at a public ngrok-dns/url.

Let's setup the paywall: click [create](https://lnpay.co/link/create) and setup your paywall. The most relevant field is "URL" which is the URL delivered by ngrok.

After clicking "save", replace the link in line 7 with your paywall URL.
The next step is setting up your webhook in the developer-section on lnpay. click [create](https://lnpay.co/webhook/create) and fill in your ngrok-url with the /webhook endpoint, e.g. "http://3bd92c3e3e79.ngrok.io/webhook". Tick the "paywall_conversion" checkbox and click "save".

You Paywall should now be ready to go.