# Micro-Quanta Scheduler

Micro-Quanta is a linux scheduler for latency sensitive tasks available as a patch for kernel v5.3.

This repository holds my experimets comapring MQ and CFS.

Memcache perf is used for memcached evaluation.

## 1. Micro-Quanta results

Command:

`$ mcperf -s localhost --scan=10:1000000:100000 -t 1 -c 8 -T 24`


### 1.1

    MQ config:
        - runtime: 40000 ns
        - period: 50000 ns



[Result](./test1.txt)


### 1.2
    MQ config:
        - runtime: 20000 ns
        - period: 40000 ns


[Result](./test2.txt)

## 2. CFS results

Default ubuntu config.

[Result](./test3.txt)