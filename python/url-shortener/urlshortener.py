from flask import Flask, request, redirect
import pyshorteners

app = Flask(__name__)
url_mappings = {}

@app.post('/shorten')
def shorten_url():
    global next_url_path
    long_url = request.json["url"]
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    if short_url not in url_mappings:
        url_mappings[short_url] = long_url
        return short_url
    if short_url in url_mappings:
        return (f"This link {long_url} has already been shortened to {short_url}")
    else:
        return "Error with the provided URL"
if __name__ == '__main__':
    app.run()