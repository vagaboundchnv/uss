angular.module('ussApp')
.factory('NotificationFactory', function () {
	toastr.options = {
		"closeButton": true,
		"debug": true,
		"positionClass": "toast-top-full-width",
		"showDuration": "300",
		"hideDuration": "1000",
		"timeOut": "5000",
		"extendedTimeOut": "1000",
		"showEasing": "swing",
		"hideEasing": "linear",
		"showMethod": "fadeIn",
		"hideMethod": "fadeOut"
	}	
    return {
        success: function (message) {
            toastr.success(message);
        },
        error: function (text) {
            toastr.error(text, "Error");
        },
        info: function (message) {
            toastr.info(message);
        }        
    };
});