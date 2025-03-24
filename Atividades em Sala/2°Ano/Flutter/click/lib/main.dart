import 'package:flutter/material.dart';
import 'aula_4/atividade.dart';

void main() => runApp(Formatador());

// void main() {
//   runApp(MeuApp());
// }

// class MeuApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       home: Scaffold(
//         appBar: AppBar(
//           title: Text('ListView Example'),
//         ),
//         body: ListView.builder(
//           itemCount: 51,
//           itemBuilder: (context, index) {
//             return InkWell(
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(
//                     builder: (context) => DetalhesItem(index: index),
//                   ),
//                 );
//               },
//               child: ListTile(
//                 title: Text('Item $index'),
//               ),
//             );
//           },
//         ),
//       ),
//     );
//   }
// }

// class DetalhesItem extends StatelessWidget {
//   final int index;

//   DetalhesItem({required this.index});

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Detalhes do Item'),
//       ),
//       body: Center(
//         child: Text('Você clicou no Item $index'),
//       ),
//     );
//   }
// }
