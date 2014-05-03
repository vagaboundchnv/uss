'use strict';

angular.module('ussApp').controller('TagCtrl', ['$scope', 'TagService', function($scope, TagService) {
  var httpRequest = TagService.getTags();
  httpRequest.success(function(data, status, headers, config){
    $scope.tags = data.objects;
    $scope.metatags = data.meta;
  })
  .error(function(data, status, headers, config){
    alert('Error While calling status:' + status +'data: ' + data);
  });
}]);