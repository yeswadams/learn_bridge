import "package:flutter/material.dart";
import "package:go_router/go_router.dart";

class PrimaryActionButton extends StatelessWidget {
  const PrimaryActionButton();

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      height: 56,
      child: ElevatedButton(
        onPressed: () {
          context.go('/home');
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
    );
  }
}
