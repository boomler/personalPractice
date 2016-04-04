var net = require("net");
// 服务器只会做监听····
// rawMessage 作为未发送的数据列表，
rawMessage = [{
    from: uid,
    to: uid,
    content: "",
    time: ""
}]
var netServer = net.createServer(connectionListener);


netServer.listen(11111)

function connectionListener(socket) {
    socket.on("connetction", handleConnection);
    socket.on("data", function(data) {
        handleData(data, socket);
    });
    socket.setTimeout(120 000); //120秒无活动就断开连接

}

function handleConnection() {
	// 轮询查找是否有该用户的消息
	 
	setInterval(getHistoryMessage(), repeat);
}

function handleData(data, socket) {
    var clientData = JSON.parse(data.toString());
    socket.write("oh, I know your name! Hello " + clientData.name);
}

// 查找两个人之间是否有未发送消息
function getHistoryMessage(sender,receiver,socket){
	for(var index=0,len=rawMessage.length;index<len;index++){
		if(rawMessage.sender == sender && rawMessage.receiver)
			socket.write(JSON.stringify(rawMessage[index]));
	}


}
