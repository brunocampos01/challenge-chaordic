from time import time

data_split = []


        # get somente os últimos 10 min de requests
        for i in times_registered:

            last_10_min = minute - times_registered[-(len(times_registered))]
            if last_10_min < 10:
                data_split.append(datas_registered[:-i])
            else:
                break # garante que não vai percorrer requests mais velhas q 10 min 


        times_registered
