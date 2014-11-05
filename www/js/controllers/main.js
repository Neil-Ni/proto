angular.module('starter')
	.controller('MainCtrl', function($rootScope, $location, $state, $scope, $ionicSideMenuDelegate, $ionicPopover, $ionicModal) {
		$scope.slideHasChanged = function(index) {
			console.log(index);
		}
		$scope.toggleRight = function() {
			$ionicSideMenuDelegate.toggleRight();
		};

		$scope.currentState = 'default';


		$scope.isLogin = false;
		var states = ['main', 'welcome', 'mortgageCalculator', 'questionnaire', 'documentUpload', 'documentReview', 'confirmClosing']; 
		$rootScope.$on('$stateChangeSuccess', function() {
			$scope.currentState = $state.current.name;
			console.log($scope.currentState);
			var i = states.indexOf($scope.currentState);
			if (i > 2) {
				$scope.isLogin = true;
			} else {
				$scope.isLogin = false;
			}
		});


		//Headers
		$scope.notifications = [];
		$scope.notification = {};

		$scope.$on("showNotifications", function(event, data){
			var i = $scope.notifications.indexOf(data);
			if (i < 0)
				$scope.notifications.push(data);
		});

		$scope.confirmNotification = function(notification) {
			$scope.notification = notification;
			var i = $scope.notifications.indexOf(notification);
			if(i != -1) $scope.notifications.splice(i, 1);
			$scope.closeModal();
		}

		$ionicPopover.fromTemplateUrl('partials/header/calendarPopover.html', {
			scope: $scope,
		}).then(function(popover) {
			$scope.calendarPopover = popover;
		});
		$scope.openCalendarPopover = function($event) {
			$scope.calendarPopover.show($event);
		};
		$scope.closeCalendarPopover = function() {
			$scope.calendarPopover.hide();
		};

		$ionicPopover.fromTemplateUrl('partials/header/popover.html', {
			scope: $scope,
		}).then(function(popover) {
			$scope.popover = popover;
		});
		$scope.openChatPopover = function($event) {
			$scope.popover.show($event);
		};
		$scope.closeChatPopover = function() {
			$scope.popover.hide();
		};
		$scope.$on('$destroy', function() {
			if($scope.popover) $scope.popover.remove();
			if($scope.calendarPopover) $scope.calendarPopover.remove();
		});

		$ionicModal.fromTemplateUrl('partials/header/notificationModal.html', {
			scope: $scope,
			animation: 'slide-in-up'
		}).then(function(modal) {
			$scope.modal = modal;
		});
		$scope.openModal = function() {
			$scope.modal.show();
		};
		$scope.closeModal = function() {
			$scope.modal.hide();
		};
		$scope.$on('$destroy', function() {
			$scope.modal.remove();
		});
		$scope.$on('modal.hidden', function() {
			if ($scope.notification.key) $scope.$broadcast($scope.notification.key)
		});
		$scope.$on('modal.removed', function() {
		});
		$scope.confirm = function() {
			$scope.modal.hide();
		}
	});