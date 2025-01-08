// Team Grizzly :: Alex Luo and Stanley Hoo 
// SoftDev pd4
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x)
{
    var j=30;
    return j+x;
};

console.log(f(5));
// Can test functions using console log to print the output


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//console.log(o); // logs the object 'o' to console 

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist"); // selects ordered list element with id "thelist"
    var newitem = document.createElement("li"); // creates a new list item element
    newitem.innerHTML = text; // sets inner HTML of new list item
    list.appendChild(newitem); // appends new list item to list
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove(); // removes the nth list item 
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) { // adds 'red' class to each item in list
	items[i].classList.add('red'); 
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) { // alternates between adding 'red' and 'blue' classes
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
function fact(n){
    let product = n;
    if (n===0){
      return 1;
    }
    for (i=n-1; i>0; i-=1){
      product *= i;
    }
    return product;
  }
// FAC
function fib(n){
    if (n===0){
      return 0;
    }
    else if (n===1){
      return 1;
    }
    else if (n===2){
      return 1;
    }
    else {
      return fib(n-1) + fib(n-2);
    }
}
// GCD
function gcd(a,b){
    if (b===0){
        return a;
    }
    else{
        return gcd(b, (a%b));
    }
}


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return param1 + param2;
};

console.log(myFxn(5,10));
addItem("fact of 5: " + fact(5));
stripe();
