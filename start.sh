#!/bin/sh

pip install discord
read -p "Token: " tk
python3 pingbot.py $tk
