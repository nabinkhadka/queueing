from time import sleep

TIME_TO_SLEEP = 20


def complex_function(task_arg):
    print(f"\n\n***********\nWorker is executing a long running job for {TIME_TO_SLEEP} seconds...")
    sleep(TIME_TO_SLEEP)
    print(f"Worker finished a long running job\n***********\n\n")
    return f"prefix_{task_arg}"
