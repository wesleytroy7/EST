// console.log('oi');
window.addEventListener('load', function () {
  // fetch('https://api.github.com/users/rrguomide').then(res =>{
  //   res.json().then(dados =>{
  //     showData(dados);
  //   });
  //   })
  //   .catch(error =>{
  //     // console.log('erro');
  //       conso{le.log('Promisse resolvida');
  //   });
  doFetch();
  });
function doFetch() {
    fetch('https://api.github.com/users/rrgomide')
        .then(res => {
            res.json().then(dados =>{
                showData(dados);
            })
        });
};


// function showData(data) {
//   const user = document.querySelector('#u');
//   user.textContent = data.id + '' + data.name;
// }

// const wes = fetch ('https://api.github.com/users/rrgomide');
// console.log(wes);


