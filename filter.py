from socketIO_client import SocketIO, LoggingNamespace
import codecs

blacklist = []
with codecs.open("blacklist.txt", "r", "utf-8") as f:
    blacklist = [w.strip() for w in f.readlines()]

def on_connect():
    print('connected')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_message(args):
    match = None

    for word in blacklist:
        if word in args["message"].split():
            match = word
            break

    if match:
        print(match)
        print(args)

socketIO = SocketIO('https://letsrobot.tv', 8000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen to new snapshots
socketIO.on('chat_message_with_name', on_message)
socketIO.wait()#seconds=1)
