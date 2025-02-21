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
</head>
<body>
    <header>
        <h1>Entre em Contato Conosco</h1>
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

</style>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layout 3</title>
    <link rel="stylesheet" href="layout3.css">
    <style>
      .sobre-nos {
        text-align: center;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid #ccc;
      }
      
      .membros-equipe {
          display: flex; /* Para alinhar os membros da equipe horizontalmente */
          justify-content: space-around; /* Para adicionar um espaçamento entre os membros */
      }

      .membro {
          margin: 20px; /* Adiciona um espaçamento de 20px ao redor de cada membro */
      }
      
      .membro img {
          border: 2px solid #333; /* Adiciona uma borda de 2px preta */
      }
    </style>
</head>
<body>
    <header>
        <h1>Nossa Equipe</h1>
    </header>

    <main class="membros-equipe">
 
      <article class="membro">
          <img src="mulher-negra.png" alt="Mulher Negra" style="max-width:100%; height:auto;">
          <h3>Maria</h3>
          <p>Atendente</p>
      </article>

      <article class="membro">
          <img src="tio.png" alt="Tio" style="max-width:100%; height:auto;">
          <h3>Paulo</h3>
          <p>Piloto</p>
      </article>
      
   
    </main>
    
    <section class="sobre-nos">
        <h2>Sobre Nós</h2>
        <p>Somos uma Empresa de transportes aérios<br> levamos voçe ao seu destino favorito, realizando sonhos e transformando vidas por meio do transporte.</p>
    </section>

    <footer>
      <p> 2025 - IFRN</p>
    </footer>
</body>
</html>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
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
.membros-equipe {
    display: flex;
    flex-wrap: wrap;
}
.membro {
    margin-right: 20px;
    margin-bottom: 20px;
}
footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}

  <style>
    body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
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
.membros-equipe {
    display: flex;
    flex-wrap: wrap;
}
.membro {
    margin-right: 20px;
    margin-bottom: 20px;
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
    <title>Layout 4</title>
    <style>
        /* Estilos gerais */
        body {
            text-align: center; /* Centraliza o conteúdo no corpo */
            min-height: 100vh; /* Garante que o body tenha pelo menos a altura da tela */
            margin: 0; /* Remove margens padrão */
            display: flex;
            flex-direction: column;
        }

        /* Estilos para o cabeçalho */
        header {
            flex-shrink: 0; /* Evita que o cabeçalho encolha */
        }

        /* Estilos para o main */
        main {
            display: flex; /* Coloca as seções lado a lado */
            justify-content: space-around; /* Espaçamento entre as seções */
            align-items: flex-start; /* Alinha as seções ao topo */
            flex: 1; /* Ocupa o espaço restante */
        }

        section {
            width: 45%; /* Largura de cada seção */
            padding: 20px;
            border: 1px solid #ccc; /* Adiciona uma borda para visualização */
            box-sizing: border-box; /* Inclui borda e padding na largura */
        }

        /* Estilos para o rodapé */
        footer {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: left; /* Remove a centralização */
            display: flex;
            flex-direction: column;
            align-items: center;
            flex-shrink: 0; /* Evita que o rodapé encolha */
        }

        .footer-images {
            display: flex;
            justify-content: center;
            margin-bottom: 10px; /* Espaço entre as imagens e o texto */
        }

        .footer-images img {
            width: 150px; /* Largura das imagens */
            height: auto;
            margin: 0 10px; /* Espaçamento entre as imagens */
            border-radius: 5px; /* Borda arredondada */
        }

        .contact-info {
            margin-bottom: 10px;
            text-align: left; /* Alinha o texto à esquerda */
        }

        .contact-info p {
            margin: 5px 0; /* Espaçamento entre os parágrafos */
        }
    </style>
</head>
<body>
    <header>
        <h1>Encontre-nos ou Reclame Aqui</h1>
    </header>
    <main>
        <section class="localizacao">
            <h2>Nossa Localização</h2>
            <img src="mapa.png" alt="Mapa da Nossa Localização">
            <p>Nós estamos localizados na Rua do IFRN, 123 - Centro, Cidade/NATAL</p>
        </section>

        <section class="reclamacao">
            <h2>Reclamações</h2>
            <img src="reclamar.png" alt="Ícone de Reclamação">
            <form class="formulario-reclamacao" action="#" method="post">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="mensagem">Mensagem:</label>
                <textarea id="mensagem" name="mensagem" rows="5" required></textarea>

                <input type="submit" value="Enviar Reclamação">
            </form>
        </section>
    </main>

    <footer>
        <div class="footer-images">
            <img src="LAYOUT1.jpg" alt="Imagem de praia">
            <img src="LAYOUT2.jpg" alt="Imagem dos Lençóis Maranhenses">
            <img src="LAYOUT3.jpg" alt="Imagem de montanha">
            <img src="LAYOUT4.jpg" alt="Imagem de balão">
        </div>
        <div class="contact-info">
            <p>Entre em contato conosco:</p>
            <p>Email: contato@transportesaereos.com</p>
            <p>Telefone: (84) 99999-9999</p>
        </div>
        <p>2025 - IFRN.</p>
    </footer>
</body>
</html>

<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0; 
}
header {
    background-color: #4CAF50; 
    color: white; 
    padding: 15px; 
    text-align:center; 
}
main { 
    padding: 20px;
} 
footer { 
    text-align:center; 
    padding: 10px;
    background-color: #f1f1f1;
} 
.localizacao img { 
    max-width: 100%;
    height: auto;
}
.formulario-reclamacao label,
.formulario-reclamacao input,
.formulario-reclamacao textarea {
    display: block;
    margin-bottom: 10px; 
}
.formulario-reclamacao input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
}
</style>
