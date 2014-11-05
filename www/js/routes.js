angular.module('starter')
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $stateProvider.state( 'index', {
        url: '/index', 
        templateUrl: 'templates/main/index.html'
    });
    $urlRouterProvider.otherwise('/index');
}]);