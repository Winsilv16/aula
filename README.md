<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layout 1</title>
    <link rel="stylesheet" href="layout.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="Interfaces para desenvolvimento.html">Início</a></li>
                <li><a href="Layout2.html">Contato</a></li>
                <li><a href="layout3.html">Serviços</a></li>
                <li><a href="layout4.html">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>Align Center</h1>
            <p>Empresa dedicada ao turismo.</p>
            <img src="menina.png" alt="Imagem de uma menina">
        </section>
    <footer>
        <div class="footer-images">
            <img src="LAYOUT1.jpg" alt="Imagem de praia">
            <img src="LAYOUT2.jpg" alt="Imagem dos Lençóis Maranhenses">
            <img src="LAYOUT3.jpg" alt="Imagem de montanha">
            <img src="LAYOUT4.jpg" alt="Imagem de balão">
        </div>
        <p> 2025 - IFRN.</p>
    </footer>
</body>
</html>
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
        .container {
            display: flex; 
            justify-content: center; 
            padding: 20px; 
        }

        .imagem-1, .imagem-2, .imagem-3, .imagem-4 {
            margin: 10px; 
            border: 2px solid #333; 
            padding: 5px;
        }

        img {
            max-width: 200px;
            height: auto; 
            display: block;
        }
  
        body {
            text-align: center; 
        }

        footer {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: left; 
        }
        
        .footer-images {
            display: flex;
            justify-content: center;
        }

        .footer-images img {
            width: 150px;
            height: auto;
            margin: 0 10px;
            border-radius: 5px;
        }

   
        .hero {
            border: 2px solid #333; 
            padding: 20px; 
            margin: 20px auto; 
            max-width: 600px;
        }

        .hero h1 {
            border: 2px solid #333; 
            padding: 10px; 
            display: inline-block; 
        }

        .hero img {
            display: block;
            margin: 0 auto; 
            max-width: 100%; 
            height: auto;
        }

header {
    background-color: #4CAF50;
    color: white;
    padding: 15px;
    text-align: center;
}
nav ul {
    list-style-type: none;
    padding: 0;
}
nav ul li {
    display: inline;
    margin-right: 10px;
}
main {
    padding: 20px;
}
.hero img {
    max-width: 100%;
    height: auto;
}
footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}

</style>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layout 2</title>
    <link rel="stylesheet" href="Layout2.css">
    <style>
        
 body {
     font-family: Arial, sans-serif;
     margin: 0;
     padding: 0;
     min-height: 100vh; 
     margin: 0; 
     display: flex;
     flex-direction: column;
 }


 footer {
     background-color: #333;
     color: white;
     text-align: center;
     padding: 10px;
     position: sticky; 
     top: 100vh; 
 }

main {
    display: flex; 
    justify-content: space-around;
    flex: 1; 
    align-items: flex-start; 
    
}

.formulario-contato, .suporte {
    width: 45%; 
    
    padding: 20px;
    
    border: 1px solid #ccc; 
    
    box-sizing: border-box; 
    
}

.suporte img {
    max-width: 100%; 
    
    height: auto;
    display: block;
    margin: 0 auto;
    
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 15px;
    text-align: center;
}
main {
    padding: 20px;
}
form {
    margin-bottom: 20px;
}

        /* Estilos para o cabeçalho */
        header {
            background-color: #f0f0f0; /* Cor de fundo para o cabeçalho */
            padding: 10px; /* Espaçamento interno */
        }

        /* Estilos para a navegação */
        nav ul {
            list-style: none; /* Remove os marcadores da lista */
            padding: 0;
            margin: 0;
            display: flex; /* Alinha os itens da lista horizontalmente */
            justify-content: center; /* Centraliza os itens da lista */
        }

        nav li {
            margin: 0 10px; /* Espaçamento entre os itens da lista */
        }

        nav a {
            text-decoration: none; /* Remove o sublinhado dos links */
            color: #333; /* Cor do texto dos links */
            display: block; /* Faz com que o link ocupe todo o espaço do item da lista */
            padding: 5px 10px; /* Adiciona um espaçamento interno aos links */
        }

        nav a:hover {
            background-color: #ddd; /* Cor de fundo ao passar o mouse */
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="Interfaces para desenvolvimento.html">Início</a></li>
                <li><a href="Layout2.html">Contato</a></li>
                <li><a href="layout3.html">Serviços</a></li>
                <li><a href="layout4.html">Home</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="formulario-contato">
            <form action="#" method="post">
                <label for="nome">Nome:</label><br />
                <input type="text" id="nome" name="nome"><br />

                <label for="email">Email:</label><br />
                <input type="email" id="email" name="email"><br />

                <label for="mensagem">Mensagem:</label><br />
                <textarea id="mensagem" name="mensagem"></textarea><br />

                <button type="submit">Enviar</button><br />
            </form>
        </section>

        <aside class="suporte">
            <img src="suporte-ao-cliente.png" alt="Suporte ao Cliente">
            <p>Precisa de ajuda? Nossa equipe de suporte está pronta para te atender!</p>
        </aside>
    </main>

    <footer>
        <p> 2025 - IFRN.</p>
    </footer>
</body>
</html>
