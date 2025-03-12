import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
          title: const Text(
            'Perfil do Usuario',
            style: TextStyle(
                color: Color(0xfff9f8f2), fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.blue,
        ),
        body: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Image.network(
                  'https://pm1.aminoapps.com/7530/2830e4e9a92ede1c3bd99e2bf39dcec5e375a7ccr1-365-327v2_hq.jpg'),
              const SizedBox(height: 10),
              const Text(
                'Galo Sniper',
                style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue),
              ),
              const SizedBox(height: 20),
              const Text(
                '10 Anos',
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.red,
                  fontStyle: FontStyle.italic,
                ),
              ),
              const SizedBox(height: 10),
              const Text(
                'Campo Grande',
                style: TextStyle(fontSize: 18, color: Colors.purple),
              ),
              const SizedBox(height: 10),
            ],
          ),
        ),
      ),
    );
  }
}
