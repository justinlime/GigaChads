#!/bin/bash
files="$(ls gigachads)"
printf '%s\n' "{
  \"gigachads\": [
    \"${files//$'\n'/$'",\n    "'}\"
  ]
}" > gigalist.json
