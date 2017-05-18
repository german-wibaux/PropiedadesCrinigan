$(document).ready(function (){
	var player = new player();
	var roulette = new ruleta();
	document.getElementById('credits').innerHTML = player.creditos;
	var apuestas = [];
	var pleno = 5;
	var otrasapuestas = 2;  /*color, par, impar, mayor, menor*/

	/*Crear apuesta*/
	$('.roulette button').on('click', doBet);

	function doBet() {
		typeBet = this.id;
		
		if (typeBet % 4 == 0 && typeBet < 11) {
			alert('Esta apuesta costara el doble de los creditos que ingrese (Multiplo 4)');
			var credits = parseInt(prompt('Creditos a apostar:')) * 2;
		}
		else {
			var credits = parseInt(prompt('Creditos a apostar:'));
		};

		if (credits < player.creditos) {
			player.creditos = player.creditos - credits;
			document.getElementById('credits').innerHTML = player.creditos;

			var betArchive = new bet(typeBet, credits);
			apuestas.push(betArchive);
			writeBet(betArchive);
		}
		else {
			alert('No alcanzan los creditos.');
		};
	};

	function writeBet(archive) {
		var listIn = document.createElement('li');
		var infobet = document.createTextNode(archive.credits + ' creditos al ' + archive.id);
		listIn.appendChild(infobet);
		document.getElementById('bets').appendChild(listIn);
	};

	/*Lanzar ruleta*/
	$('#playRoulette').on('click', play);

	function play(){
		roulette.tirar();
		document.getElementById('numberWin').innerHTML = roulette.valor;
		getAwards();
	};

	function getAwards() {
		var creditsWin = 0;
		apuestas.forEach(function(element, index, array){
			if (element.id < 11) {
				if (element.id == roulette.valor) {
					if (roulette.valor % 4 == 0) {
						creditsWin = creditsWin + (element.credits * pleno * 3);
					}
					else {
						creditsWin = creditsWin + (element.credits * pleno);
					};
				};
			};

			if (element.id == 11) {
				if (roulette.rojo) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				};
			};
			if (element.id == 12) {
				if (!roulette.rojo) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				};
			};

			if (element.id == 13) {
				if (roulette.par) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				}
			}
			if (element.id == 14) {
				if (!roulette.par) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				}
			}

			if (element.id == 15) {
				if (roulette.menor) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				}
			}
			if (element.id == 16) {
				if (!roulette.menor) {
					creditsWin = creditsWin + (element.credits * otrasapuestas);
				}
			}
		});

		player.creditos = player.creditos + creditsWin;
		document.getElementById('credits').innerHTML = player.creditos;
		document.getElementById('premios').innerHTML = creditsWin + ' creditos ganados';
	};


	/* FUNCIONES CONSTRUCTORAS */
	function player(){
		this.creditos = 100;
	};

	function bet(IDApuesta, betCredits) {
		this.credits = betCredits;
		this.id = IDApuesta;
	};

	function ruleta(){
		this.valor = 0;
		this.rojo = true;
		this.par = true;
		this.menor = true;
	};

	ruleta.prototype.tirar = function(){
		this.valor = Math.floor(Math.random() * 10);

		if (reds.indexOf(this.valor) != -1) {
			this.rojo = true;
		}
		else {
			this.rojo = false;
		};

		if (this.valor % 2 == 0) {
			this.par = true;
		}
		else {
			this.par = false;
		};
	
		if (this.valor < 6 && this.valor != 0) {
			this.menor = true;
		} 	else if(this.valor > 5 && this.valor != 0) {
				this.menor = false;
			} 	else {
					this.menor = NaN;
				};
	};
});
