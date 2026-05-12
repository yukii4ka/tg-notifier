# tg-notifier

tiny script to send telegram messages from the command line or other scripts. useful for getting notified when a long job finishes or a cron task fails.

```bash
python notify.py "backup done"
python notify.py "deploy failed: $ERROR"
```

## setup

1. create a bot via [@BotFather](https://t.me/botfather), get token
2. get your chat id (message the bot, check `getUpdates`)
3. copy `.env.example` to `.env` and fill in the values

```
TG_TOKEN=your_bot_token
TG_CHAT_ID=your_chat_id
```

## usage

```bash
# simple message
python notify.py "hello from server"

# with title
python notify.py --title "cron" "nightly backup finished in 4m 32s"

# from a pipe
echo "something went wrong" | python notify.py
```

## in cron

```
0 3 * * * /usr/bin/python3 /opt/backup.sh && python3 /opt/notify.py "backup ok" || python3 /opt/notify.py "backup FAILED"
```

## stack

python · requests · python-dotenv
