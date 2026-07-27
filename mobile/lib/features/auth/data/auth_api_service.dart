// Handles external server connections
import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthApiService {
  static const String _baseUrl = 'http://10.0.2';

  Future<bool> requestPasswordResetOtp(String email) async {
    try {
      final url = Uri.parse('$_baseUrl/forgot-password');
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email}),
      );

      if (response.statusCode == 200) {
        return true;
      }
      return false;
    } catch (e) {
      return false; // Incase of Network failure
    }
  }
}
