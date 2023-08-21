import 'package:digital_eye/Showimage.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:firebase_database/firebase_database.dart';

class Movement extends StatefulWidget {
  @override
  _MovementState createState() => _MovementState();
}

class _MovementState extends State<Movement> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder(
          stream: FirebaseDatabase.instance.reference().child('Movement').onValue,
          builder: (BuildContext context, snapshot) {
            if (snapshot.hasData) {
              Map<dynamic, dynamic> map = snapshot.data.snapshot.value;
              return GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2),
                itemCount: map.values
                    .toList()
                    .length,
                itemBuilder: (BuildContext context, index) {
                  return Container(
                    margin: EdgeInsets.all(5.0),
                    width: MediaQuery.of(context).size.width/100 * 50,
                    height: MediaQuery.of(context).size.height/100 * 40,
                    child: GestureDetector(
                      onTap: (){
                        Navigator.of(context).push(MaterialPageRoute
                          (builder: (context) => Showimage(map.values.toList()[index])));
                      },
                      child: Image.network(map.values.toList()[index],
                        fit: BoxFit.fill,
                        filterQuality: FilterQuality.high,
                      ),
                    ),
                  );
                },
              );
            }
            else {
              return CircularProgressIndicator();
            }
          }
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.lock_open),
        onPressed: (){
          FirebaseDatabase.instance.reference().child('motor').set(1);
        },
      ),
    );
  }
}
