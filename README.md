<img src="https://github.com/kcoopermiller/chatgpt-mal-plugin/blob/main/img/mal-logo.png" alt="mal logo" width="100" /> ✖️ <img src="https://github.com/kcoopermiller/chatgpt-mal-plugin/blob/main/img/openai-logo.png" alt="openai logo" width="100" />

# ChatGPT MyAnimeList Plugin

This plugin allows you to interact with your MyAnimeList account through ChatGPT. Get info about specific anime/manga, access general or seasonal rankings, read forum topics, get or update info about an authenticated user, and more.

## Setup on Heroku

1. Follow the instructions [here](https://myanimelist.net/forum/?topicid=1973141) to create a MyAnimeList API ID.
   You will receive a Client ID and a Client Secret. Save these for later.

2. Install [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up), the Heroku CLI and login.

3. Clone the repository and navigate to the directory.

```bash
git clone https://github.com/kcoopermiller/chatgpt-mal-plugin.git
cd chatgpt-mal-plugin
```

4. Create a new Heroku app.

```bash
heroku create
```

5. Add the following config variables to your Heroku app. These are the Client ID and Client Secret you received from MyAnimeList.

```bash
heroku config:set OPENAI_CLIENT_ID=<your-mal-client-id>
heroku config:set OPENAI_CLIENT_SECRET=<your-mal-client-secret>
```

6. Deploy the app and run it.

```bash
git push heroku main
heroku ps:scale web=1
```

7. Once the app is deployed, navigate to the [ChatGPT](https://chat.openai.com/) Plugin store
8. Select "Develop your own plugin"
9. Enter the domain where your plugin is hosted (ex: `https://my-plugin.herokuapp.com`)
10. Enter the OAuth client ID and client secret you received from MyAnimeList.
11. Add the verification token to your `ai-plugin.json` file
12. Commit and push your changes to GitHub and redeploy your Heroku app.

The plugin should now be installed and enabled!

## Getting help

This plugin is forked from [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart) and designed to work in conjunction with the
[ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).
