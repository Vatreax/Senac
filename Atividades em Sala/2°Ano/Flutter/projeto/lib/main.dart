import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
} 
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: UserProfile(),
    );
  }
}

class UserProfile extends StatefulWidget {
  @override
  _UserProfileState createState() => _UserProfileState();
}


class _UserProfileState extends State<UserProfile> {
  List<String> userNames = [
    "Roberval",
    "Juvenal",
    "Doberval",
    "Jureg",
    "Ximira"
  ];

  int currentIndex = 0;
  void changeUserName() {
    setState(() {

      currentIndex = (currentIndex + 1) % userNames.length;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor:  Color.fromARGB(255, 0, 0, 0),
        appBar:
        AppBar(
          title: Text(
            'Perfil',
            style: TextStyle(color: Color.fromARGB(255, 0, 0, 0), fontWeight: FontWeight.w600), textAlign: TextAlign.center),
            backgroundColor:  Color.fromARGB(255, 255, 255, 255),
    
        ),
        body: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                width: 150,
                height: 150,
              ),

              Text(
                '${userNames[currentIndex]}',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Color.fromARGB(255, 255, 255, 255)),
              ),
              SizedBox(height: 20),
              Text(
                '10 Anos',
                style: TextStyle(
                  fontSize: 20,
                  color: Color.fromARGB(255, 255, 254, 254),
                  fontStyle: FontStyle.italic,
                ),
              ),
              SizedBox(height: 20),
              Text(
                'Campo Grande',
                style: TextStyle(fontSize: 20, color: Color.fromARGB(255, 255, 255, 255)),
              ),
              SizedBox(height: 20),
              ElevatedButton(onPressed: changeUserName, child: Text('Aperta Ai'))
            ],
          ),
        ),
      ),
    );
  }
}



// Explicação:
// Lista de Nomes: A variável userNames contém uma lista de nomes que o usuário pode ter.
// Índice do Nome Atual: A variável currentIndex mantém o índice do nome atual da lista.
// Alteração do Nome: A função _changeUserName altera o índice do nome atual. Quando o índice chega ao final da lista, ele volta para o início usando a operação % userNames.length (módulo).
// Exibição do Nome: O nome exibido na tela é o nome no índice atual da lista.
// Resultado:
// Cada vez que você clica no botão, o nome do usuário vai mudar para o próximo nome na lista. Quando chega ao último nome, ele volta para o primeiro nome da lista, criando um ciclo.