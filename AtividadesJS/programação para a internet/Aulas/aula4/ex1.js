function quest() {
  let name = prompt("Digite seu nome: ");
  let color = prompt("Digite sua cor favorita: ");
  let food = prompt("Digite algo que tu gosta de comer: ");
  let music = prompt("Digite algo q gosta de escultar: ");

  let array = []

  array[0]= name
  array[1]= color
  array[2]= food
  array[3]= music

  document.writeln(
    "Olá " +
      array[0] +
      ", analisei suas preferências e estou vendo que sua cor preferida é " +
      array[1] +
      ", seu prato preferido é " +
      array[2] +
      " e que você gosta de ouvir " +
      array[3] +
      ", agora que já sei de tudo isso, vou selecionar as melhores notícias para você ler hoje!",
  );
}

