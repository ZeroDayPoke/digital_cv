bind = '0.0.0.0:8000'
workers = 4
threads = 2
worker_class = 'sync'
preload_app = True
max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 30
accesslog = '-'
errorlog = '-'
