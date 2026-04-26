from datetime import datetime

# start_time = time.perf_counter()
start_time = datetime.now()
for i in range(3000):
    # for j in range(1000):
        print("x")

# end_time = time.perf_counter()
end_time = datetime.now()
print("total time:", end_time - start_time)
