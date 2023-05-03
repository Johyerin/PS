#달리기 경주(Lv.1)

def solution(players, callings):
    counting = {}

    for i in range(len(players)):
        counting[players[i]] = i

    for name in callings:
        counting[name] -= 1
        counting[players[counting[name]]] += 1
        players[counting[name]], players[counting[name] +  1] = players[counting[name] + 1], players[counting[name]]

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))