# Creating-Spotify-Playlist-from-Billboard-100

**Step 1 - Scraping the Billboard Hot 100**
1. Create a new project in PyCharm and create the main.py file.

**Step 2 - Authentication with Spotify**
1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:
https://developer.spotify.com/dashboard/

3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.
Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password. We'll explore OAuth more in later modules on web development, but if you want you can read more about it here: https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

Authenticating with Spotify is quite complicated, especially when you want to access a user's account. So instead, we're going to use one of the most popular Python Spotify modules - Spotipy to make things easier.

**Step 3 - Search Spotify for the Songs from Step 1**
1. Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).

**Step 4 - Creating and Adding to Spotify Playlist**
