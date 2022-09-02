#!/usr/bin/env bash
function run() {
    echo "[ { \"type\" : \"bad json\", \"file\" : \"$PWD/tool.sh\", \"line\": 1,\
              \"message\" : \"JSON is many things, but it is not this.\",\
              \"details_url\": null } ]"
    exit 0
}

[[ "$3" = "version" ]] && echo "1"
[[ "$3" = "applicable" ]] && echo "true"
[[ "$3" = "run" ]] && run
[[ -z "$3" ]] && echo '{ "version" : 1, "name" : "json-verifier" }'
