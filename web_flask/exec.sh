#!/usr/bin/bash

for file in *.py; do
	if [ -f "$file" ]; then
		if [ ! -x "$file" ]; then
			chmod +x "$file"
			echo "Made $file executable."
		else
			echo ""
		fi
	fi
done
