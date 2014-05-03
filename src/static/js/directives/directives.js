'use strict';

/* Directives */


angular.module('ussApp')
.directive('appVersion', ['version', function(version) {
	return function(scope, elm, attrs) {
		elm.text(version);
	};
}]);