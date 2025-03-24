import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:brasil_fields/brasil_fields.dart';

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
                  LengthLimitingTextInputFormatter(5),
                  CentavosInputFormatter(casasDecimais: 2)
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
                  LengthLimitingTextInputFormatter(6),
                  CentavosInputFormatter(casasDecimais: 2)
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
                  var x = UtilBrasilFields.converterMoedaParaDouble(_n1.text) ??
                      0.0;
                  var y = UtilBrasilFields.converterMoedaParaDouble(_n2.text) ??
                      0.0;
                  var z = x + y;

                  _r.text =
                      UtilBrasilFields.obterReal(z, decimal: 2, moeda: false);
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
