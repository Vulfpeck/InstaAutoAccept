import 'dart:async';
import 'dart:io';
import 'package:aqueduct/aqueduct.dart';

class CountController extends ResourceController {
  @Operation.get()
  Future<Response> getFollowCount() async {
    final Map<String, dynamic> map =
        await request.body.decode<Map<String, dynamic>>();
    
    final String username = map['username'].toString();
    final count = await File("./profiles/${username}/${username}_count.txt").readAsString();

    return Response.ok({"count": count});
  }
}
