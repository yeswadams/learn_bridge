import "package:flutter/material.dart";
import "../../data/auth_api_service.dart";

class AuthState extends ChangeNotifier {
  final AuthApiService _apiService = AuthApiService();

  bool _isLoading = false;
  String _email = '';
  String? _statusMessage;
  bool _isSuccess = false;

  bool get isLoading => _isLoading;
  String get email => _email;
  String? get statusMessage => _statusMessage;
  bool get isSuccess => _isSuccess;

  void setEmail(String value) {
    _email = value;
    notifyListeners();
  }

  void _setLoading(bool value) {
    _isLoading = value;
    notifyListeners();
  }

  Future<void> sendResetCode() async {
    if (_email.isEmpty) return;
    _setLoading(true);
    _statusMessage = null;

    // Call your Flask API backend service
    final success = await _apiService.requestPasswordResetOTP(_email);

    if (success) {
      _isSuccess = true;
      _statusMessage = 'An OTP verification code has been sent to $_email';
    } else {
      _isSuccess = false;
      _statusMessage =
          'Failed to send OTP. Please check your connection or email';
    }

    _setLoading(false);
  }

  void reset() {
    _email = '';
    _statusMessage = null;
    _isSuccess = false;
    notifyListeners();
  }
}
