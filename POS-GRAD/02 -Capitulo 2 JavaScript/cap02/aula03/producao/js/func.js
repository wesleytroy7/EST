// var a = -5;
// var b = 0;

// if ( a > b ) {
//   console.log(a + ' é maior que ' + b)
// }else {
//     if(a < b ) {
//       console.log( a + ' é menor que ' + b)
//       }else {
//         console.log(a + ' é igual a ' + b)
//       }
// }
var dia = 3;
switch (dia) {
  case 1: r = 'Domingo';    
    break;
  case 2: r = 'Segunda';
    break;
  case 3: r = 'Terça';
    break;
  case 4: r = 'Quarta';
    break;
  case 5: r = 'Quinta';
    break;
  case 6: r = 'Sexta';
    break;
  case 7: r = 'Sabado';
      
  default: r = 'Dia invalido'
    }
console.log(r)


a = 6;
b = 7;
var resposta = a > b ? 'Maior' : a < b ? 'Menor' : 'Igual';
console.log(resposta)


var contador = 1;
var somatorio = 0;

while ( contador <= 10) {
    somatorio += contador;
    contador++;
};
console.log(somatorio)
var cont = 1;
var somar = 0;
do{
    somar += cont;
    cont++;
    
}while(cont <= 10)
console.log(somar)
summ = 0;
for (let i = 0; i < 10; i++) {
    summ+=i;

}
console.log(summ)