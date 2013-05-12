
Assignment 1 solutions 

[Assignment description][1] 

About twitterstream.py: 

Used to fetch live stream data from twitter. Requires oauth2, which is not part of the EnThought Python library. 

usage: Open the program and replace access\_token\_key, access\_token\_secret, consumer\_key, and consumer\_secret with the appropriate values. Then run $ python twitterstream.py 

To get credentials: 

*   Create a twitter account if you do not already have one.
*   Go to https://dev.twitter.com/apps and log in with your twitter credentials.
*   Click "create an application"
*   Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
*   On the next page, scroll down and click "Create my access token"
*   Copy your "Consumer key" and your "Consumer secret" into twitterstream.py
*   Click "Create my access token." You can [Read more about Oauth authorization.][2]
*   Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret
*   Run the following and make sure you see data flowing.
<pre>$ python twitterstream.py
</pre></li>

 [1]: https://class.coursera.org/datasci-001/assignment/view?assignment_id=3
 [2]: https://dev.twitter.com/docs/auth