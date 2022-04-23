class Person {
  String fullname;
  String aadhar;
  String address;
  String phone;
  String password;
  String email;

  Person(this.fullname, this.aadhar, this.address, this.phone, this.password,
      this.email);

  get getAadhar => this.aadhar;

  Map toJson() => {
        'Aadhar_id': aadhar,
        'name': fullname,
        'address': address,
        'phone_no': phone,
        'email': email,
        'password': password, // Todo: Encrypt
      };
}
