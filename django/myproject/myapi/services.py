import docker

API_CLIENT_URL = "tcp://192.168.0.106:2375"
CONTAINER_NAME = "ubuntu"
NO_OF_CORES = 4.0

def calculate_cpu_percent(d):
    cpu_count = len(d["cpu_stats"]["cpu_usage"]["percpu_usage"])
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
  try:
   cpuPercent = calculate_cpu_percent(stat)
  except KeyError:
   continue
  return str(cpuPercent)
#modify_stats()

def client_info(): 
 client = docker.APIClient(base_url='tcp://192.168.0.106:2375')
 return client.version()

def create_containers():
 client = docker.APIClient(base_url='tcp://192.168.0.106:2375')
 container_id = client.create_container(IMAGE_NAME, detach=DETACH, tty=True, )
 print(container_id)
 all_containers = client.containers(all=True)
 print(all_containers)
#create_containers()

def delete_containers():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 container_id = client.remove_container(container=CONTAINER_NAME,v=True, force=True)
 print(container_id)
#delete_containers()


def rename_container():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 container_name = client.rename(container=CONTAINER_NAME, name="Alpine-Container")
 return container_name
#rename_container()

def container_stats():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 #stats = client.stats(container=CONTAINER_NAME, decode=False, stream=False)
 for stat in client.stats(container=CONTAINER_NAME, decode=True, stream=True):
  for k,v in stat.items():
   if k == 'read':
    return v
    #container_stats()

def start_container():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 start = client.start(container=CONTAINER_NAME)
#start_container()

def top_containers():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 top = client.top(container=CONTAINER_NAME)
 print(top)
#top_containers()

def update_containers():
 client = docker.APIClient(base_url=API_CLIENT_URL)
 update = client.update_container(container=CONTAINER_NAME, cpuset_cpus="0,1,2,3", mem_limit="4m")
#update_containers()

def list_containers():
  client = docker.APIClient(base_url=API_CLIENT_URL)
  all_containers = client.containers(all=True)
  return all_containers