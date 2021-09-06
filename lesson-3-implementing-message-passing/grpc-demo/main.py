import time
from concurrent import futures

import grpc
import item_pb2
import item_pb2_grpc
import item2_pb2
import item2_pb2_grpc

## For item.proto
# class ItemServicer(item_pb2_grpc.ItemServiceServicer):
#     def Create(self, request, context):

#         request_value = {
#             "name": request.name,
#             "brand_name": request.brand_name,
#             "id": int(request.id),
#             "weight": request.weight,
#         }
#         print(request_value)

#         return item_pb2.ItemMessage(**request_value)


# # Initialize gRPC server
# server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
# item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)

## For item2.proto
class ItemServicer(item2_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):

        request_value = {
            "name": request.name,
            "brand_name": request.brand_name,
            "id": int(request.id),
            "weight": request.weight,
        }
        print(request_value)

        return item_pb2.ItemMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)