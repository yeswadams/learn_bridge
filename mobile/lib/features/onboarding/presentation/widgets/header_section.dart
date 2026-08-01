import "package:flutter/material.dart";

class HeaderSection extends StatelessWidget {
  const HeaderSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.centerRight,
      child: TextButton(
        onPressed: () {
          // Skip logic here
        },
        child: const Text(
          'Skip',
          style: TextStyle(color: Colors.white70, fontSize: 16),
        ),
      ),
    );
  }
}