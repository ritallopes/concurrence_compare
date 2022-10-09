import threading
import random
import requests
import time
url = "https://roll-dice1.p.rapidapi.com/rollDice"

headers = {
    "X-RapidAPI-Key": "658fe435e7mshcba5a8d6ebae09bp1a20ccjsnd5e3ca64059a",
    "X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
}

tempos = {1: [], 10: [], 50: [],
          100: [], 500: [], 1000: [], 5000: []}


def req_d(i):
    response = requests.request("GET", url, headers=headers)
    resp = response.json()
    print("Saida " + str(i) + ": " +
          str(resp['data']['Dice']), end=", ")


cenarios = [1, 10, 50, 100, 500, 1000, 5000]

paradaReq = 0
tempoParada = 0

for cenario in cenarios:
    for e in range(20):
        inicio = time.time_ns()
        print("\nInício - cenário " + str(cenario) +
              ", execucao " + str(e), end="\n")
        threads = []
        for i in range(cenario):
            paradaReq += 1
            if (paradaReq == 200):
                ini = time.time_ns()
                time.sleep(60)
                paradaReq = 0
                f = time.time_ns()
                tempoParada += f - ini
            t = threading.Thread(target=req_d, args=(i,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()
        fim = time.time_ns()
        tempoGasto = fim - inicio - tempoParada
        tempoParada = 0
        tempos[cenario].append(tempoGasto)
    print("\nFim execucao "+str(tempos)+"\n")
    time.sleep(60)
print("\n\n"+str(tempos))
