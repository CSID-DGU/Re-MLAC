from fastapi import HTTPException
from app.core.config import DataFrameSingleton
from app.utils import category_label
import pandas as pd
import requests
import os

from app.utils.custom_logger import CustomLogger

dataframe_singleton = DataFrameSingleton()
dataframe_body_singleton = DataFrameSingleton()
logger = CustomLogger()


def read_csv_file(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {str(e)}")


def initialize_dataframe(file_path: str, body_path: str):
    dataframe_singleton.data = read_csv_file(file_path)
    dataframe_body_singleton.data = read_csv_file(body_path)


def post_data_async(url: str, data: dict):
    try:
        response = requests.post(url, json=data)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending POST request: {str(e)}")


def post_data():
    dataframe = dataframe_singleton.data
    dataframe_body = dataframe_body_singleton.data

    if dataframe is None:
        raise HTTPException(status_code=500, detail="CSV file not loaded")

    if dataframe_body is None:
        raise HTTPException(status_code=500, detail="CSV file not loaded")

    random_row = dataframe.sample(n=1)

    ip = random_row.iloc[0]['srcip']
    port = random_row.iloc[0]['sport'].astype(str)
    index = int(random_row.iloc[0]['category_label'])
    label = category_label[index]
    body = dataframe_body[label].sample(n=1)
    body_json = body.to_json(orient='records')
    random_row.drop(columns=['srcip', 'sport', "category_label"], inplace=True)

    url = os.getenv("POST_URL")

    if not url:
        raise HTTPException(status_code=500, detail="POST URL not configured")

    response_data = post_data_async(url, {
        "ip": ip,
        "port": port,
        "body": body_json,
        "packet_info": {
            "dur": float(random_row.iloc[0]['dur']),
            "sbytes": float(random_row.iloc[0]['sbytes']),
            "dbytes": float(random_row.iloc[0]['dbytes']),
            "sttl": float(random_row.iloc[0]['sttl']),
            "dttl": float(random_row.iloc[0]['dttl']),
            "sloss": float(random_row.iloc[0]['sloss']),
            "dloss": float(random_row.iloc[0]['dloss']),
            "sload": float(random_row.iloc[0]['sload']),
            "dload": float(random_row.iloc[0]['dload']),
            "spkts": float(random_row.iloc[0]['spkts']),
            "dpkts": float(random_row.iloc[0]['dpkts']),
            "swin": float(random_row.iloc[0]['swin']),
            "dwin": float(random_row.iloc[0]['dwin']),
            "stcpb": float(random_row.iloc[0]['stcpb']),
            "dtcpb": float(random_row.iloc[0]['dtcpb']),
            "smeansz": float(random_row.iloc[0]['smeansz']),
            "dmeansz": float(random_row.iloc[0]['dmeansz']),
            "trans_depth": float(random_row.iloc[0]['trans_depth']),
            "res_bdy_len": float(random_row.iloc[0]['res_bdy_len']),
            "sjit": float(random_row.iloc[0]['sjit']),
            "djit": float(random_row.iloc[0]['djit']),
            "sintpkt": float(random_row.iloc[0]['sintpkt']),
            "dintpkt": float(random_row.iloc[0]['dintpkt']),
            "tcprtt": float(random_row.iloc[0]['tcprtt']),
            "synack": float(random_row.iloc[0]['synack']),
            "ackdat": float(random_row.iloc[0]['ackdat']),
            "is_sm_ips_ports": int(random_row.iloc[0]['is_sm_ips_ports']),
            "ct_state_ttl": int(random_row.iloc[0]['ct_state_ttl']),
            "ct_flw_http_mthd": int(random_row.iloc[0]['ct_flw_http_mthd']),
            "is_ftp_login": int(random_row.iloc[0]['is_ftp_login']),
            "ct_ftp_cmd": int(random_row.iloc[0]['ct_ftp_cmd']),
            "proto_3pc": int(random_row.iloc[0]['proto_3pc']),
            "proto_a/n": int(random_row.iloc[0]['proto_a/n']),
            "proto_aes-sp3-d": int(random_row.iloc[0]['proto_aes-sp3-d']),
            "proto_any": int(random_row.iloc[0]['proto_any']),
            "proto_argus": int(random_row.iloc[0]['proto_argus']),
            "proto_aris": int(random_row.iloc[0]['proto_aris']),
            "proto_arp": int(random_row.iloc[0]['proto_arp']),
            "proto_ax.25": int(random_row.iloc[0]['proto_ax.25']),
            "proto_bbn-rcc": int(random_row.iloc[0]['proto_bbn-rcc']),
            "proto_bna": int(random_row.iloc[0]['proto_bna']),
            "proto_br-sat-mon": int(random_row.iloc[0]['proto_br-sat-mon']),
            "proto_cbt": int(random_row.iloc[0]['proto_cbt']),
            "proto_cftp": int(random_row.iloc[0]['proto_cftp']),
            "proto_chaos": int(random_row.iloc[0]['proto_chaos']),
            "proto_compaq-peer": int(random_row.iloc[0]['proto_compaq-peer']),
            "proto_cphb": int(random_row.iloc[0]['proto_cphb']),
            "proto_cpnx": int(random_row.iloc[0]['proto_cpnx']),
            "proto_crtp": int(random_row.iloc[0]['proto_crtp']),
            "proto_crudp": int(random_row.iloc[0]['proto_crudp']),
            "proto_dcn": int(random_row.iloc[0]['proto_dcn']),
            "proto_ddp": int(random_row.iloc[0]['proto_ddp']),
            "proto_ddx": int(random_row.iloc[0]['proto_ddx']),
            "proto_dgp": int(random_row.iloc[0]['proto_dgp']),
            "proto_egp": int(random_row.iloc[0]['proto_egp']),
            "proto_eigrp": int(random_row.iloc[0]['proto_eigrp']),
            "proto_emcon": int(random_row.iloc[0]['proto_emcon']),
            "proto_encap": int(random_row.iloc[0]['proto_encap']),
            "proto_esp": int(random_row.iloc[0]['proto_esp']),
            "proto_etherip": int(random_row.iloc[0]['proto_etherip']),
            "proto_fc": int(random_row.iloc[0]['proto_fc']),
            "proto_fire": int(random_row.iloc[0]['proto_fire']),
            "proto_ggp": int(random_row.iloc[0]['proto_ggp']),
            "proto_gmtp": int(random_row.iloc[0]['proto_gmtp']),
            "proto_gre": int(random_row.iloc[0]['proto_gre']),
            "proto_hmp": int(random_row.iloc[0]['proto_hmp']),
            "proto_i-nlsp": int(random_row.iloc[0]['proto_i-nlsp']),
            "proto_iatp": int(random_row.iloc[0]['proto_iatp']),
            "proto_ib": int(random_row.iloc[0]['proto_ib']),
            "proto_icmp": int(random_row.iloc[0]['proto_icmp']),
            "proto_idpr": int(random_row.iloc[0]['proto_idpr']),
            "proto_idpr-cmtp": int(random_row.iloc[0]['proto_idpr-cmtp']),
            "proto_idrp": int(random_row.iloc[0]['proto_idrp']),
            "proto_ifmp": int(random_row.iloc[0]['proto_ifmp']),
            "proto_igmp": int(random_row.iloc[0]['proto_igmp']),
            "proto_igp": int(random_row.iloc[0]['proto_igp']),
            "proto_il": int(random_row.iloc[0]['proto_il']),
            "proto_ip": int(random_row.iloc[0]['proto_ip']),
            "proto_ipcomp": int(random_row.iloc[0]['proto_ipcomp']),
            "proto_ipcv": int(random_row.iloc[0]['proto_ipcv']),
            "proto_ipip": int(random_row.iloc[0]['proto_ipip']),
            "proto_iplt": int(random_row.iloc[0]['proto_iplt']),
            "proto_ipnip": int(random_row.iloc[0]['proto_ipnip']),
            "proto_ippc": int(random_row.iloc[0]['proto_ippc']),
            "proto_ipv6": int(random_row.iloc[0]['proto_ipv6']),
            "proto_ipv6-frag": int(random_row.iloc[0]['proto_ipv6-frag']),
            "proto_ipv6-icmp": int(random_row.iloc[0]['proto_ipv6-icmp']),
            "proto_ipv6-no": int(random_row.iloc[0]['proto_ipv6-no']),
            "proto_ipv6-opts": int(random_row.iloc[0]['proto_ipv6-opts']),
            "proto_ipv6-route": int(random_row.iloc[0]['proto_ipv6-route']),
            "proto_ipx-n-ip": int(random_row.iloc[0]['proto_ipx-n-ip']),
            "proto_irtp": int(random_row.iloc[0]['proto_irtp']),
            "proto_isis": int(random_row.iloc[0]['proto_isis']),
            "proto_iso-ip": int(random_row.iloc[0]['proto_iso-ip']),
            "proto_iso-tp4": int(random_row.iloc[0]['proto_iso-tp4']),
            "proto_kryptolan": int(random_row.iloc[0]['proto_kryptolan']),
            "proto_l2tp": int(random_row.iloc[0]['proto_l2tp']),
            "proto_larp": int(random_row.iloc[0]['proto_larp']),
            "proto_leaf-1": int(random_row.iloc[0]['proto_leaf-1']),
            "proto_leaf-2": int(random_row.iloc[0]['proto_leaf-2']),
            "proto_llc": int(random_row.iloc[0]['proto_llc']),
            "proto_lldp": int(random_row.iloc[0]['proto_lldp']),
            "proto_merit-inp": random_row.iloc[0]['proto_merit-inp'],
            "proto_mhrp": int(random_row.iloc[0]['proto_mhrp']),
            "proto_micp": int(random_row.iloc[0]['proto_micp']),
            "proto_mobile": int(random_row.iloc[0]['proto_mobile']),
            "proto_mtp": int(random_row.iloc[0]['proto_mtp']),
            "proto_mux": int(random_row.iloc[0]['proto_mux']),
            "proto_narp": int(random_row.iloc[0]['proto_narp']),
            "proto_netblt": int(random_row.iloc[0]['proto_netblt']),
            "proto_nsfnet-igp": int(random_row.iloc[0]['proto_nsfnet-igp']),
            "proto_nvp": int(random_row.iloc[0]['proto_nvp']),
            "proto_ospf": int(random_row.iloc[0]['proto_ospf']),
            "proto_pgm": int(random_row.iloc[0]['proto_pgm']),
            "proto_pim": int(random_row.iloc[0]['proto_pim']),
            "proto_pipe": int(random_row.iloc[0]['proto_pipe']),
            "proto_pnni": int(random_row.iloc[0]['proto_pnni']),
            "proto_pri-enc": int(random_row.iloc[0]['proto_pri-enc']),
            "proto_prm": int(random_row.iloc[0]['proto_prm']),
            "proto_ptp": int(random_row.iloc[0]['proto_ptp']),
            "proto_pup": int(random_row.iloc[0]['proto_pup']),
            "proto_pvp": int(random_row.iloc[0]['proto_pvp']),
            "proto_qnx": int(random_row.iloc[0]['proto_qnx']),
            "proto_rdp": int(random_row.iloc[0]['proto_rdp']),
            "proto_rsvp": int(random_row.iloc[0]['proto_rsvp']),
            "proto_rtcp": int(random_row.iloc[0]['proto_rtcp']),
            "proto_rtp": int(random_row.iloc[0]['proto_rtp']),
            "proto_rvd": int(random_row.iloc[0]['proto_rvd']),
            "proto_sat-expak": int(random_row.iloc[0]["proto_sat-expak"]),
            "proto_sat-mon": int(random_row.iloc[0]["proto_sat-mon"]),
            "proto_sccopmce": int(random_row.iloc[0]["proto_sccopmce"]),
            "proto_scps": int(random_row.iloc[0]["proto_scps"]),
            "proto_sctp": int(random_row.iloc[0]["proto_sctp"]),
            "proto_sdrp": int(random_row.iloc[0]["proto_sdrp"]),
            "proto_secure-vmtp": int(random_row.iloc[0]["proto_secure-vmtp"]),
            "proto_sep": int(random_row.iloc[0]["proto_sep"]),
            "proto_skip": int(random_row.iloc[0]["proto_skip"]),
            "proto_sm": int(random_row.iloc[0]["proto_sm"]),
            "proto_smp": int(random_row.iloc[0]["proto_smp"]),
            "proto_snp": int(random_row.iloc[0]["proto_snp"]),
            "proto_sprite-rpc": int(random_row.iloc[0]["proto_sprite-rpc"]),
            "proto_sps": int(random_row.iloc[0]["proto_sps"]),
            "proto_srp": int(random_row.iloc[0]["proto_srp"]),
            "proto_st2": int(random_row.iloc[0]["proto_st2"]),
            "proto_stp": int(random_row.iloc[0]["proto_stp"]),
            "proto_sun-nd": int(random_row.iloc[0]["proto_sun-nd"]),
            "proto_swipe": int(random_row.iloc[0]["proto_swipe"]),
            "proto_tcf": int(random_row.iloc[0]["proto_tcf"]),
            "proto_tcp": int(random_row.iloc[0]["proto_tcp"]),
            "proto_tlsp": int(random_row.iloc[0]["proto_tlsp"]),
            "proto_tp++": int(random_row.iloc[0]["proto_tp++"]),
            "proto_trunk-1": int(random_row.iloc[0]["proto_trunk-1"]),
            "proto_trunk-2": int(random_row.iloc[0]["proto_trunk-2"]),
            "proto_ttp": int(random_row.iloc[0]["proto_ttp"]),
            "proto_udp": int(random_row.iloc[0]["proto_udp"]),
            "proto_udt": int(random_row.iloc[0]["proto_udt"]),
            "proto_unas": int(random_row.iloc[0]["proto_unas"]),
            "proto_uti": int(random_row.iloc[0]["proto_uti"]),
            "proto_vines": int(random_row.iloc[0]["proto_vines"]),
            "proto_visa": int(random_row.iloc[0]["proto_visa"]),
            "proto_vmtp": int(random_row.iloc[0]["proto_vmtp"]),
            "proto_vrrp": int(random_row.iloc[0]["proto_vrrp"]),
            "proto_wb-expak": int(random_row.iloc[0]["proto_wb-expak"]),
            "proto_wb-mon": int(random_row.iloc[0]["proto_wb-mon"]),
            "proto_wsn": int(random_row.iloc[0]["proto_wsn"]),
            "proto_xnet": int(random_row.iloc[0]["proto_xnet"]),
            "proto_xns-idp": int(random_row.iloc[0]["proto_xns-idp"]),
            "proto_xtp": int(random_row.iloc[0]["proto_xtp"]),
            "proto_zero": int(random_row.iloc[0]["proto_zero"]),
            "state_ACC": int(random_row.iloc[0]["state_ACC"]),
            "state_CLO": int(random_row.iloc[0]["state_CLO"]),
            "state_CON": int(random_row.iloc[0]["state_CON"]),
            "state_ECO": int(random_row.iloc[0]["state_ECO"]),
            "state_ECR": int(random_row.iloc[0]["state_ECR"]),
            "state_FIN": int(random_row.iloc[0]["state_FIN"]),
            "state_INT": int(random_row.iloc[0]["state_INT"]),
            "state_MAS": int(random_row.iloc[0]["state_MAS"]),
            "state_MHR": int(random_row.iloc[0]["state_MHR"]),
            "state_NNS": int(random_row.iloc[0]["state_NNS"]),
            "state_NRS": int(random_row.iloc[0]["state_NRS"]),
            "state_PAR": int(random_row.iloc[0]["state_PAR"]),
            "state_REQ": int(random_row.iloc[0]["state_REQ"]),
            "state_RSP": int(random_row.iloc[0]["state_RSP"]),
            "state_RST": int(random_row.iloc[0]["state_RST"]),
            "state_TST": int(random_row.iloc[0]["state_TST"]),
            "state_TXD": int(random_row.iloc[0]["state_TXD"]),
            "state_URF": int(random_row.iloc[0]["state_URF"]),
            "state_URFIL": int(random_row.iloc[0]["state_URFIL"]),
            "state_URH": int(random_row.iloc[0]["state_URH"]),
            "state_URHPRO": int(random_row.iloc[0]["state_URHPRO"]),
            "state_URN": int(random_row.iloc[0]["state_URN"]),
            "state_URP": int(random_row.iloc[0]["state_URP"]),
            "state_no": int(random_row.iloc[0]["state_no"]),
            "service_-": int(random_row.iloc[0]["service_-"]),
            "service_0": int(random_row.iloc[0]["service_0"]),
            "service_dhcp": int(random_row.iloc[0]["service_dhcp"]),
            "service_dns": int(random_row.iloc[0]["service_dns"]),
            "service_ftp": int(random_row.iloc[0]["service_ftp"]),
            "service_ftp-data": int(random_row.iloc[0]["service_ftp-data"]),
            "service_http": int(random_row.iloc[0]["service_http"]),
            "service_irc": int(random_row.iloc[0]["service_irc"]),
            "service_pop3": int(random_row.iloc[0]["service_pop3"]),
            "service_radius": int(random_row.iloc[0]["service_radius"]),
            "service_smtp": int(random_row.iloc[0]["service_smtp"]),
            "service_snmp": int(random_row.iloc[0]["service_snmp"]),
            "service_ssh": int(random_row.iloc[0]["service_ssh"]),
            "service_ssl": int(random_row.iloc[0]["service_ssl"])
        }
    })

    return response_data
