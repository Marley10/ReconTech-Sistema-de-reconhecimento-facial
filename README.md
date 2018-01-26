# ReconTech-Sistema-de-reconhecimento-facial
O sistema de reconhecimento facial possui um funcionamento bem simples, operando na placa Dragonboard 410c em linux utilizando apenas dois scripts em python e um banco de dados local criado por meio de pacotes do linux, possui uma precisão considerável, para um sistema fácil de ser feito e relativamente barato.  Add TipAsk Question Step 1: Passo 1: Descrição E Materiais Para o desenvolvimento do sistema de reconhecimento facial foi utilizada a placa Dragonboard 410c além de dois LEDs, um Buzzer, uma webcam e alguns pacotes do linux instalados no linaro, sistema operacional da placa. Foram utilizados os pacotes "mc", "MySQL" e "open cv". Toda a programação foi escrita em python e, portanto, utiliza as respectivas bibliotecas da linguagem. Todos os pacotes foram instalados com o auxílio do "aptitude". Para o funcionamento do programa são necessários o script em python para a captura das informações de nome, idade e rosto do usuário, o banco de dados feito no MySQL para a manipulação de dados e comunicação com o próximo item: o script de leitura facial, também em python.  Add TipAsk Question Step 2: Passo 2: Configuração Do Banco De Dados A primeira coisa que deve ser feita é a configuração de um banco de dados para a troca de informações entre o script de adicionar usuário e o de procurar usuários. Vale lembrar que as imagens gravadas pela câmera para comparação com o vídeo serão gravadas em uma pasta local, fora do banco de dados. Inicialmente é instalado o MySQL para estabelecer o banco de dados que será utilizado nos scripts. Para criar bancos de dados basta seguir os passos do link à seguir:  https://www.vivaolinux.com.br/artigo/Gerenciando-b...  No banco de dados se pode criar inúmeras variáveis para serem requisitadas pelo script para o preenchimento das informações do usuário, para efeito deste tutorial foram criadas duas variáveis, o nome e o CPF, mas estes são apenas exemplos, poderiam ter sido criadas n variáveis, como por exemplo a idade, a cor do cabelo, altura, etc. Também está presente no banco de dados uma possibilidade de ser colocado um número de identificação para a informação armazenada. No script de saída há apenas dois prints para mostrar o nome e o CPF do usuário identificado.  Uma vez configurado o banco de dados, já se pode trabalhar no script para receber as informações.  Add TipAsk Question Step 3: Passo 3: Configurando a Recepção De Dados Do Usuário Nesta parte do tutorial será feita a programação em python do script para receber os dados do usuário, na forma de "raw_input()" para a determinação do nome e do CPF. Para a recepção de dados da câmera já é necessária a utilização do open cv, baixado por meio do linux, além do MySQL para atrelar o código om o banco de dados. O código está disponível nesta página.  Attachments criando_inf.pycriando_inf.pyDownload Add TipAsk Question Step 4: Passo 4: Programando O Reconhecimento Facial E Periféricos Picture of Passo 4: Programando O Reconhecimento Facial E Periféricos A programação utilizada neste script é responsável por comunicar-se com o banco de dados enquanto reconhece a face do usuário, além de ativar os Groves extras ( Buzzer, LEDs). Para esta última é necessário um comando diferente para o python, para que execute comandos no terminal do linux para habilitar a funcionalidade dos pinos corretos na Dragonboard e assegurar que operem corretamente. Os periféricos utilizados estão mostrados na imagem disponível junto ao código disponibilizado.  Attachments recon_face.pyrecon_face.pyDownload Add TipAsk Question Step 5: Passo 5: Testes Nesse tipo de experimento erros são bastante comuns. Normalmente erros ocorrem devido à falhas no código, pinagem, ou até mesmo, imprecisões nos periféricos, como a webcam, portanto, é recomendável fazer diversos teste, com fundos de cores diferentes, pessoas diferentes etc. Este código é mais recomendável para apenas um usuário por vez, já que podem haver problemas com a detecção e reconhecimento de mais de uma face.
Step 1: Passo 1: Descrição E Materiais
Para o desenvolvimento do sistema de reconhecimento facial foi utilizada a placa Dragonboard 410c além de dois LEDs, um Buzzer, uma webcam e alguns pacotes do linux instalados no linaro, sistema operacional da placa. Foram utilizados os pacotes "mc", "MySQL" e "open cv". Toda a programação foi escrita em python e, portanto, utiliza as respectivas bibliotecas da linguagem. Todos os pacotes foram instalados com o auxílio do "aptitude". Para o funcionamento do programa são necessários o script em python para a captura das informações de nome, idade e rosto do usuário, o banco de dados feito no MySQL para a manipulação de dados e comunicação com o próximo item: o script de leitura facial, também em python.
Step 2: Passo 2: Configuração Do Banco De Dados
A primeira coisa que deve ser feita é a configuração de um banco de dados para a troca de informações entre o script de adicionar usuário e o de procurar usuários. Vale lembrar que as imagens gravadas pela câmera para comparação com o vídeo serão gravadas em uma pasta local, fora do banco de dados. Inicialmente é instalado o MySQL para estabelecer o banco de dados que será utilizado nos scripts. Para criar bancos de dados basta seguir os passos do link à seguir:

https://www.vivaolinux.com.br/artigo/Gerenciando-b...

No banco de dados se pode criar inúmeras variáveis para serem requisitadas pelo script para o preenchimento das informações do usuário, para efeito deste tutorial foram criadas duas variáveis, o nome e o CPF, mas estes são apenas exemplos, poderiam ter sido criadas n variáveis, como por exemplo a idade, a cor do cabelo, altura, etc. Também está presente no banco de dados uma possibilidade de ser colocado um número de identificação para a informação armazenada. No script de saída há apenas dois prints para mostrar o nome e o CPF do usuário identificado.

Uma vez configurado o banco de dados, já se pode trabalhar no script para receber as informações.
Step 3: Passo 3: Configurando a Recepção De Dados Do Usuário
Nesta parte do tutorial será feita a programação em python do script para receber os dados do usuário, na forma de "raw_input()" para a determinação do nome e do CPF. Para a recepção de dados da câmera já é necessária a utilização do open cv, baixado por meio do linux, além do MySQL para atrelar o código om o banco de dados. O código está disponível nesta página.
A programação utilizada neste script é responsável por comunicar-se com o banco de dados enquanto reconhece a face do usuário, além de ativar os Groves extras ( Buzzer, LEDs). Para esta última é necessário um comando diferente para o python, para que execute comandos no terminal do linux para habilitar a funcionalidade dos pinos corretos na Dragonboard e assegurar que operem corretamente. Os periféricos utilizados estão mostrados na imagem disponível junto ao código disponibilizado.