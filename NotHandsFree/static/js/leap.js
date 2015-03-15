console.log("Hello World");
var controller = new Leap.Controller();

controller.inBrowser();

controller.on('frame', function(frame) {
	console.log(frame);
});

controller.inBrowser(true);
controller.connect();