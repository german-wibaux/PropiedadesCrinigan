// 'SlideViewer' must be included:
var app = angular.module('miAplicacion', []);

app.controller('crt',  function ($scope) {
   $scope.datas = [
      {id: '1', name: 'Option A'},
      {id: '2', name: 'Option B'},
      {id: '3', name: 'Option C'}
    ]
    $scope.selectedOption= {id: '3', name: 'Operacion..'} //This sets the default value of the select in the ui
});