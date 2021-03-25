// function sum(a, b){
//   return a + b;
// }

// console.log(sum(1, 3));

// function compareNumebers(a, b){
//   // return a > b ? 1 : a < b ? -1 : 0;
//   return a - b;

// }

// console.log(compareNumebers(5, 5));
// console.log(compareNumebers(1, 1));
// console.log(compareNumebers(1, 1));


// function superSum(from, upTo){
//   var sum = 0;
//   for (let i = from; i <= upTo; i++){
//     sum += i;   
//   }
//   return sum;
// }
// console.log(superSum(1, 4))
// // console.log(superSum(9, 10))


function ni(number){
  var x = 0;
  for (let i = 1; i <= number; i++){
    x +=i;  
  }
  return x;
}
console.log(ni(5));


function crazy(num) {
  return (num * (4+3)) / 5;
  
}
console.log(crazy(20));

var a = {id: 2};
var b = a;
a.id = 4;
console.log(a.id)


function nine(nuuu) {
    if((nuuu / 2 +1)% 2 ===0){
      return 'par';
    }else {
      return 'impar';
    }
}

console.log(nine(16))



function has(q,w,e) { 
  return (q  + w + e) / 3 >= 7.0;
  
}
console.log(has(10,5,6));