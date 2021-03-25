window.addEventListener('load', ()=>{
f4();
f2();
ex();
});


const array = [1, 2, 3, 4, 5, 6, 7, 8];
function f4() {
  return array.find(item => item % 4 === 0)
  console.log(array);
  };

const  array2 = [1, '2', '3', 4, 5];

function f2() {
  return array2.filter(item => typeof item === 'string');
  console.log(array2);
};


function ex(n1, n2 =20) {
  return n1 + n2 / 4
  console.log();
  ex(10);
}
