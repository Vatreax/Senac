<?php

class BancoDados {
    public string $host;
    public string $usuario;
    public string $senha;

    public function __construct($host, $usuario, $senha){
        $this->host = $host;
        $this->usuario = $usuario;
        $this->senha = $senha;
    }

    public function connectar(): string {
        if($this->host == 'localhost' && $this->usuario == 'user' && $this->senha == 'pass'){
            return "Conectado ao banco de dados com sucesso";
        }

        return "Não Conectado ao banco de dados";
    }

    public function __destruct() {
        echo "Destruido - Banco de Dados";
    }
}

class Pessoa {
    public string $nome = 'Teste';
    public bool $conectado = false;

    public function __construct($host,$usuario,$password){
        $bd = new BancoDados($host,$usuario,$password);
        if ($bd->connectar() == 'Conectado ao banco de dados com sucesso'){
            $this->conectado = true;
        }
    }

    public function conectado_ao_banco() {
        $conectado = $this->conectado ? 'Sim' : 'Não';
        echo "<p>Conectado: " . $conectado . "</p>";
    }

    public function exibir() {
        echo "<p>$this->nome</p>";
    }

    public function __destruct() {
        echo "Destruido - Pessoa";
    }
}

$rafa = new Pessoa("localhost","user","pass");
$rafa->exibir();

echo $rafa->conectado_ao_banco();