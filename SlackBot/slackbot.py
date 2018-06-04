#!/usr/bin/python
#------------------------------------- HOW TO USE -------------------------------------
# Send text using slack api (cli)
#	curl -X POST -H 'Content-type: application/json' --data '{"text":"First line \nSecond line"}' https://hooks.slack.com/services/webhook_TOKEN
#
# Send text a specific channel
#	curl -X POST --data "payload={\"text\": \"Hi, Im *$(hostname)* \", \"channel\": \"My_slack_channel\", \"username\": \"My_name\"}" https://hooks.slack.com/services/Webhooks_token
#
# Send file to channel
#	curl -F file=@/path_to_file/file.conf -F channels=My_slack_channel -F token=legacy-token https://slack.com/api/files.upload
#
# Send log to channel
#	curl -F file=@/var/log/netd-history.log -F channels=My_slack_channel -F token=legacy-token https://slack.com/api/files.upload
#
# --------------- INFO ------------------
# url  Webhook token
# You can create webhooks token here: https://my.slack.com/services/new/incoming-webhook/
#
# Legacy token
# You can create legacy token here:  https://api.slack.com/custom-integrations/legacy-tokens
# -------------------------------------------------------------------------------------
from slackclient import SlackClient
import re
import time
import os
import commands

BOT_TOKEN = "_%_legacy-token_%_"

def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if not sc.rtm_connect():
        raise Exception("Can not connect to slack, is your tocken a legacy token.")

# .................................. LOOP .........................................#
    # Where the magic happens
    while True:
        # Examine latest events
        for slack_event in sc.rtm_read():

            # Disregard events that are not messages
            if not slack_event.get('type') == "message":
                continue

            # Variables, do not modify this vars 
            user = slack_event.get("user")
            message = slack_event.get("text")
            channel = slack_event.get("channel")

	    # Uncoment this two lines if you limit messages only from humans (slack real users)
            # if not message or not user:
                # continue

#-------------------------------- FUNCTIONS AND COMMANDS HERE ----------------------------------------------#
            if "hello" in message.lower():
                sc.rtm_send_message(channel, "I'm have life, thanks father!!!")

            # when you write cmd, all text after it is executed on terminal linux (DANGER, use with responsability)
            if "cmd" in message.lower():
                sc.rtm_send_message(channel, commands.getoutput(message.split(' ', 1)[1]) )
                # commands.getoutput    = Get output of command line 
                # split()               = returns a list of all the words in the string
                # (' ', 1)[1]           = cut the first word of the command, in this case "cmd" 

#-------------------------------- // END COMMANDS ----------------------------------------------#
        # Sleep for half a second
        time.sleep(0.5)
# .................................. END LOOP .........................................#
if __name__ == '__main__':
    main()
