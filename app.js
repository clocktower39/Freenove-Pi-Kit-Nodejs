const LCD = require('raspberrypi-liquid-crystal');
const gpio = require('onoff').Gpio;
const tempSensor = require("node-dht-sensor");

// adjust according to GPIO pins
const lcd = new LCD(1, 0x27, 16, 2);
var motionSensor = new gpio(26, 'in', 'both');

// turn on the LCD then clear the screen
lcd.beginSync();
lcd.clearSync();

let displayText = (inputText) => {
    if(inputText.length > 32){
        overSixteenCharacters(inputText);
    }
    else if(inputText.length > 16){
        lcd.printLineSync(0, inputText.substr(0,15) );
        lcd.printLineSync(1, inputText.substr(15,inputText.length-1) );
    }
    else {
        lcd.printLineSync(0, inputText );
    }
}
// cycles through the text and stops at the end
let overSixteenCharacters = (paragraph) => {
    for(let i = 0; i < paragraph.length-31; i++){
        //delay the loop to make the animation visible
        delay(i,paragraph);
    }
}

function delay(i,paragraph){
    setTimeout(function(){
        // each line only has space for 16 characters
        
        let topLine = paragraph.substr(i,i+16);
        let bottomLine = paragraph.substr(i+16,i+16)

        lcd.printLineSync(0, topLine );
        lcd.printLineSync(1, bottomLine );

        // multiple the delay by i so it actually delays
    }, 200*i)
}

// motion sensor
motionSensor.watch(function(err, value) {
    // clear previous screen
    lcd.clearSync();

    // voltage changes to 1 during motion
    if (value == 1) {
        sendMessage(`Motion detected @ ${new Date().toLocaleTimeString()}`);
    }
    // ~10 seconds back initial voltage, 15 more seconds until detection available
    else {
        tempSensor.read(11, 4, function(err, temperature, humidity) {
            if (!err) {
          
              console.log(`${new Date().toLocaleTimeString()} ${new Date().toLocaleDateString()}\ntemp: ${(temperature*(9/5)+32).toFixed(1)}^F \nhumidity: ${humidity.toFixed(1)}%\n`);
        
              lcd.clearSync();
              lcd.printLineSync(0, `temp: ${(temperature*(9/5)+32).toFixed(1)}^F`);
              lcd.printLineSync(1, `humidity: ${humidity.toFixed(1)}%` );
            }
            else{
              console.log(err)
            }
        });
    }
});


function sendMessage(message) {
    displayText(message);
    console.log(message);
}