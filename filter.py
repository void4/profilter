from socketIO_client import SocketIO, LoggingNamespace
import codecs

blacklist = []
with codecs.open("blacklist.txt", "r", "utf-8") as f:
    blacklist = [w.strip().lower() for w in f.readlines()]

def on_connect():
    print('Connected')

def on_disconnect():
    print('Disconnected')

def on_reconnect():
    print('Reconnected')

def on_message(args):
    match = None
    message = [w.strip().lower() for w in args["message"].split()]

    for word in blacklist:
        if word in message:
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
