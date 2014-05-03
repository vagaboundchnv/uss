'use strict';
angular.module('ussApp')
.service('ScrapService', ['$http', '$q', function($http,$q){
	return {
		get: function(uri){
			return $http({method: 'GET', url: 'http://api.embed.ly/1/oembed?url='+uri})
		},
		newget : function(uri){
			var deferred = $q.defer();
			$http.get('http://api.embed.ly/1/oembed?url='+uri).success(function(e) { 
				deferred.resolve(e.data);
			}, function(reason) {
				deferred.reject(reason);
			});
			return deferred.promise;
		},
		setAllUrls : function(urls) {
			var deferred = {};
			for (var url in urls){
				deferred[urls[url]['link']]= $http({method: 'GET', url: 'http://api.embed.ly/1/oembed?url='+urls[url]['link']});
			}
			for (var key in deferred){
				deferred[key].success(function(data){
					urls[data["url"]].scrap_data = data;
				})
			}
			return urls;
		}
	}
}]);