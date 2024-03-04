from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .apps import PipelineFactory
from .dto.packet_dto import PacketRequestDto, PacketResponseDto

import logging

@csrf_exempt
def analysis_packet(request):
    request_dto = None
    
    try:
        data = JSONParser().parse(request)
        request_dto = PacketRequestDto(data=data)
    except:
        logging.error("Parsing Error")
        return JsonResponse({
            "success": False,
            "data": None,
            "error": {
                "code": 40400,
                "message": "not pasering"
                },
            },
                            status=400,
                            safe=False)
        
    pipeline = PipelineFactory.get_instance()
    attack_type = pipeline.run(request_dto.packet_info)
    
    return JsonResponse(
        PacketResponseDto(
            request_dto=request_dto,
            attack_type=attack_type
        ).get_packet_info(), safe=False)