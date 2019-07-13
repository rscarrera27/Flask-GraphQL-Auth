import json


def request(test_cli, type, call, body):
    query = type + " {" + call + "{" + body + "}" + "}"

    response = test_cli.post(
        "/graphql", data=json.dumps({"query": query}), content_type="application/json"
    )

    return response.json["data"]
