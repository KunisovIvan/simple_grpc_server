import time

import greet_pb2_grpc
import greet_pb2
import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        while True:
            name = input('What is your name?: ')
            stub = greet_pb2_grpc.GreeterStub(channel)
            hello_request = greet_pb2.HelloRequest(greeting="Hello", name=name)
            response = stub.InteractingHello(hello_request)
            print('response-> ', response.message)
            time.sleep(1)


if __name__ == "__main__":
    run()
