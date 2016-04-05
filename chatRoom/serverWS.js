var WebSocketServer = require('ws').Server,
    wss = new WebSocketServer({ port: 9090 });

//通过ws+ssl的方式通信. 和HTTPS类似
wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
        console.log('received: %s', message);
    });

    ws.send('something');
});
