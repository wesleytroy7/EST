'use strict';// o javascript acusa mais erros
window.addEventListener('load', () =>
{

  doMap();
  doFilter();
  doForeach();
  doReduce();
  doFind();
  doSome();
  doEvery();
  doSort();

}

);
//utilizando o map
function doMap() {
  
  {
    const emailArray = people.results.map(person => {
      return  {
        name : person.name,
        email: person.email
      };
    });
    console.log('email');
    console.log(emailArray);
    return emailArray;
  }
}
//utilizando o filter

function doFilter() {
  const maioresDe50 = people.results.filter(person =>
    {
      return person.dob.age > 50; //dob e o nome escolhido para a chave

    });
    console.log('maior de 50');
    console.log(maioresDe50);
    return maioresDe50;
}

function doForeach() {
  const mappedPeople = doMap();
    mappedPeople.forEach(
      person => { 
        person.nameSize =
        person.name.title.length +
        person.name.first.length +
        person.name.last.length;

      }
    );
    console.log('numero deletras');
    console.log(mappedPeople);

}
function doReduce() {
    const totalAges = people.results.reduce((accumulator, current) => {
        return accumulator + current.dob.age;

    },0);//o zero inicia o accumulator 
    console.log(totalAges);

  }

  function doFind() {
    const found = people.results.find(person =>
      {
        return person.location.state === 'Minas Gerais';
      });
      console.log(found);
  }

  function doSome() {
      const found = people.results.some( person => {
          return person.location.state === 'Amazonas';

      });
    console.log(found);  
      
    }

function doEvery() {
    const every = people.results.every( person =>{
        return person.nat === 'US';

    });
    console.log(every);
  }
function doSort() {
    const mappedNames = people.results
    .map( person => {
        return{
          name : person.name.first
          
        };
    })
    .filter(
      person => person.name.startsWith('A')
    )    .sort((a, b) => {
        return a.name.length - b.name.length;
      });
    console.log('teste');
    console.log(mappedNames);
}