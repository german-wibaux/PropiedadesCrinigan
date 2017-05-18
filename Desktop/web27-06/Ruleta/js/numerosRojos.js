var reds = [1, 3, 5, 7, 9];
$(document).ready(function (){
	$('#changeColors').on('click', function(){
		var resp;
		reds = [];
		alert('Ingrese de a uno los numeros rojos.');
		while (resp != 'listo') {
			var number;
			number = parseInt(prompt());
			if (number > 0 && number < 11) {
				reds.push(number);
			}
			resp = prompt('Para no cambiar mas numeros, ingresar "listo".')
		};

		if (reds.indexOf(1) != -1) {
			$('#1').removeClass('black');
			$('#1').addClass('red');
		} else {
			$('#1').removeClass('red');
			$('#1').addClass('black')
		};
		if (reds.indexOf(2) != -1) {
			$('#2').removeClass('black');
			$('#2').addClass('red');
		} else {
			$('#2').removeClass('red');
			$('#2').addClass('black')
		};
		if (reds.indexOf(3) != -1) {
			$('#3').removeClass('black');
			$('#3').addClass('red');
		} else {
			$('#3').removeClass('red');
			$('#3').addClass('black')
		};
		if (reds.indexOf(4) != -1) {
			$('#4').removeClass('black');
			$('#4').addClass('red');
		} else {
			$('#4').removeClass('red');
			$('#4').addClass('black')
		};
		if (reds.indexOf(5) != -1) {
			$('#5').removeClass('black');
			$('#5').addClass('red');
		} else {
			$('#5').removeClass('red');
			$('#5').addClass('black')
		};
		if (reds.indexOf(6) != -1) {
			$('#6').removeClass('black');
			$('#6').addClass('red');
		} else {
			$('#6').removeClass('red');
			$('#6').addClass('black')
		};
		if (reds.indexOf(7) != -1) {
			$('#7').removeClass('black');
			$('#7').addClass('red');
		} else {
			$('#7').removeClass('red');
			$('#7').addClass('black')
		};
		if (reds.indexOf(8) != -1) {
			$('#8').removeClass('black');
			$('#8').addClass('red');
		} else {
			$('#8').removeClass('red');
			$('#8').addClass('black')
		};
		if (reds.indexOf(9) != -1) {
			$('#9').removeClass('black');
			$('#9').addClass('red');
		} else {
			$('#9').removeClass('red');
			$('#9').addClass('black')
		};
		if (reds.indexOf(10) != -1) {
			$('#10').removeClass('black');
			$('#10').addClass('red');
		} else {
			$('#10').removeClass('red');
			$('#10').addClass('black')
		};

	});
});