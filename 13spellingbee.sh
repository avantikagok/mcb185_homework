cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "^[crazion]+$" | grep -E "r" | grep -E "...." 