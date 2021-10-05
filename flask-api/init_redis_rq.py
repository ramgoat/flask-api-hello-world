from flask_rq2 import RQ

rq = RQ()
'''
def create_workers():
    default_worker = rq.get_worker()
    default_worker.work(burst=True)
'''