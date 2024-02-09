# 48report.md #

## Output of 45dndstats.py ##

3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll

| Roll Type| Average score |
| ---------| --------------|
| 3D6      | 10.5275       |
| 3D6r1    | 12.0068       |
| 3d6x2    | 17.8659       |
| 4D6d1    | 12.2499       |


## Output of 46savingthrows.py ##

DC = difficulty class (need to roll above the selected difficulty class number)
Advantage roll = roll two d20 dice, choose higher number 
Disadvantage roll = roll two d20 dice, choose lower number

|       |  Normal| Adv	  | Disadv |
|-------| -------| -------| -------|
| DC 5	| 0.7988 | 0.9598 | 0.627  |
| DC 10 | 0.5608 | 0.7974 |	0.2976 |
| DC 15 | 0.3156 | 0.511  | 0.0911 |
 

## Output of 47deathsaves.py ##

Roll less than 10 = "failure"
Roll 10 or greater = "success"
Roll 1 = 2 "failures"
Roll 20 = "revive" 
3 failures = "death"
3 successes = "stable"

| Status 	  | Probability |
| ------------| ------------|
| Death prob  | 0.4126      |
| Stable prob | 0.4079      | 
| Revive prob | 0.1795      |
