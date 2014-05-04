angular.module('ussApp')
.controller('AddUrlCtrl', ['$scope', '$location', '$modal', 'NotificationFactory', function($scope, $location, $modal, NotificationFactory) {
  $scope.open = function () {
    var modalInstance = $modal.open({
      templateUrl: '/partials/add-url.html',
      controller: 'AddModalInstanceCtrl',
      resolve: {
      }
    });
    modalInstance.result.then(
      function (response) {
        NotificationFactory.info(response);
      }
    )
  };
}])

.controller('AddModalInstanceCtrl', ['$scope', '$modalInstance', function($scope, $modalInstance) {
  $scope.response = "Succeessfully Added Url";

  $scope.ok = function () {
    $modalInstance.close($scope.response);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };

}]);