import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'app.dart';
import 'features/auth/presentation/controllers/auth_state.dart';


void main() {
  runApp(
    MultiProvider(
      providers: [
      ChangeNotifierProvider<AuthState>(
        create: (BuildContext context) => AuthState(),
      ),
    ],
    child: const MyApp(),
    ),
  );
}

// class MainApp extends StatelessWidget {
//   const MainApp({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp.router(
//       debugShowCheckedModeBanner: false,
//       theme: ThemeData.dark(),
//       routerConfig: appRouter,
//     );
//   }
// }
