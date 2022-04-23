import 'package:flutter/material.dart';
import 'package:flutter_frontend/classes/person.dart';

import 'person.dart';

class Item {
  Person person;
  String itemID;
  String itemName;
  String description;
  double price;
  String location;
  bool status;
  String type;

  Item(this.person, this.itemID, this.itemName, this.description, this.price,
      this.location, this.status, this.type);

  // Item.fromJson(Map<String, dynamic> json)
  //     : ['lender_id'],
  //       ['Item_id'],
  //       ['name'],
  //       ['description'],
  //       ['price'],
  //       ['location'],
  //       ['status'],
  //       ['type'],

  Map toJson() => {
        'lender_id': person.getAadhar,
        'Item_id': itemID,
        'name': itemName,
        'description': description,
        'price': price,
        'location': location,
        'status': status,
        'type': type,
      };
}
