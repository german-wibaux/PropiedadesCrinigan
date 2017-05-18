$(document).ready(function(){

	$.ajax({
		url: 'home.html',
		cache: false,
		dataType: 'HTML',
		method: 'GET',
		success: function(data){
			$('.contenido').html(data);
		}
	});


	$("#home").on("click", function(ev){
		ev.preventDefault();

		$.ajax({
			url: 'home.html',
			cache: false,
			dataType: 'HTML',
			method: 'GET',
			success: function(data){
				$('.contenido').html(data);
			}
		});
	});


	$("#proyectos").on("click", function(ev){
		ev.preventDefault();

		$.ajax({
			url: 'proyects.html',
			cache: false,
			dataType: 'HTML',
			method: 'GET',
			success: function(data){
				$('.contenido').html(data);
			}
		});
	});

	$("#tarifas").on("click", function(ev){
		ev.preventDefault();

		$.ajax({
			url: 'costs.html',
			cache: false,
			dataType: 'HTML',
			method: 'GET',
			success: function(data){
				$('.contenido').html(data);
			}
		});
	});

	$("#contacto").on("click", function(ev){
		ev.preventDefault();

		$.ajax({
			url: 'contact.html',
			cache: false,
			dataType: 'HTML',
			method: 'GET',
			success: function(data){
				$('.contenido').html(data);
			}
		});
	});
});