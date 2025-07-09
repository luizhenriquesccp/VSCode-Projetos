function mostrarNumeroAleatorio() {
  const numero = Math.floor(Math.random() * 100) + 1;
  document.getElementById("resultado").textContent = "Número aleatório: " + numero;
}