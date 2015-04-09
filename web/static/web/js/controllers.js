
var cordexManager = angular.module('cordexManager', []);

cordexManager.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

cordexManager.controller('submissionsListCtrl', function ($scope, $http) {
	$http.get('/api/submissions/?format=json').success(function(data) {
		$scope.submissions = data;
	});

});

cordexManager.controller('experimentsListCtrl', function ($scope, $http) {
	$http.get('/api/meta-experiments/?format=json').success(function(data) {
		$scope.meta_experiments = data;
	});
});