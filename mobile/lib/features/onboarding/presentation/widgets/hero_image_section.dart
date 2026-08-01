import 'package:flutter/material.dart';

class HeroImageSection extends StatelessWidget {
  const HeroImageSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Center(
        child: Container(
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(24)),
          child: Image.asset(
            'assets/images/hero_img.png',
            width: double.infinity,
          ),
        ),
      ),
    );
  }
}
