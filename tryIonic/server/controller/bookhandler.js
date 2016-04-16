var book = require("../model/book");
var bodyParser = require("body-parser");

module.exports = exports = {
    personalCollection: function(req,res){
        var uid = req.body.id;
        book.personalCollection(uid,res.send);
    }
}

