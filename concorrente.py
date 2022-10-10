import threading
import requests
import time
import random
url = "https://dummyjson.com/products/"

tempos = {1: [], 10: [], 50: [],
          100: [], 500: [], 750: [], 1000: []}


def req_d(i):
    response = requests.request("GET", url+str(random.randint(1, 100)))
    resp = response.json()
    print("Saida " + str(i) + ": " +
          str(resp['id']), end=", ")


cenarios = [1, 10, 50, 100, 500, 750, 1000]

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
            if (paradaReq == 100):
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
