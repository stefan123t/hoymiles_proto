from google.protobuf.message import Message as _ProtobufMessage
from .cloud import Cloud
from .app import App

def build_packet_raw(msg_type: int, seq: int, encoded_dto: bytes) -> bytes: ...
def parse_packet_raw(packet: bytes) -> tuple[int, int, str]: ...
def msg_from_packet(packet: bytes) -> BaseMessage: ...

def int_time() -> int: ...
def ymd_hms() -> str: ...
def hmcrc(data: bytes) -> int: ...

class BaseMessage(_ProtobufMessage):
  msg_type : int
  def __init__(self) -> None:
    self.seq : int
  def ToPacket(self) -> bytes: ...

class ReqMessage(BaseMessage): ...
class ResMessage(BaseMessage): ...
