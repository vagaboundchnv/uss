'use strict';


// Declare app level module which depends on filters, and services
angular.module('ussApp', [
  'ngRoute',
  'ussApp.filters',
  'ussApp.services',
  'ussApp.directives',
  'ussApp.controllers'
]).
config(['$interpolateProvider','$routeProvider', function($interpolateProvider, $routeProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');  
  $routeProvider.when('/urls', {
  	title:'List of Urls',
  	templateUrl: 'partials/url-list.html', 
  	controller: 'UrlListCtrl',
	// resolve: {
	// 	style : function(){
 //      	/* check if already exists first - note ID used on link element*/
 //      	/* could also track within scope object*/
 //      	if( !angular.element('link#urls').length){
 //        	angular.element('head').append('<link href="css/url-list.css" rel="stylesheet">');
 //      	}
 //      }
 //  	}  	
  });  
  $routeProvider.when('/urls/:urlId', {templateUrl: 'partials/url-details.html', controller: 'UrlDetailCtrl'});
  $routeProvider.otherwise({redirectTo: '/urls'});
}]);