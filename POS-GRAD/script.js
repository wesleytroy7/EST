const meuNome ='wesley';
const minhaMensagem = 'Eu,' + meuNome + ',estou realizando uma prova'; 
const textoCompleto = ` ${minhaMensagem} na IGTI`;
console.log(textoCompleto);


let numeros = [100,2,30,28];
console.log('Sem sort:', numeros);
console.log('Com sort:',
numeros.sort( (a, b) =>{
  return a - b  ;
})
);
