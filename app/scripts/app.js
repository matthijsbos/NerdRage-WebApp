requirejs.config({
    baseUrl: 'scripts',
    paths: {
        jquery: '/lib/jquery/js/jquery.min',
        knockout: '/lib/knockoutjs/js/knockout',
        bootstrap: '/lib/bootstrap/js/bootstrap.bundle.min'
    },
	shim: {
		bootstrap: {
			'deps': ['jquery']
		}
	}
});

require(['jquery', 'knockout', 'bootstrap'], function($, ko, bootstrap) {
	socket = new WebSocket("ws://" + location.hostname + (location.port ? (':'+ location.port) : '') + "/ws");
	
/* 	socket.addEventListener('open', function(event) {
		socket.send("test");
		console.log('Message sent');
	}); */
	
	socket.addEventListener('message', function(event) {
		console.log('Message from server ', event.data);
	});

	var firing = false;
	var firingLaser = false;
	
	var viewModel = {
		yawSpeed: 100.0,
		yawAcceleration: 100.0,
		pitchSpeed: 100.0,
		pitchAcceleration: 100.0,
		command: "",
		fireGun: function() {
			console.log('Fire gun');
			socket.send(JSON.stringify({ commandName: 'FireGun' }));
			firing = true;
			
		},
		stopGun: function() {
			console.log('Stop gun');
			socket.send(JSON.stringify({ commandName: 'StopGun' }));			
			firing = false;
		},
		toggleLaser: function() {
			if (!firingLaser) {
				console.log('Fire laser');
				socket.send(JSON.stringify({ commandName: 'FireLaser' }));
				firingLaser = true;
			} else {
				console.log('Stop laser');
				socket.send(JSON.stringify({ commandName: 'StopLaser' }));
				firingLaser = false;
			}
		},
		movePitchPositive: function() {
			console.log('Move pitch positive');
			socket.send(JSON.stringify({ commandName: 'MovePitchPositive' }));
		},
		movePitchNegative: function() {
			console.log('Move pitch negative');
			socket.send(JSON.stringify({ commandName: 'MovePitchNegative' }));
		},
		moveYawPositive: function() {
			console.log('Move yaw positive');
			socket.send(JSON.stringify({ commandName: 'MoveYawPositive' }));
		},
		moveYawNegative: function() {
			console.log('Move yaw negative');
			socket.send(JSON.stringify({ commandName: 'MoveYawNegative' }));
		},
		stopPitch: function() {
			console.log('Stop pitch');
			socket.send(JSON.stringify({ commandName: 'StopPitch' }));
		},
		stopYaw: function() {
			console.log('Stop yaw');
			socket.send(JSON.stringify({ commandName: 'StopYaw' }));
		},
		home: function() {
			console.log('Homing');
			socket.send(JSON.stringify({ commandName: 'Home' }));			
		},
		stop: function() {
			console.log('STOP');
			socket.send(JSON.stringify({ commandName: 'Stop' }));			
		},
		executeCommand: function() {
			console.log('Execute command "' + viewModel.command + '"');
			socket.send(JSON.stringify({ commandName: 'Execute', command: viewModel.command}));
		}
	};
	
	ko.applyBindings(viewModel);
	

	window.addEventListener("gamepadconnected", function(e) {
		console.log("gamepad connected");		
		setInterval(function() {
			if (firing == false && navigator.getGamepads()[e.gamepad.index].buttons[0].pressed) {
				console.log('gamepad button 0 pressed');
				viewModel.fireGun();
			} else if (firing == true && !navigator.getGamepads()[e.gamepad.index].buttons[0].pressed) {
				console.log('gamepad button 0 released');
				viewModel.stopGun() 
			}
		}, 99);
	});

});
