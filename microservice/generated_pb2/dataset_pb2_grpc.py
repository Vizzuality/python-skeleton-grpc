# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dataset_pb2 as dataset__pb2


class DatasetStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateDataset = channel.unary_unary(
        '/dataset.Dataset/CreateDataset',
        request_serializer=dataset__pb2.DatasetCreateRequest.SerializeToString,
        response_deserializer=dataset__pb2.DatasetReply.FromString,
        )
    self.GetDataset = channel.unary_unary(
        '/dataset.Dataset/GetDataset',
        request_serializer=dataset__pb2.DatasetGetRequest.SerializeToString,
        response_deserializer=dataset__pb2.DatasetReply.FromString,
        )


class DatasetServicer(object):

  def CreateDataset(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDataset(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatasetServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateDataset': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDataset,
          request_deserializer=dataset__pb2.DatasetCreateRequest.FromString,
          response_serializer=dataset__pb2.DatasetReply.SerializeToString,
      ),
      'GetDataset': grpc.unary_unary_rpc_method_handler(
          servicer.GetDataset,
          request_deserializer=dataset__pb2.DatasetGetRequest.FromString,
          response_serializer=dataset__pb2.DatasetReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dataset.Dataset', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))