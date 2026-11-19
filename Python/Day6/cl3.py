
def task_status():

    status = "pending"

    def update_status():
        nonlocal status
        status = "completed"

    update_status()

    print("Final status:", status)


task_status()
