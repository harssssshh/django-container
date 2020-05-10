import docker

API_CLIENT_URL = "tcp://192.168.0.106:2375"
CONTAINER_NAME = "ubuntu"
NO_OF_CORES = 4.0

def calculateCPUPercentUnix(v):
    cpuPercent = 0.0
    previousCPU = v['precpu_stats']['cpu_usage']['total_usage']
    cpuDelta = v['cpu_stats']['cpu_usage']['total_usage'] - previousCPU
    previousSystem = v['precpu_stats']['system_cpu_usage']
    systemDelta = v['cpu_stats']['system_cpu_usage'] - previousSystem
    if systemDelta > 0.0 and cpuDelta > 0.0:
        cpuPercent = cpuDelta / systemDelta * 100 
        #cpuPercent = (cpuDelta / systemDelta) * len(v['cpu_stats']['cpu_usage']['percpu_usage']) * 100 
        return "{0:.2f}".format(cpuPercent)
    else:
        return cpuPercent

def calculate_cpu_percent(d):
    cpu_count = len(d["cpu_stats"]["cpu_usage"]["percpu_usage"])
    #print(cpu_count)
    cpu_percent = 0.0
    cpu_delta = float(d["cpu_stats"]["cpu_usage"]["total_usage"]) - \
                float(d["precpu_stats"]["cpu_usage"]["total_usage"])
    system_delta = float(d["cpu_stats"]["system_cpu_usage"]) - \
                   float(d["precpu_stats"]["system_cpu_usage"])
    online_cpus = d["cpu_stats"].get("online_cpus", len(d["cpu_stats"]["cpu_usage"]["percpu_usage"]))
    if system_delta > 0.0:
        cpu_percent = ((cpu_delta / system_delta) * online_cpus * 100.0) / NO_OF_CORES 
    return cpu_percent


def modify_stats():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 stats = client.stats(container=CONTAINER_NAME, decode=True, stream=True)
 for stat in stats:
  
  #print(stat['cpu_stats']['cpu_usage']['total_usage'])
  #print(stat['precpu_stats']['cpu_usage']['total_usage'])
  #print(stat['cpu_stats']['system_cpu_usage'])
  #print(stat['precpu_stats'])
  try:
   cpuPercent = calculate_cpu_percent(stat)
  except KeyError:
   continue
  print(cpuPercent)
modify_stats()
