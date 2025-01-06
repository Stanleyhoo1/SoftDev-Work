//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

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

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
console.log(fact(5));

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
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

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
console.log(fib(10));
//=================================================================

