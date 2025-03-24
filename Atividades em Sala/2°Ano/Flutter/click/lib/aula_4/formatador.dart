import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class Formatador extends StatelessWidget {
  var _n1 = TextEditingController();
  var _n2 = TextEditingController();
  var _r = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('Calculadora'),
        ),
        body: Padding(
          padding: EdgeInsets.all(10),
          child: Column(
            children: [
              TextField(
                controller: _n1,
                decoration: InputDecoration(
                  labelText: 'Insira o primeiro número',
                ),
                keyboardType: TextInputType.number,
                inputFormatters: [
                  FilteringTextInputFormatter.digitsOnly,
                  LengthLimitingTextInputFormatter(5)
                ],
              ),
              TextField(
                controller: _n2,
                decoration: InputDecoration(
                  labelText: 'Insira o segundo número',
                ),
                keyboardType: TextInputType.number,
                inputFormatters: [
                  FilteringTextInputFormatter.digitsOnly,
                  LengthLimitingTextInputFormatter(5)
                ],
              ),
              TextField(
                controller: _r,
                decoration: InputDecoration(
                  labelText: 'Resultado',
                ),
                readOnly: true,
              ),
              SizedBox(
                height: 10,
              ),
              FilledButton(
                onPressed: () {
                  var x = double.tryParse(_n1.text) ?? 0.0;
                  var y = double.tryParse(_n2.text) ?? 0.0;
                  var z = x + y;

                  _r.text = z.toString();
                },
                child: Text('somar'),
              )
            ],
          ),
        ),
      ),
    );
  }
}
