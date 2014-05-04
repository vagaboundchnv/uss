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
  $scope.tags = [];
  $scope.save = function (urlForm) {
    if (urlForm.$inValid){
      var requiredElements = userTasksDetailForm.$error.required;
      for(var i=0; i<requiredElements.length; i++) {
        requiredElements[i].$dirty = true;
        requiredElements[i].$prinstine = false;
      }
      $scope.errorMessage = true;
    }
    else {
      $modalInstance.close($scope.response);
    }
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
}])