import 'package:flutter_frontend/classes/item.dart';
import 'package:flutter_frontend/classes/person.dart';

class Borrow {
  Person borrower;
  Item item;
  double price;
  DateTime borrowDate;
  DateTime returnDate;

  Borrow(
      this.borrower, this.item, this.price, this.borrowDate, this.returnDate);

  Map toJson() => {
        'item_id': item.itemID,
        'borrower_id': borrower.aadhar,
        'amount': price,
        'borrowDate': borrowDate,
        'returnDate': returnDate,
      };
}
