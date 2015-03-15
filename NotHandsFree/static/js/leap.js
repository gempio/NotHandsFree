console.log("Hello World");

var controller = Leap.loop({enableGestures:true}, function(frame){
    var currentFrame = frame;
    var previousFrame = controller.frame(1);
    var tenFramesBack = controller.frame(10);
});

controller.inBrowser();

controller.connect();