def hello_world(request):
    request_json = request.get_json()
    if "batata" in request_json["data"]:
        return "ok", 201
    return "Bad request - Not batata", 400
