#!/bin/bash

set -euo pipefail

if ! [[ -f /usr/bin/podman ]]; then
  echo "podman is not available"
  exit 1
fi

podman build -t build_pdf:latest .

exit 0
