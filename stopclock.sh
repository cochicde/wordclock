#!/bin/bash
 echo $$

for id in $(ps -aux | grep wordcl | tr -s " " | cut -f2 -d " "); do
 if [ "$$" -eq "$id" ]; then
   continue
  fi

 echo $id
  sudo kill  ${id}
done

ps -aux | grep wordcl
