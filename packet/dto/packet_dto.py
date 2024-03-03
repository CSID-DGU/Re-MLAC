class PacketRequestDto:
    def __init__(self, data):
        self.ip = data.get('ip')
        self.port = data.get('port')
        self.timestamp = data.get('timestamp')
        self.body = data.get('body')
        self.packet_info = data.get('packet_info')

class PacketResponseDto:
    def __init__(self, request_dto: PacketRequestDto, attack_type: str):
        self.ip = request_dto.ip
        self.port = request_dto.port
        self.timestamp = request_dto.timestamp
        self.body = request_dto.body
        self.attackType = attack_type
    
    def get_packet_info(self):
        return {
            'ip': self.ip,
            'port': self.port,
            'timestamp': self.timestamp,
            'body': self.body,
            'attack_type': self.attackType
        }