from multiprocessing import Process
import hashlib
import time

def lambda_worker(runtime=60):
    end = time.time() + runtime
    nonce = 0

    while time.time() < end:
        hashlib.sha256(str(nonce).encode()).digest()
        nonce += 1

    print(f"Worker finished: {nonce:,} hashes")

if __name__ == "__main__":
    for i in range(10):  # simulate repeated Lambda invocations
        workers = []

        for _ in range(4):  # simulate concurrent executions
            p = Process(target=lambda_worker)
            p.start()
            workers.append(p)

        for p in workers:
            p.join()

        print(f"Batch {i+1} complete")
