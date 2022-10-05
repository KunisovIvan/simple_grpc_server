from concurrent import futures

import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def InteractingHello(self, request, context):
        print('request-> ', request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
