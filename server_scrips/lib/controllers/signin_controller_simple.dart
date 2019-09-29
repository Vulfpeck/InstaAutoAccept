import 'package:aqueduct/aqueduct.dart';
import 'dart:io';
import 'dart:convert';

class SigninControllerSimple extends ResourceController {
  @Operation.post()
  Future<Response> signinUser() async {
    final Map<String, dynamic> map =
        await request.body.decode<Map<String, dynamic>>();
    final uname = map['username'];
    final pass = map['password'];

    String resultString;
    await Process.run(
            'python3', ['login_simple.py', uname.toString(), pass.toString()])
        .then((result) {
      resultString = result.stdout.toString().split('\n')[0];
      print(resultString);
    });

    if (resultString == "error")
      return Response.ok({'success': 'false'});
    else
      return Response.ok({'success': 'true'});
  }
}
