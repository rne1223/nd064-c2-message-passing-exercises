import grpc
# import item_pb2
# import item_pb2_grpc
import item2_pb2
import item2_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
## For item.proto
# stub = item_pb2_grpc.ItemServiceStub(channel)

# # Update this with desired payload
# item = item_pb2.ItemMessage(
#     name="Non-Stick Frying Pan",
#     brand_name="Fruit Cup",
#     id=4,
#     weight=4.5
# )

## For item2.proto
stub = item2_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
item = item2_pb2.OrderMessage(
    id="RT",
    created_by="Fool",
    status=item2_pb2.OrderMessage.Status.QUEUED,
    created_at="10:00pm",
    equipment=[item2_pb2.OrderMessage.Equipment.MOUSE, item2_pb2.OrderMessage.Equipment.MONITOR]
)

response = stub.Create(item)