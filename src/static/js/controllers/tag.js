'use strict';

angular.module('ussApp').controller('TagCtrl', ['$scope','$location','TagService', function($scope, $location, TagService) {
  var httpRequest = TagService.getTags();
  httpRequest.success(function(data, status, headers, config){
    $scope.tags = data.objects;
  })
  .error(function(data, status, headers, config){
    alert('Error While calling status:' + status +'data: ' + data);
  });

  $scope.isActive = function (viewLocation) { 
	return viewLocation === $location.path();
	};

}]);