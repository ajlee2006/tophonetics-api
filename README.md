# tophonetics.com API
# Update: This is broken. I will not be maintaining this
## The replit is using [eng-to-ipa](https://pypi.org/project/eng-to-ipa/) instead.
An API for [tophonetics.com](https://www.tophonetics.com/) using Flask. It basically just sends a request to tophonetics.com, then formats the HTML response into plain text IPA. Thus, it is possible that it could fail if they reformat their website. Also, it can take up to 3 seconds for the IPA to load.   

An instance is currently running on https://tophonetics-api.ajlee.repl.co/api. 

## Use
### Python (requests)
```python
import requests
english = "hello"
british_english_ipa = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": english}).text
american_english_ipa = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": english, "dialect": "am"}).text
```
### In the URL
Visit https://tophonetics-api.ajlee.repl.co/api?text=[text] in the browser to get the IPA in plain text. You can also add "&dialect=am" after if you want American English (British English is the default).

## Characters returned
The following characters are used in the IPA returned:

Consonants: bdfhjklmnprstvwxzðŋɡʃʒʤʧθ   
Vowels: aeiouæɑɒɔəɛɜɪʊʌ    
Other: *ˈˌː 

## Legality
I posted a comment on tophonetics.com sharing this, and they replied: "We do not encourage this as it is open to abuse and, yes, it will hit the wall eventually, but good job". I suppose this shows that it is allowed and legal though they don't encourage it.
