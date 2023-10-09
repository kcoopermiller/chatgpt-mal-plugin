# <img src="https://github.com/kcoopermiller/chatgpt-mal-plugin/blob/main/img/mal-logo.png" alt="mal logo" width="100" /> ✖️ <img src="https://github.com/kcoopermiller/chatgpt-mal-plugin/blob/main/img/openai-logo.png" alt="openai logo" width="100" />

# ChatGPT MyAnimeList Plugin

This plugin allows you to interact with your MyAnimeList account through ChatGPT. It allows you to add anime to your list, search for anime, get recommendations, and more.

## Setup locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com.
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled!

## Getting help

This plugin is forked from [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart) and designed to work in conjunction with the
[ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).
