angular.module('starter')
	.controller('MainCtrl', function($rootScope, $location, $state, $scope, $ionicSideMenuDelegate) {
		$scope.toggleRight = function() {
			$ionicSideMenuDelegate.toggleRight();
		};
		$scope.currentState = 'default';
		$rootScope.$on('$stateChangeSuccess', function() {
			$scope.currentState = $state.current.name;
		});
	});