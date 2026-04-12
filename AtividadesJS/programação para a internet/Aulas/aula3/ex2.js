function multiplo() {
        let n = prompt("Digite um número: ");
        for (i = 1; i <= 50; i++) {
        if (i % n == 0) {
            document.writeln( i + ": multiplo" + "<br>");
        } else {
            document.writeln(i + "<br>")
        }
    }
    }