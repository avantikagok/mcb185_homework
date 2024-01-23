echo "Name: Avantika Gokulnatha"
echo "USER: $USER"

cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "^[muotfca]+$" | grep -E "a" | grep -E "...." 
gunzip -c dictionary.gz | grep -E "^[muotfca]+$" | grep -E "a" | grep -E "...."  | wc -l



#gunzip -c dictionary.gz | grep -E "^[tailnrb]+$" | grep -E "b" | grep -E "...." 
gunzip -c dictionary.gz | grep -E "^[tailnrb]+$" | grep -E "b" | grep -E "...."  | wc -l



#gunzip -c dictionary.gz | grep -E "^[maonidc]+$" | grep -E "c" | grep -E "...." 
gunzip -c dictionary.gz | grep -E "^[maonidc]+$" | grep -E "c" | grep -E "...."  | wc -l

#gunzip -c dictionary.gz | grep -E "^[anorgiz]+$" | grep -E "z" | grep -E "...." 
gunzip -c dictionary.gz | grep -E "^[anorgiz]+$" | grep -E "z" | grep -E "...."  | wc -l


cd ~/Code/MCB185/data
gunzip -c jaspar2024_core.transfac.gz | grep -E "tax" | wc -l "diatoms"



gunzip -c jaspar2024_core.transfac.gz | grep "tax" | cut -d ":" -f 2 | sort | uniq -c | sort -n
 
 
echo "Authors: Avantika, Varsha, Anisha, Francesca"