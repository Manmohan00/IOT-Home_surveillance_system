import 'package:digital_eye/Images.dart';
import 'package:digital_eye/Movement.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        visualDensity: VisualDensity.adaptivePlatformDensity,
       // brightness: Brightness.dark,
      ),
      home: DefaultTabController(
        length: 2,
        child: Scaffold(
          backgroundColor: Colors.transparent,
          appBar:  AppBar(
              leading: Icon(Icons.remove_red_eye,
                color: Colors.white60,),
              elevation: 2.0,
              centerTitle: true,
              backgroundColor: Colors.green,
              title: Text("Remote Eye",
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  letterSpacing: 4.0,
                ),
              ),
            bottom: TabBar(
              tabs: [
                Text("Regular Updates"),
                Text("Movement ")
              ],
            ),
          ),
          body: TabBarView(
            children: [
              Images(),
              Movement(),
            ],
          ),
        ),
      )
    );
  }
}
