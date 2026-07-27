// Handles external server connections
import 'dart:convert';
import 'package:http/http.dart';

class AuthApiService {
  static const String _baseUrl = 'http://10.0.2';

  Future<bool> requestPasswordResetOTP(String email) async {
    try {
      final url = Uri.parse('$_baseUrl/forgot-password');
    }
  }
}
