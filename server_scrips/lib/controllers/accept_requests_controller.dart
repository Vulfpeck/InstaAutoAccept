import 'dart:async';
import 'dart:io';
import 'package:aqueduct/aqueduct.dart';

class AcceptRequestsController extends ResourceController {
  @Operation.post()
  Future<Response> toggleAccept() async {
    final Map<String, dynamic> map = await request.body.decode<Map<String, dynamic>>();
    final uname = map['username'].toString();
    final scriptmode = map['mode'].toString();

    await File('./profiles/${uname}/${uname}_status.txt').writeAsString(scriptmode);

    await Process.start('python3', ['proxy_accept.py', uname, scriptmode]);
    return Response.ok({'mode': scriptmode});
  }
}