import 'package:flutter/material.dart';
import 'package:learn_bridge/features/onboarding/presentation/widgets/header_section.dart';
import 'package:learn_bridge/features/onboarding/presentation/widgets/hero_image_section.dart';
import 'package:learn_bridge/features/onboarding/presentation/widgets/primary_action_button.dart';
import 'package:learn_bridge/features/onboarding/presentation/widgets/content_section.dart';

class OnboardingScreen extends StatelessWidget {
  const OnboardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home Screen')),
      backgroundColor: const Color(0xFF121212),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              HeaderSection(),
              SizedBox(height: 20),
              HeroImageSection(),
              SizedBox(height: 32),
              ContentSection(),
              SizedBox(height: 32),
              PrimaryActionButton(),
            ],
          ),
        ),
      ),
    );
  }
}
