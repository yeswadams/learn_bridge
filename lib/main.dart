import 'package:flutter/material.dart';

class HitType {
  final String name;
  const HitType(this.name);
}

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark(),
      home: const OnboardingScreen(),
    );
  }
}

class OnboardingScreen extends StatelessWidget {
  const OnboardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF121212),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Align(
                alignment: Alignment.centerRight,
                child: TextButton(
                  onPressed: () {
                    // Implement functionality here
                  },
                  child: const Text(
                    'Skip',
                    style: TextStyle(color: Colors.white70, fontSize: 16),
                  ),
                ),
              ),
              const SizedBox(height: 20),

              // 2. Hero Graphic Area
              Expanded(
                child: Center(
                  child: Container(
                    decoration: BoxDecoration(
                      color: Colors.transparent,
                      borderRadius: BorderRadius.circular(24),
                    ),
                    child: Center(
                      child: Image.asset(
                        'assets/images/hero_img.png',
                        width: double.infinity,
                      ),
                    ),
                  ),
                ),
              ),

              const SizedBox(height: 32),

              // 3. Main Headline Text
              const Text(
                'Start learning\nanywhere, and build\nyour bright career.',
                style: TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                  height: 1.2,
                ),
              ),

              const SizedBox(height: 12),

              // 4. Subtitle Text
              const Text(
                'Basic to advance level of designing with expert instructor and fee bonus classess',
                style: TextStyle(
                  fontSize: 15,
                  color: Colors.white54,
                  height: 1.4,
                ),
              ),

              const SizedBox(height: 32),

              // 5. Primary Action Button
              SizedBox(
                width: double.infinity,
                height: 56,
                child: ElevatedButton(
                  onPressed: () {
                    // Should Navigate to home Screen
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF7C65C1),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                    elevation: 0,
                  ),
                  child: const Text(
                    'Start Learning',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w600,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
