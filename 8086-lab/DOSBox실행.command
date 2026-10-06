#!/bin/bash
open -n -a "DOSBox Staging" --args -conf "$(cd "$(dirname "$0")" && pwd)/dosbox-8086.conf"
