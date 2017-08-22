def generate_tweet_options(form):
    options = {"tweet_id": form["tweet_id"]}
    if "users" not in form:
        options["trim_user"] = "true"
    if "entities" not in form:
        options["include_entities"] = "false"

    return options
