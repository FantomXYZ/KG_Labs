


var area = document.getElementById("area");

var red_slider = document.getElementById("red_slider");
var green_slider = document.getElementById("green_slider");
var blue_slider = document.getElementById("blue_slider");

var red_input = document.getElementById("red_input");
var green_input = document.getElementById("green_input");
var blue_input = document.getElementById("blue_input");

var cyan_slider = document.getElementById("cyan_slider");
var magenta_slider = document.getElementById("magenta_slider");
var yellow_slider = document.getElementById("yellow_slider");
var key_slider = document.getElementById("key_slider");

var cyan_input = document.getElementById("cyan_input");
var magenta_input = document.getElementById("magenta_input");
var yellow_input = document.getElementById("yellow_input");
var key_input = document.getElementById("key_input");

var hue_slider = document.getElementById("hue_slider");
var saturation_slider = document.getElementById("saturation_slider");
var value_slider = document.getElementById("value_slider");

var hue_input = document.getElementById("hue_input");
var saturation_input = document.getElementById("saturation_input");
var value_input = document.getElementById("value_input");

var colorInput = document.getElementById("picker");



var red,green,blue;
var cyan,magenta,yellow,key;
var hue,saturation,value;
var hex

function hexToRgb(hex) {

    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, function(m, r, g, b) {
      return r + r + g + g + b + b;
    });
  
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }



function fromRGBtoCMYK(r,g,b){

    k = (1-Math.max(r/255,g/255,b/255))*100;
    c = (1-r/255-k/100)/(1-k/100)/(1-k/100)*100;
    m = (1 - g/255 - k/100)/(1-k/100)*100;
    y = (1 - b/255 - k/100)/(1-k/100)*100;

    return [Math.round(c),Math.round(m),Math.round(y),Math.round(k)]
}

function fromCMYKtoRGB(c,m,y,k){
    r = 255*(1-c/100)*(1-k/100);
    g = 255*(1-m/100)*(1-k/100);
    b = 255*(1-y/100)*(1-k/100);

    return [Math.round(r),Math.round(g),Math.round(b)]
}

function fromRGBtoHSV(r,g,b){

    let rabs, gabs, babs, rr, gg, bb, h, s, v, diff, diffc, percentRoundFn;
    rabs = r / 255;
    gabs = g / 255;
    babs = b / 255;
    v = Math.max(rabs, gabs, babs),
    diff = v - Math.min(rabs, gabs, babs);
    diffc = c => (v - c) / 6 / diff + 1 / 2;
    percentRoundFn = num => Math.round(num * 100) / 100;
    if (diff == 0) {
        h = s = 0;
    } else {
        s = diff / v;
        rr = diffc(rabs);
        gg = diffc(gabs);
        bb = diffc(babs);

        if (rabs === v) {
            h = bb - gg;
        } else if (gabs === v) {
            h = (1 / 3) + rr - bb;
        } else if (babs === v) {
            h = (2 / 3) + gg - rr;
        }
        if (h < 0) {
            h += 1;
        }else if (h > 1) {
            h -= 1;
        }
    }
    return [
        Math.round(h * 360),
        Math.round(s * 100),
        Math.round(v * 100)]
    

}

function fromHSVtoRGB(h,s,v){
  h = h / 360;
  s = s / 100;
  v = v / 100;

  var r, g, b;

  if (s === 0) {
    r = v;
    g = v;
    b = v;
  } else {
    var i = Math.floor(h * 6);
    var f = h * 6 - i;
    var p = v * (1 - s);
    var q = v * (1 - f * s);
    var t = v * (1 - (1 - f) * s);

    switch (i % 6) {
      case 0:
        r = v;
        g = t;
        b = p;
        break;
      case 1:
        r = q;
        g = v;
        b = p;
        break;
      case 2:
        r = p;
        g = v;
        b = t;
        break;
      case 3:
        r = p;
        g = q;
        b = v;
        break;
      case 4:
        r = t;
        g = p;
        b = v;
        break;
      case 5:
        r = v;
        g = p;
        b = q;
        break;
    }
  }

  
  r = Math.round(r * 255);
  g = Math.round(g * 255);
  b = Math.round(b * 255);

  return [r, g, b ];
}


function update_rgb_slider(){
    red_slider.value = red;
    green_slider.value = green;
    blue_slider.value = blue;
}

function update_rgb_input(){
    red_input.value = red;
    blue_input.value = blue;
    green_input.value = green;
}

function update_cmyk_slider(){
    cyan_slider.value = cyan;
    magenta_slider.value = magenta;
    yellow_slider.value = yellow;
    key_slider.value = key;
}


function update_cmyk_input(){
    cyan_input.value = cyan;
    magenta_input.value = magenta;
    yellow_input.value = yellow;
    key_input.value = key;
}

function update_hsv_slider(){
    hue_slider.value = hue;
    saturation_slider.value = saturation;
    value_slider.value = value;
}

function update_hsv_input(){
    hue_input.value = hue;
    saturation_input.value = saturation;
    value_input.value = value;
}



function rgb_slider_update(){

    red = red_slider.value;
    green = green_slider.value;
    blue = blue_slider.value;

    update_rgb_input();

    [cyan,magenta,yellow,key] = fromRGBtoCMYK(red,green,blue)
    
    update_cmyk_slider();

    update_cmyk_input();

    [hue,saturation,value] = fromRGBtoHSV(red,green,blue);

    update_hsv_slider();

    update_hsv_input();


    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;

}


function rgb_input_change(){
    red = red_input.value;
    green = green_input.value;
    blue = blue_input.value;

    
    update_rgb_slider();

    [cyan,magenta,yellow,key] = fromRGBtoCMYK(red,green,blue)
    
    update_cmyk_slider();

    update_cmyk_input();

    [hue,saturation,value] = fromRGBtoHSV(red,green,blue);

    update_hsv_slider();

    update_hsv_input();

    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}


function cmyk_slider_update(){
    cyan = cyan_slider.value;
    magenta = magenta_slider.value;
    yellow = yellow_slider.value;
    key = key_slider.value;

    update_cmyk_input();

    [red,green,blue] = fromCMYKtoRGB(cyan,magenta,yellow,key)

    update_rgb_slider();

    update_rgb_input();

    [hue,saturation,value] = fromRGBtoHSV(red,green,blue);

    update_hsv_slider();

    update_hsv_input();

    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

function cmyk_input_change(){
    cyan = cyan_input.value;
    magenta = magenta_input.value;
    yellow = yellow_input.value;
    key = key_input.value;

    update_cmyk_slider();

    [red,green,blue] = fromCMYKtoRGB(cyan,magenta,yellow,key)

    update_rgb_slider();
    
    update_rgb_input();

    [hue,saturation,value] = fromRGBtoHSV(red,green,blue);

    update_hsv_slider();

    update_hsv_input();

    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}


function hsv_slider_update(){
    hue = hue_slider.value
    saturation = saturation_slider.value
    value = value_slider.value

    update_hsv_input();

    [red,green,blue] = fromHSVtoRGB(hue,saturation,value)

    update_rgb_slider();
    
    update_rgb_input();

    [cyan,magenta,yellow,key] = fromRGBtoCMYK(red,green,blue)
    
    update_cmyk_slider();

    update_cmyk_input();

    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

function hsv_input_change(){
    hue = hue_input.value
    saturation = saturation_input.value
    value = value_input.value

    update_hsv_slider();

    [red,green,blue] = fromHSVtoRGB(hue,saturation,value)

    update_rgb_slider();
    
    update_rgb_input();

    [cyan,magenta,yellow,key] = fromRGBtoCMYK(red,green,blue)
    
    update_cmyk_slider();

    update_cmyk_input();

    area.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

function picker_update(){
    hex = colorInput.value
    
    red = hexToRgb(hex).r
    green = hexToRgb(hex).g
    blue = hexToRgb(hex).b

    
    update_rgb_slider()
    rgb_slider_update()
}


red_slider.addEventListener("input",rgb_slider_update);
green_slider.addEventListener("input",rgb_slider_update);
blue_slider.addEventListener("input",rgb_slider_update);

red_input.addEventListener("input",rgb_input_change);
green_input.addEventListener("input",rgb_input_change);
blue_input.addEventListener("input",rgb_input_change);

cyan_slider.addEventListener("input",cmyk_slider_update);
magenta_slider.addEventListener("input",cmyk_slider_update);
yellow_slider.addEventListener("input",cmyk_slider_update);
key_slider.addEventListener("input",cmyk_slider_update);

cyan_input.addEventListener("input",cmyk_input_change);
magenta_input.addEventListener("input",cmyk_input_change);
yellow_input.addEventListener("input",cmyk_input_change);
key_input.addEventListener("input",cmyk_input_change);

hue_slider.addEventListener("input",hsv_slider_update);
saturation_slider.addEventListener("input",hsv_slider_update);
value_slider.addEventListener("input",hsv_slider_update);

hue_input.addEventListener("input",hsv_input_change);
saturation_input.addEventListener("input",hsv_input_change);
value_input.addEventListener("input",hsv_input_change);

colorInput.addEventListener("input",picker_update)

