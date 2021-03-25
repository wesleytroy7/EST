
//so vai executar quando a pagina terminar de 
//carregar
window.addEventListener('load', start);
//isolando os dados 
var globalNames = ['um', 'dois', 'tres','quatro'];
var inputName = null;
var isEditing = false;
var currentIndex



function start() {
  // console.log('oi');
  inputName = document.querySelector('#inputName');
  preventFormSUbmit();// evita que o form seja recarregado com preventdefault
  activateInput();// manda ativar o input -> enviando o cursor direto para ele 
  render();
}
//pegando o evento Enter que enviado implicitamente
//escuta a digitação do usuário
function activateInput(){
  function updateName(newName) {
       globalNames[currentIndex] = newName;
  }

  function handleTyping(event) {
    // !! significa que eu torno algo realmente verdadeiravel ou falseavel, neste caso tem que ter valor
    // trim() !=='' retira os espaços em 
    let hasText = !!event.target.value && event.target.value.trim() !=='';
      if (!hasText) {
        clearInput();
        return;
      }
    

    // console.log(event); // No target consigo capturar o tipo de evento
    if (event.key === 'Enter') { // o keyup for igual a ENTER
      // console.log(event.target.value);
      if(isEditing){//Recebendo o dado para edição
        // console.log('Editing...');
        updateName(event.target.value);
      }
      else {
        insertName(event.target.value);
        // console.log('Inserting ...');
        }
      render();
      isEditing = false; // por padrão devevoltar ao modo inserção  
      clearInput();
    }
  function insertName(newName) {
    globalNames.push(newName);    
     
  }
    
  }
  inputName.addEventListener('keyup', handleTyping);
  inputName.focus();
}

/// função 
function preventFormSUbmit() {
  function handleFormSubmit(event) {//recebe um evento implicito,o nome pode ser qualquer um.
    event.preventDefault();//preventDefault previne o refrech na pagina
  }
  //pegando a referencia do form 
  var form = document.querySelector('form');
  //form tem um envento de submit
  form.addEventListener('submit', handleFormSubmit);//quando se trabalha com evento ele envia um parametro implicito (chamado de evento)
}

function render(){

  //deletar botao 
  function creteDeleteButton(i) {//cloger (conceito)
    function deleteName() {
      // console.log('deleteName')
      globalNames.splice(i, 1);
      render();      
    }
    let button = document.createElement('button');
    button.classList.add('deleteButton');
    button.textContent = 'x';
    button.addEventListener('click', deleteName);// chama a funcao deleteName
    return button;
  }
  //editar dado
  function createSpan(name, index) {
    function editItem() {
      inputName.value= name;
      inputName.focus();
      isEditing = true;
      currentIndex = index
     
    }
    let  span = document.createElement('span');
    span.classList.add('clickable');
    span.textContent = name; 
    span.addEventListener('click', editItem);//chama a funcao editItem
   return span;
  }
  
  
  let divNames = document.querySelector('#names');
  // divNames.innerHTML = '<ul><li>Nome 01</li><li>nome 02</li></ul>'
  divNames.innerHTML = ''; // limpa a div após a inserção ,para não ocorrer repetição
  //criar ul
  //Fazer N li's , conforme tamanho do vetor globalNames
  let ul = document.createElement('ul');
  // let li1 = document.createElement('li');
  // let li2 = document.createElement('li');
  // li1.textContent = 'Prim';
  // li2.textContent = 'Seg';
  // ul.appendChild(li1);
  // ul.appendChild(li2);
  for (let i = 0; i < globalNames.length; i++) {// percorre o vetor
    const currentName = globalNames [i];
    let li = document.createElement('li');// cria uma linha
    // li.textContent = currentName;// recebe o texto 
  
    let button = creteDeleteButton(i); // chama a função de criação de botao e envia index que veio do for
    let span = createSpan(currentName, i);// recebendo o texto e o index
    

    li.appendChild(button);
    li.appendChild(span);
    ul.appendChild(li);
    // ul.appendChild(li)  // fecha a linha
  }
  divNames.appendChild(ul);//fecha a div
    }
function clearInput() {
  inputName.value =''; // limpa o inputName após o enter
inputName.focus();
}