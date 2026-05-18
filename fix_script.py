import re

with open('script.js', 'r') as f:
    js = f.read()

# Ah wait, I overwrote script.js previously, but then I did `git restore index.html script.js` when looking for add_new_modules.py error and wiped my script.js changes!
# I need to re-apply the script.js changes for the new UI.
