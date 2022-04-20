from flask.helpers import make_response


def list(data_list):
    return make_response({
        "data": data_list
    }), 200
