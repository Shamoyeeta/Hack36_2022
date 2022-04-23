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

  Item(this.person, this.itemID, this.itemName, this.description, this.price,
      this.location, this.status);

  Map toJson() => {
        'lender_id': person.getAadhar,
        'Item_id': itemID,
        'name': itemName,
        'description': description,
        'price': price,
        'location': location,
        'status': status,
      };
}
