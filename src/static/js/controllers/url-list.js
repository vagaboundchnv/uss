'use strict';

angular.module('ussApp').controller('UrlListCtrl', ['$scope', 'UrlService', function($scope, UrlService) {
  var httpRequest = UrlService.getUrls();
  httpRequest.success(function(data, status, headers, config){
    $scope.urls = data.objects;
  })
  .error(function(data, status, headers, config){
    alert('Error While calling status:' + status +'data: ' + data);
  });
}]);