import os
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
periods_n = [5000, 10000, 20000, 50000, 100000, 250000, 500000,
             1000000, 5000000, 10000000, 25000000, 50000000, 100000000]
runtimes_n = [4000, 8000, 16000, 50000, 80000, 220000, 450000,
              800000, 4500000, 8000000, 21000000, 45000000, 80000000]

rates = [1000, 5000, 8000, 10000]
wrk2_dir = "/home/mohammad/Desktop/wrk2"
save_dir = "/home/mohammad/Desktop/results"
url = "http://localhost"


def set_runtime(ns):
    print("[+] Runtime set to: " + str(ns))
    os.system('sudo sysctl kernel.sched_microq_runtime_ns=' + str(ns))


def set_period(ns):
    print("[+] Period set to: " + str(ns))
    os.system('sudo sysctl kernel.sched_microq_period_ns=' + str(ns))


def exec_test(rps, connections, threads):
    print("[+] Executing test...")
    command = "sudo " + wrk2_dir + "/wrk --latency -R " + str(rps) + " -c " + str(connections) + " -t " + str(threads) + " " + url
    stream = os.popen(command)
    output = stream.read()
    print("[+] Test Done")
    return output


def save_result(result, path, filename):
    os.makedirs(path, exist_ok=True)
    with open(path + "/" + filename, 'w') as file:
        file.write(result)


def run(connections, threads):
    for rps in rates:
        for period in periods_n:
            set_period(period)
            for runtime in runtimes_n:
                set_runtime(runtime)
                result = exec_test(rps, connections, threads)
                filename = 'p%s-r%s' % (period//1000, runtime//1000)
                path = save_dir + "/" + str(rps)
                save_result(result, path, filename)


def get_latency(line):
    return line.split()[-1]


def find_string(lines, key_string):
    for line in lines:
        if key_string in line:
            return line


def get_content(file):
    with open(file) as f:
        return f.readlines()


def res_to_csv(dir, percentile, save_at="./out.csv"):
    files = [f for f in os.listdir(
        dir) if os.path.isfile(os.path.join(dir, f))]
    rows = np.array([str(x//1000) for x in periods_n])
    cols = np.array([str(x//1000) for x in runtimes_n])
    df = pd.DataFrame(index=rows,
                      columns=cols)
    for file in files:
        latency = float(get_latency(find_string(get_content(
            os.path.join(dir, file)), percentile))[:-2])
        period = file.split("-")[0][1:]
        runtime = file.split("-")[1][1:]
        df.loc[period, runtime] = latency
    df.to_csv(save_at)


def generate_heatmap(csv_file, threshold, threshold_replacement):
    df = pd.read_csv(csv_file, index_col=0)
    df.where(df <= threshold, threshold_replacement, inplace=True)
    sns.heatmap(df, annot=True)
    plt.show()

if __name__ == "__main__":
    threads = 2
    connections = 10
    rate = 5000
    save_path = os.path.join(save_dir, str(rate))
    # run(connections, threads)
    res_to_csv(save_path, "99.000%")
    generate_heatmap("./out.csv", 700, 20)

