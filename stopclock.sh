#!/bin/bash

for id in $(ps -aux | grep wordcl | tr -s " " | cut -f2 -d " "); do
  sudo kill  ${id}
done

ps -aux | grep wordcl
