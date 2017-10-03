def generate_tweet_options(form):
    options = {"tweet_id": _parse_tweet_id(form["tweet_id"])}
    if "users" not in form:
        options["trim_user"] = "true"
    if "entities" not in form:
        options["include_entities"] = "false"

    return options

def _parse_tweet_id(given):
    return given.rsplit("/", 1)[-1].strip()
