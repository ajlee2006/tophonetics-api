# tophonetics.com API
An API for tophonetics.com using Flask. It is currently running on https://tophonetics-api.ajlee.repl.co/api. 
## Use
### Python (requests)
```python
english = "hello"
british_english_ipa = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": english}).text
american_english_ipa = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": english, "dialect": "am"}).text
```
