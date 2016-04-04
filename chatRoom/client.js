var net = require("net");

var message = {
    name: "wang",
    clientMessage: "Hi, server~"
}
var client = net.connect({ port: 11111 }, function() {
    console.log("已经建立起链接了~");
 client.write(JSON.stringify(message));
});
client.on("connection", function() {
    client.write(JSON.stringify(message));
})
client.on("data", function(data) {
    console.log("收到data: " + data.toString());
});
 client.on("end", function() {
    console.log("服务器已经断开连接了~");
})

