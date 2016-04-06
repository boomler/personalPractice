/*后台入口文件 所有请求通过此文件处理*/
// 此文件处理以下业务：
// 1、路由分配
// 2、cookie  session处理（登录状态 ）
// 3、此文件不处理其他业务
var bodyParser = require('body-parser');
var cookieParser = require("cookie-parser");
var session = require('express-session');
var express = require("express");
var config = require("./config");
// var userHandler = require("./controller/userHandler");
  
var app = express();
app.use(bodyParser.json("{type:'application/*+json'}"));

/**静态文件服务**/
app.use("/", express.static(__dirname + "/view"));

app.use(cookieParser());

app.use(session({
    secret: '<mysecret>',
    saveUninitialized: true,
    resave: true,
    cookie: { maxAge: 60000 }
}));
 
app.post("/register",userHandler.register);
app.post("/login",userHandler.login);
 
 
app.listen(config.PORT);  //luck number
