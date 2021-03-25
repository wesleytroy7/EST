// window.addEventListener('load', function () {
//   getGroupMembers();
//   getFullName();

// })

function getGroupMembers() {
  const groupPersons = ['Matheus de Souza',
  'Marco Antonio Salles da Silva',
  'Michelle Vieira de Messias',
  'Tatiana Fagundes Fischer',
  'Guilherme Lospes Lader',
  'Diego da Silva Ressureição',
  'Wesley Angelo Ferreira'];
  

  return groupPersons.sort();
  
} ;

console.log(getGroupMembers());

function getFullName(...names) {
  return names.join(' ');
};
console.log(getFullName('José', 'Vieira', 'Silva'));


function transform(input) {
  return input.map( num => num / 10 + 1);
};
console.log(transform([10, 20, 30, 40, 50]));
console.log(transform([61, 72, 83, 94]));

function onlyNumbersFrom(onlyNum){
  return onlyNum
  .split('')
  .filter(char => !isNaN(char) && char !== ' ' )
  
};
console.log(onlyNumbersFrom('s24343435, 242344 , reggggg, 34534tg5'));

