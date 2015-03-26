
var cordexManager = angular.module('cordexManager', []);

cordexManager.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

cordexManager.controller('submissionsListCtrl', function ($scope) {
	$scope.submissions = [
		{'experiment_name': 'CORDEX-ESD s1t1', 'notes': 'Just testing'},
		{'experiment_name': 'CORDEX-ESD s1t1', 'notes': 'Just testing 2'}
	];
});

cordexManager.controller('experimentsListCtrl', function ($scope, $http) {
	$http.get('/api/experiments/?format=json').success(function(data) {
		$scope.experiments = data;
	});
});