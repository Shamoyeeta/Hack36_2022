import 'package:flutter/material.dart';

class addNewItem extends StatefulWidget {
  const addNewItem({Key? key}) : super(key: key);

  @override
  State<addNewItem> createState() => _addNewItemState();
}

class _addNewItemState extends State<addNewItem> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: true,
        elevation: null,
      ),
      body: Container(
          child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              const Text(
                "Name : ",
                style: TextStyle(
                    fontWeight: FontWeight.bold, color: Colors.black87),
              ),
              const Text("", style: TextStyle(color: Colors.blueGrey)),
            ],
          )
        ],
      )),
    );
  }
}
