# active-badge-discord-bot
![image](https://github.com/jeremycanlas/active-badge-discord-bot/assets/80456535/0079c44d-f642-4019-911a-cf3e67bef2d3)

Active Developer badge details<br>
https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge<br><br>
Create a virtual environment<br>

    python -m venv env
Activate your virtual environment<br>
    
    env\Scripts\activate
Install requirements

    pip install -r requirements.txt

Create a discord bot in the developer portal and get your bot token by clicking Reset Token<br>
[https://discord.com/developers/docs/getting-started](https://discord.com/developers/docs/getting-started#step-1-creating-an-app)<br><br>
Invite your bot to your server<br>
https://discord.com/developers/docs/getting-started#step-1-creating-an-app<br><br>
Create a .env in your main directory and put your token there<br>

    token=INSERT TOKEN HERE

Open up a terminal and run main.py

    python main.py

Go to any channel and type
    
    /badge

Check after 24 hours<br>
https://discord.com/developers/active-developer<br><br>
Run at least once slash command every 30 days
