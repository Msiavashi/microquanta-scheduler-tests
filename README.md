# Micro-Quanta Scheduler

Micro-Quanta is a linux scheduler for latency sensitive tasks available as a patch for kernel v5.3.

This repository holds my experimets comapring MQ and CFS.

Memcache perf is used for memcached evaluation.

## 1. Memcached tests

Command:

`$ mcperf -s localhost --scan=10:1000000:100000 -t 1 -c 8 -T 24`


### 1.1 MQ

    MQ config:
        - runtime: 40000 ns
        - period: 50000 ns



[Result](./test1.txt)


### 1.2 MQ
    MQ config:
        - runtime: 20000 ns
        - period: 40000 ns


[Result](./test2.txt)

### 1.3 CFS 

Default ubuntu config.

[Result](./test3.txt)

## 2. HTTP echo server tests

## 2.1 Isolated

Isonaled HTTP server running on docker. The echo server was the only application running.
HTTP echo server: hashicorp/http-echo 

### 2.1.1 MQ

    MQ config:
        - runtime: 20000 ns
        - period: 40000 ns

[Result](./http-echo/normal-p4r2)


### 2.1.2 MQ

    MQ config:
        - runtime: 40000 ns
        - period: 50000 ns

[Result](./http-echo/normal-p5r2)

### 2.1.3 CFS

Default config.

[Result](./http-echo/normal-cfs)

### 2.1.4 
Blue: MQ with period: 40us & runtime: 20us

Green: CFS

Orange: MQ with period: 50us & runtime: 40us

![Result](./http-echo/normal.png)

## 2.2 Colocation

`stress-ng` was running in the backroug as antigonistic app. 
No affinity was set.


### 2.2.1 MQ

    MQ config:
        - runtime: 20000 ns
        - period: 40000 ns

[Result](./http-echo/stress-p4r2)


### 2.2.2 MQ

    MQ config:
        - runtime: 40000 ns
        - period: 50000 ns

[Result](./http-echo/stress-p5r2)


### 2.2.3 CFS

Default config.

[Result](./http-echo/normal-cfs)


### 2.2.4 
Blue: MQ with period: 40us & runtime: 20us
Green: CFS
Orange: MQ with period: 50us & runtime: 40us
![Result](./http-echo/stress.png)