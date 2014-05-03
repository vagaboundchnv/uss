'use strict';
angular.module('ussApp')
.service('UrlService', ['$http', function($http){
	return {
		getUrls : function() {
			return $http({method: 'GET', url: '/api/v1/urls/'});
		}
	}
}]);