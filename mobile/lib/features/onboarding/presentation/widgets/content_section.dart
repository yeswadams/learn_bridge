import "package:flutter/material.dart";

class ContentSection extends StatelessWidget {
  const ContentSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: const [
        Text(
          'Start Learning\nanywhere, and build\nyour bright career.',
          style: TextStyle(
            fontSize: 32,
            fontWeight: FontWeight.bold,
            color: Colors.white,
            height: 1.2,
          ),
        ),
        SizedBox(height: 12),
        Text(
          'Basic to advance level of designing with expert instructor and fee bonus classes.',
          style: TextStyle(fontSize: 15, color: Colors.white54, height: 1.4),
        ),
      ],
    );
  }
}
