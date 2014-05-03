'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('ussApp.services', []).
	service('ScrapService', ['$http', '$q', function($http,$q){
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
						// $http({method: 'GET', url: 'http://api.embed.ly/1/oembed?url='+urls[url]['link']}).
						// 	success(function(data){
						// 		urls[url].scrap_data  = data;
						// 	});
					}
					console.log(deferred);
					for (var key in deferred){
						console.log(key);
						deferred[key].success(function(data){
							console.log(data);

							urls[data["url"]].scrap_data = data;
						})
					}

					return urls;
				}
				}
	}]);

