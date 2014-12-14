# ircreactor

ircreactor is a library for the conversion of IRC messages into intermediate objects.  In other words,
ircreactor provides the following functionality:

 * Parsing of IRC messages into an intermediate representation
 * Conversion of intermediate representation back into IRC messages
 * Subscription for intermediate representation elements

## usage

ircreactor is mainly meant to implement irc clients *or* irc servers.  It handles abstraction of the IRC
protocol versions, by providing a clean native object which describes an IRC message.  It also provides an
event manager for implementation of the mutation-reactor pattern.

A very basic example which ties `ircreactor` to `asyncio.Protocol` and dumps IR representation of the IRC
messages can be found at `example.py`.

If you run it, you will see output like:

```
2014-12-14 11:54:06,447 Using selector: KqueueSelector
Serving on ('127.0.0.1', 6667)
Connection from ('127.0.0.1', 51952)
2014-12-14 11:54:09,705 dispatching: rfc1459 message NICK: {'verb': 'NICK', 'client': <__main__.IRCClient object at 0x106329780>, 'source': None, 'params': ['kaniini'], 'tags': {}}
```

It will also echo back the message after rebuilding from the intermediate representation.
