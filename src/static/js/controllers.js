'use strict';

/* Controllers */

angular.module('ussApp.controllers', ['ussApp.services']).
  controller('UrlListCtrl', ['$scope', '$http', 'ScrapService', function($scope, $http, ScrapService) {

    $http({method: 'GET', url: 'static/data/urls.json'})
      .success(function(data, status, headers, config){
          $scope.urls = data.urls;
          // for (var url in $scope.urls){
          //     var urlForScrap = $scope.urls[url]['link'];
          //     // ScrapService.get(urlForScrap)
          //     //   .success(function(data, status, headers, config){
          //     //       $scope.urls[url].scrap_data = data;
          //     //     });
          //     // ScrapService.LongRunningRequest(urlForScrap).then(function(data){
          //     //   $scope.urls[url].scrap_data = data;
          //     // });
          //     ScrapService.newget(urlForScrap).then(function(data){
          //       $scope.urls[url].scrap_data = data;
          //     });           
          //   };
          $scope.urls = ScrapService.setAllUrls($scope.urls);
        })
      .error(function(data, status, headers, config){
        alert('Error While calling status:' + status +'data: ' + data);
      });
  
  }])
  .controller('UrlDetailCtrl', ['$scope', '$http', function($scope, $http) {

  }]);