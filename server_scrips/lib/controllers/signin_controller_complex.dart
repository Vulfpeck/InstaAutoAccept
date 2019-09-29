import 'package:aqueduct/aqueduct.dart' show Operation, ResourceController, Response;
import 'dart:io' show Process;

class SigninControllerComplex extends ResourceController {

  @Operation.post()
  Future<Response> signinUser() async {
    final Map<String, dynamic> map = await request.body.decode<Map<String, dynamic>>();
    final uname = map['username'];
    final pass = map['password'];
    String resultString;

    await Process.run('python3', ['login_complex.py', uname.toString(), pass.toString()]).then((result) {
      resultString = result.stdout.toString().split('\n')[0];
      print(result.stdout.toString());
    });

    if (resultString == 'done') {
      return Response.ok({'success': 'true'});
    } else if (resultString == 'error'){
      return Response.ok({'success': 'false'});
    } else {
      return Response.forbidden();
    }
  }
}
