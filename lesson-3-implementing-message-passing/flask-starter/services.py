import sys

# Running 'flask run'
if "run" in sys.argv:
    from .enums import Status
else: # Running 'python app.py'
    from enums import Status

id = 3
orders = [
        {
            "id": "1",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:31:10.969696",
            "created_by": "USER14",
            "equipment": [
                "KEYBOARD", "MOUSE"
            ]
        },
        {
            "id": "2",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:29:10.969696",
            "created_by": "USER15",
            "equipment": [
                "KEYBOARD", "WEBCAM"
            ]
        }
    ]


def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """

    global id 
    order_data["id"] = id
    order_data["status"] = Status.Queued.value
    orders.append(order_data)

    id += 1

    msg = "order in the system"
    return msg 


def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't actually do anything.
    """
    return orders