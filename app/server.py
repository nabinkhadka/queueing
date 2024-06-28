from flask import Flask
from long_task import complex_function

from connection_settings import queue

app = Flask(__name__)


@app.route("/")
def index():
    argument_to_function = 5
    # Queue a long task
    queue.enqueue(complex_function, argument_to_function)
    # get list of jobs that are completed
    job_ids = queue.finished_job_registry.get_job_ids()
    # get list of jobs that are failed
    failed_job_ids = queue.failed_job_registry.get_job_ids()
    return {
        "finished": len(job_ids),
        "queued": len(queue.get_jobs()),
        "failed": len(failed_job_ids),
    }


app.run(debug=True, host="0.0.0.0", port=5007)
