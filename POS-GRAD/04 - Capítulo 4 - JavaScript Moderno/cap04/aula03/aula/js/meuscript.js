console.log('oi');
window.addEventListener('load', ()=>{
  doSpread();
  doRest();
  infinitSum();
  doDestruct();
  f4();
});

function doSpread() {
  const marrienMen = people.results.filter(

    person => (person.name.title === 'Mr')
  );
  const marrienM = people.results.filter(

    person => (person.name.title === 'Ms')
  );

    const tudo = [...marrienM, ...marrienMen, {msg: 'oi'}];
    console.log(tudo); 
    
}
function doRest() {
  console.log(infinitSum(2, 3));
}
function infinitSum(...numbers) {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}

function doDestruct() {
  const first = people.results[0];

  const {username, password} = first.login;

  console.log(username);
  console.log(password);
}

const array = [1, 2, 3, 4, 5, 6, 7, 8];
function f4() {
  return array.find(item => item % 4 === 0);
  console.log('oooo');
  console.log(array);
};
