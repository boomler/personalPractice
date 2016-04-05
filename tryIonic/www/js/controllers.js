var app = angular.module('starter.controllers', [])

function urlParse(url) {
  url = decodeURI(url);
    var result = {};
    var paramStart = url.indexOf("?");

    if (paramStart) {
        var params = url.slice(paramStart + 1, url.length);
        if (params.indexOf("=") > 0) {
            var parameters = params.split("&");
            parameters.forEach(function(i) {
                if (i.indexOf("="))
                    result[i.split("=")[0]] = i.split("=")[1];

            })
        }
    }
    return result;
}
app.controller('AppCtrl', function($scope, $ionicModal, $timeout) {
 
    $scope.loginData = {};

    // Create the login modal that we will use later
    $ionicModal.fromTemplateUrl('templates/login.html', {
        scope: $scope
    }).then(function(modal) {
        $scope.modal = modal;
    });

    // Triggered in the login modal to close it
    $scope.closeLogin = function() {
        $scope.modal.hide();
    };

    // Open the login modal
    $scope.login = function() {
        $scope.modal.show();
    };

    // Perform the login action when the user submits the login form
    $scope.doLogin = function() {
        console.log('Doing login', $scope.loginData);

        // Simulate a login delay. Remove this and replace with your login
        // code if using a login system
        $timeout(function() {
            $scope.closeLogin();
        }, 1000);
    };
})

app.controller('PlaylistsCtrl', function($scope) {
    $scope.playlists = [
        { title: 'Reggae', id: 1 },
        { title: 'Chill', id: 2 },
        { title: 'Dubstep', id: 3 },
        { title: 'Indie', id: 4 },
        { title: 'Rap', id: 5 },
        { title: 'Cowbell', id: 6 }
    ];
})

app.controller('PlaylistCtrl', function($scope, $stateParams) {})
app.controller('friendlistCtrl', function($scope) {
    $scope.friendslist = [{
        name: "王浩",
        img: "http://a.hiphotos.baidu.com/baike/w%3D268/sign=8a535c7988d4b31cf03c93bdbfd7276f/279759ee3d6d55fb7245311c6e224f4a20a4dd0d.jpg",
        introduction: "你好啊，浩神~",
        id: 01
    }, {
        name: "王浩",
        img: "http://a.hiphotos.baidu.com/baike/w%3D268/sign=8a535c7988d4b31cf03c93bdbfd7276f/279759ee3d6d55fb7245311c6e224f4a20a4dd0d.jpg",
        introduction: "你好啊，浩神~",
        id: 02
    }, {
        name: "王浩",
        img: "http://a.hiphotos.baidu.com/baike/w%3D268/sign=8a535c7988d4b31cf03c93bdbfd7276f/279759ee3d6d55fb7245311c6e224f4a20a4dd0d.jpg",
        introduction: "我不好，浩神~",
        id: 03
    }, {
        name: "王浩",
        img: 'https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1992558276,2545449464&fm=58',
        introduction: "你好啊，浩神~",
        id: 04
    }]
})
app.controller('chatCtrl', function($scope) {
    $scope.user = {
        name: urlParse(location.href).name,
        id: urlParse(location.href).id,
    }
    $scope.chat = {
      newMessage:""
    }
    
});
