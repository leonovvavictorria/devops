from flask import Flask, abort, request


def divide(a, b):
    if b == 0:
        return 'Нельзя делить на ноль'
    return a/b


main = Flask(__name__)


@main.route('/', methods=["GET"])
def get_tasks():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = None

    if b == 0:
        res = 'Нельзя делить на ноль'
    elif a and b:
        res = divide(a, b)

    if res is None:
        abort(422, "Unprocessable Entity")
    return {'res': res}


if __name__ == '__main__':
    main.run(host="127.0.0.1", port=5000)
