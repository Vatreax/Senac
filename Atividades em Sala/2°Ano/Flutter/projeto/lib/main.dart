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
                child: Image.asset('../images/galosniper.webp'),  
                decoration: BoxDecoration(borderRadius: BorderRadius.circular(20)),
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


