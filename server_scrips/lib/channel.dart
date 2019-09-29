import 'package:insta_app/controllers/accept_requests_controller.dart';
import 'package:insta_app/controllers/otp_controller.dart';
import 'package:insta_app/controllers/request_count_value_controller.dart';
import 'package:insta_app/controllers/signin_controller_simple.dart';
import 'package:insta_app/controllers/signin_controller_complex.dart';

import 'insta_app.dart';

class InstaAppChannel extends ApplicationChannel {

  @override
  Future prepare() async {
    logger.onRecord.listen((rec) => print("$rec ${rec.error ?? ""} ${rec.stackTrace ?? ""}"));
  }

  @override
  Controller get entryPoint {
    final router = Router();

    // Prefer to use `link` instead of `linkFunction`.
    // See: https://aqueduct.io/docs/http/request_controller/
    router
      .route("/signinsimple")
      .link(() => SigninControllerSimple());

    router
      .route("/signincomplex")
      .link(() => SigninControllerComplex());

    router.route('/submitotp').link(() => OTPController());

    router.route('/togglescript').link(()=> AcceptRequestsController());

    router.route('/usercount').link(() => CountController());

    return router;
  }
}