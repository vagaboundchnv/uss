'use strict';


// Declare app level module which depends on filters, and services
var ussApp = angular.module('ussApp', ['ngResource', 'ui.bootstrap', 'ngRoute', 'ngTagsInput']);

ussApp.config(['$interpolateProvider','$routeProvider', function($interpolateProvider, $routeProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');  
  $routeProvider.when('/urls', {
    title:'List of Urls',
  	templateUrl: 'partials/url-list.html', 
  	controller: 'UrlListCtrl',
  });  
  $routeProvider.when('/url/:urlId', {templateUrl: 'partials/url-detail.html', controller: 'UrlDetailCtrl'});
  $routeProvider.when('/urls/:tagType', {templateUrl: 'partials/url-list.html', controller: 'UrlListCtrl'});  
  $routeProvider.otherwise({redirectTo: '/urls'});
}]);