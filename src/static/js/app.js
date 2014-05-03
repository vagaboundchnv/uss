'use strict';


// Declare app level module which depends on filters, and services
var ussApp = angular.module('ussApp', ['ngResource', 'ui.bootstrap', 'ngRoute']);

ussApp.config(['$interpolateProvider','$routeProvider', function($interpolateProvider, $routeProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');  
  $routeProvider.when('/urls', {
    title:'List of Urls',
  	templateUrl: 'partials/url-list.html', 
  	controller: 'UrlListCtrl',
  });  
  $routeProvider.when('/urls/:urlId', {templateUrl: 'partials/url-details.html', controller: 'UrlDetailCtrl'});
  $routeProvider.otherwise({redirectTo: '/urls'});
}]);