table = {   #dict안에 dict
    "SLEEP" : {"HIT":"WAKE"},
    "WAKE":{"TIMER10":"SLEEP"}
}

cur_state =  "SLEEP"
next_state = table[cur_state]["HIT"]
print(next_state)