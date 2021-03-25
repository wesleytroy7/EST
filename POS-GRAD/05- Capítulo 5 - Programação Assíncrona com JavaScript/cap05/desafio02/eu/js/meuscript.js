/**
 * Estado da aplicação (state)
 */
let tabCountries = null;
let tabFavorites = null;

let allCountries = [];
let favoriteCountries = [];

let countCountries = 0;
let countFavorites = 0;

let totalPopulationList = 0;
let totalPopulationFavorites = 0;

let numberFormat = null;

window.addEventListener('load', () => {//garante que so vai mexer no DOM após carregado
  //mapeamento do DOM
  tabCountries = document.querySelector('#tabCountries');
  tabFavorites = document.querySelector('#tabFavorites');
  countCountries = document.querySelector('#countCountries');
  countFavorites = document.querySelector('#countFavorites');
  totalPopulationList = document.querySelector('#totalPopulationList');

  // prettier-ignore
  totalPopulationFavorites = 
    document.querySelector('#totalPopulationFavorites');

  numberFormat = Intl.NumberFormat('pt-BR');//instanciando 

  fetchCountries();//invocação
});

// async function fetchCountries() {
//   // console.log('Fetching....');
//   const res = await fetch('https://restcountries.eu/rest/v2/all');
//   const json = await res.json();

//   allCountries = json
//     .map((country) => {
//       const { numericCode, translations, population, flag } = country;

//       return {
//         id: numericCode,
//         name: translations.pt,
//         population,
//         formattedPopulation: formatNumber(population),
//         flag,
//       };
//     })
//     .filter((country) => {
//       return !!country.id;
//     }); // Inclusão extra - filtrando somente países com id válido

//   render();
// }

// function render() {
//   renderCountryList();
//   renderFavorites();
//   renderSummary();

//   handleCountryButtons();
// }

// function renderCountryList() {
//   let countriesHTML = '<div>';

//   allCountries.forEach((country) => {
//     const { name, flag, id, population, formattedPopulation } = country;
      
//     //Template literals
//     const countryHTML = `
//       <div class='country'>
//         <div>
//           <a id="${id}" class="waves-effect waves-light btn">+</a>
//         </div>
//         <div>
//           <img src="${flag}" alt="${name}">
//         </div>
//         <div>
//           <ul>
//             <li>${name}</li>
//             <li>${formattedPopulation}</li>
//           </ul>
//         </div>
//       </div>  
//     `;

//     countriesHTML += countryHTML;
//   });

//   countriesHTML += '</div>';''
//   tabCountries.innerHTML = countriesHTML;
// }

// function renderFavorites() {
//   let favoritesHTML = '<div>';

//   favoriteCountries.forEach((country) => {
//     const { name, flag, id, population, formattedPopulation } = country;

//     const favoriteCountryHTML = `
//       <div class='country'>
//         <div>
//           <a id="${id}" class="waves-effect waves-light btn red darken-4">-</a>
//         </div>
//         <div>
//           <img src="${flag}" alt="${name}">
//         </div>
//         <div>
//           <ul>
//             <li>${name}</li>
//             <li>${formattedPopulation}</li>
//           </ul>
//         </div>
//       </div>  
//     `;

//     favoritesHTML += favoriteCountryHTML;
//   });

//   favoritesHTML += '</div>';
//   tabFavorites.innerHTML = favoritesHTML;
// }

// function renderSummary() {
//   countCountries.textContent = allCountries.length;
//   countFavorites.textContent = favoriteCountries.length;

//   const totalPopulation = allCountries.reduce((accumulator, current) => {
//     return accumulator + current.population;
//   }, 0);
// //reduce tem como umas das funcoes é somar 
//   const totalFavorites = favoriteCountries.reduce((accumulator, current) => {
//     return accumulator + current.population;
//   }, 0);

//   totalPopulationList.textContent = formatNumber(totalPopulation);
//   totalPopulationFavorites.textContent = formatNumber(totalFavorites);
// }

// function handleCountryButtons() {
//   //motando um array dos botoes pegando a class btn do materialize
//   //sem o Array retorna um nodelist
//   const countryButtons = Array.from(tabCountries.querySelectorAll('.btn'));
//   const favoriteButtons = Array.from(tabFavorites.querySelectorAll('.btn'));

//   //
//   countryButtons.forEach((button) => {
//     button.addEventListener('click', () => addToFavorites(button.id));
//   });

//   favoriteButtons.forEach((button) => {
//     button.addEventListener('click', () => removeFromFavorites(button.id));
//   });
// }

// function addToFavorites(id) {//id do botao
//   const countryToAdd = allCountries.find((country) => country.id === id);

//   favoriteCountries = [...favoriteCountries, countryToAdd];

//   favoriteCountries.sort((a, b) => {
//     return a.name.localeCompare(b.name);
//   });
// //filter gera outro vetor 
//   allCountries = allCountries.filter((country) => country.id !== id);

//   render();
// }

// function removeFromFavorites(id) {
//   const countryToRemove = favoriteCountries.find(
//     (country) => country.id === id
//   );

//   allCountries = [...allCountries, countryToRemove];

//   allCountries.sort((a, b) => {
//     return a.name.localeCompare(b.name);
//   });

//   favoriteCountries = favoriteCountries.filter((country) => country.id !== id);

//   render();
// }

// function formatNumber(number) {
//   return numberFormat.format(number);
// };


// programação sincrona 
/* function fetchCountries(){
  console.log('fetching ....');

  // const country = fetch('https://restcountries.eu/rest/v2/all');
  // console.log(country); // retorna uma promisse
   fetch('https://restcountries.eu/rest/v2/all')
   // encurtando os comandos,mas é funcional quando se recebe apenas uma valor    
   // .then( response =>{
     // return response.json().then(json => {
       //      (allCountries = json);
       //      console.log(allCountries);
       // })
       // })
       //encurtando
       .then(response => response.json())
       .then(json => {
         allCountries = json;
         // console.log(allCountries);
        })      
      });*/
      
      //programacao assincrona -- escrita assincrona
      //decora a função com async
async function fetchCountries() {
    const response = await fetch('https://restcountries.eu/rest/v2/all');
    const json = await response.json();
      // allCountries = json;
      // console.log(allCountries);
      // console.log(json)
      //=> tratando para pegar apenas o necessario do array
      allCountries = json.map((country) => { 
        // => para minizar mais o codigo é possivel utilizar o object destruction
     const { numericCode, translations, population, flag, region } = country;
        return {
              // verifico os dados que precisa do json e pega sua chave
             
                id: numericCode,
                name: translations.pt,
                population,
                formattedPopulation: formatNumber(population),
                region,
                flag
      }
     
      })
      .filter((country) =>{
        return !!country.id;
      })
      // Inclusão extra - filtrando somente países com id válido


      // console.log(allCountries);
      // favoritesCountries = allCountries;

    render();
    }
function render() {
      // console.log('rendering..');
      renderCountryList();
      renderFavorites();
      renderSummary();
      
    
    handleCountryButtons();
   
  };

function renderCountryList() {
  let countriesHTML = '<div>';
  
    allCountries.forEach((country) => {
      const { name, flag, id, population,  region, formattedPopulation  } = country;
      const countryHTML = `
                <div class= 'country'>
                  <div>
                  <a id="${id}"class="waves-effect waves-light btn">+</a>
                 </div>
              
                  <div>
                    <img src="${flag}" alt="${name}">
                  </div>
                                
                  <div>
                    <ul>
                        <li>${region}</li>
                        <li>${name}</li>
                        <li>${formattedPopulation}</li>
                    </ul>
                  </div>
                </div>
      `;
      countriesHTML += countryHTML;
    });
    countriesHTML += '</div>';
    tabCountries.innerHTML = countriesHTML;
};

function renderFavorites() {
  let favoritesHTML = '<div>';

    favoriteCountries.forEach((country) => {
      const { name, flag, id, population,  region ,formattedPopulation } = country;

      const favoriteCountryHTML = `
      <div class= 'country'>
          <div>
               <a id="${id}" class="waves-effect waves-light btn red darken-4">-</a>
          </div>
          <div>
               <img src="${flag}" alt="${name}">
          </div>
          <div>
            <ul>
              <li>${region}</li>
              <li>${name}</li>
              <li>${formattedPopulation}</li>
            </ul>
          </div>
      </div>     
  `;
      favoritesHTML +=  favoriteCountryHTML;
    
    });
favoritesHTML += '</div>';
tabFavorites.innerHTML = favoritesHTML;


  };

function renderSummary() {
  countCountries.textContent = allCountries.length;
  countFavorites.textContent = favoriteCountries.length;
  const totalPopulation = allCountries.reduce(
    (accumulator, current ) =>{
      return accumulator + current.population;
    },0);

  const totalFavorites = favoriteCountries.reduce((accumulator, current)=>{
    return accumulator + current.population;
  },0);
    totalPopulationList.textContent = formatNumber(totalPopulation);
    totalPopulationFavorites.textContent =
    formatNumber(totalFavorites);
}

function handleCountryButtons() {

      //SEM O ARRAY.FROM RETORNARIA UM NODELIST
      const countryButtons = Array.from(tabCountries.querySelectorAll('.btn'));// faz referencia PARA ESTE CAMPO <a id="${id}" class="waves-effect waves-light btn red darken-4">-</a>
      // console.log(countryButtons);

      const favoritesButtons = Array.from( // pega todos botoes e coloca em novo array
        tabFavorites.querySelectorAll('.btn')
        );
        // console.log(favoritesButtons);
        
        // ação  de adição em favoritos
        // percorre coutryButtons e com a ação de click com chamando a funcao addTo Favorites -> enviado o id
      countryButtons.forEach(button =>{// pega todos botoes e coloca em novo array
        button.addEventListener('click', () => addToFavorites(button.id));
      });
          
        //ação de remoção de favoritos
        // chama a função de remove de favoritos
      favoritesButtons.forEach(button =>{
        button.addEventListener('click', ()=>
        removeFromFavorites(button.id));
      });
  };

  //acoes dos botoes
function addToFavorites(id) { // add nos favoritos recebendo o id de handleCountryButtons->ação de adição 

  const countryToAdd = allCountries.find(country => country.id === id);
      //utilizando o spred 
  favoriteCountries = [...favoriteCountries,  countryToAdd];
  

  // realiza a ordenação alfabetica 
  favoriteCountries.sort((a, b)=>{
      return a.name.localeCompare(b);//compara o nome pela primeira vogal
    });
    allCountries = allCountries.filter(country => country.id !== id);
    // console.log(favoriteCountries.length);
    // console.log(allCountries.length);
    render();

  }
  // console.log(favoriteCountries);
function removeFromFavorites(id) {
  const countryToRemove = favoriteCountries.find(country => country.id === id);
  
  allCountries = [...allCountries, countryToRemove];
  allCountries.sort((a, b) => {
  return a.name.localeCompare(b.name)
  });
  favoriteCountries = favoriteCountries.filter(country=> country.id !== id );
  render();
}

function formatNumber(number) {
  return numberFormat.format(number);
};

