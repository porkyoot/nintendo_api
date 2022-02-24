Nintendo REST API (4 ACNH)
==========================

Nintendo Online REST API to get online game data like in the phone apps. Code derived from (Eli's)[https://github.com/frozenpandaman] project Splanet2statink, especially (that file)[https://github.com/frozenpandaman/splatnet2statink/blob/master/iksm.py]. Also big thanks to Mathew Chan with their (blog post)[https://dev.to/mathewthe2/intro-to-nintendo-switch-rest-api-2cm7] on how to access the ACNH API in particular.

Anyone is free to frok or do a PR on tat repository to make it into a proper Python module for PyPi.

To start accessing the API do the following :

```
tokens = animal_crossing.login() #Follow instructions
animal_crossing.send('ehlo',tokens=tokens)
```
