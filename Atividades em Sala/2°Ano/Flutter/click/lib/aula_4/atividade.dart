import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:brasil_fields/brasil_fields.dart';

class Formatador extends StatelessWidget {
  var _n1 = TextEditingController();
  var _n2 = TextEditingController();
  var _r = TextEditingController();

  var _formulario = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('Calculadora'),
        ),
        body: Form(
          key: _formulario,
          child: Column(
            children: [
              TextFormField(
                  controller: _n1,
                  decoration: InputDecoration(
                    labelText: 'Insira o primeiro número',
                  ),
                  inputFormatters: [
                    FilteringTextInputFormatter.digitsOnly,
                    LengthLimitingTextInputFormatter(5),
                  ],
                  keyboardType: TextInputType.number,
                  validator: (valor) {
                    if (valor == null || valor.isEmpty) {
                      return 'O campo é obrigatório';
                    } else if (int.tryParse(valor)! < 0) {
                      return 'Digite um número acima de 0';
                    }
                    return null;
                  }),
              TextFormField(
                  controller: _n2,
                  decoration: InputDecoration(
                    labelText: 'Insira o segundo número',
                  ),
                  inputFormatters: [
                    FilteringTextInputFormatter.digitsOnly,
                    LengthLimitingTextInputFormatter(5),
                  ],
                  keyboardType: TextInputType.number,
                  validator: (valor) {
                    if (valor == null || valor.isEmpty) {
                      return 'O campo é obrigatório';
                    } else if (int.tryParse(valor)! <= 0) {
                      return 'Digite um número acima de 0';
                    }
                    return null;
                  }),
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
                  if (_formulario.currentState!.validate()) {
                    var x = UtilBrasilFields.converterMoedaParaDouble(_n1.text);

                    var y = UtilBrasilFields.converterMoedaParaDouble(_n2.text);

                    var z = x + y;

                    _r.text = r'R$' +
                        UtilBrasilFields.obterReal(
                          z,
                          moeda: false,
                        );
                  }
                },
                child: const Text('somar'),
              )
            ],
          ),
        ),
      ),
    );
  }
}
