import 'package:aqueduct/aqueduct.dart';
import 'dart:io';
import 'dart:convert';

class OTPController extends ResourceController {
  @Operation.post()
  Future<Response> handleOTP() async {
    final Map<String, dynamic> map = await request.body.decode<
        Map<String, dynamic>>();
    final uname = map['username'];
    final otp = map['otp'];
    String resultString;

    final String fileName = './profiles/${uname}/${uname}_otp.txt';
    await File(fileName).writeAsString(otp.toString());

    return Response.ok({'valid': 'true'});
  }
}