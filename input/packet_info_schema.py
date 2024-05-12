from pydantic import BaseModel, Field
import pandas as pd


class PacketInfoSchema(BaseModel):
    dur: float = Field(None, alias="dur")
    sbytes: float = Field(None, alias="sbytes")
    dbytes: float = Field(None, alias="dbytes")
    sttl: float = Field(None, alias="sttl")
    dttl: float = Field(None, alias="dttl")
    sloss: float = Field(None, alias="sloss")
    dloss: float = Field(None, alias="dloss")
    sload: float = Field(None, alias="sload")
    dload: float = Field(None, alias="dload")
    spkts: float = Field(None, alias="spkts")
    dpkts: float = Field(None, alias="dpkts")
    swin: float = Field(None, alias="swin")
    dwin: float = Field(None, alias="dwin")
    stcpb: float = Field(None, alias="stcpb")
    dtcpb: float = Field(None, alias="dtcpb")
    smeansz: float = Field(None, alias="smeansz")
    dmeansz: float = Field(None, alias="dmeansz")
    trans_depth: float = Field(None, alias="trans_depth")
    res_bdy_len: float = Field(None, alias="res_bdy_len")
    sjit: float = Field(None, alias="sjit")
    djit: float = Field(None, alias="djit")
    sintpkt: float = Field(None, alias="sintpkt")
    dintpkt: float = Field(None, alias="dintpkt")
    tcprtt: float = Field(None, alias="tcprtt")
    synack: float = Field(None, alias="synack")
    ackdat: float = Field(None, alias="ackdat")
    is_sm_ips_ports: int = Field(None, alias="is_sm_ips_ports")
    ct_state_ttl: int = Field(None, alias="ct_state_ttl")
    ct_flw_http_mthd: int = Field(None, alias="ct_flw_http_mthd")
    is_ftp_login: int = Field(None, alias="is_ftp_login")
    ct_ftp_cmd: int = Field(None, alias="ct_ftp_cmd")
    proto_3pc: int = Field(None, alias="proto_3pc")
    proto_a_n: int = Field(None, alias="proto_a/n")
    proto_aes_sp3_d: int = Field(None, alias="proto_aes-sp3-d")
    proto_any: int = Field(None, alias="proto_any")
    proto_argus: int = Field(None, alias="proto_argus")
    proto_aris: int = Field(None, alias="proto_aris")
    proto_arp: int = Field(None, alias="proto_arp")
    proto_ax_25: int = Field(None, alias="proto_ax.25")
    proto_bbn_rcc: int = Field(None, alias="proto_bbn-rcc")
    proto_bna: int = Field(None, alias="proto_bna")
    proto_br_sat_mon: int = Field(None, alias="proto_br-sat-mon")
    proto_cbt: int = Field(None, alias="proto_cbt")
    proto_cftp: int = Field(None, alias="proto_cftp")
    proto_chaos: int = Field(None, alias="proto_chaos")
    proto_compaq_peer: int = Field(None, alias="proto_compaq-peer")
    proto_cphb: int = Field(None, alias="proto_cphb")
    proto_cpnx: int = Field(None, alias="proto_cpnx")
    proto_crtp: int = Field(None, alias="proto_crtp")
    proto_crudp: int = Field(None, alias="proto_crudp")
    proto_dcn: int = Field(None, alias="proto_dcn")
    proto_ddp: int = Field(None, alias="proto_ddp")
    proto_ddx: int = Field(None, alias="proto_ddx")
    proto_dgp: int = Field(None, alias="proto_dgp")
    proto_egp: int = Field(None, alias="proto_egp")
    proto_eigrp: int = Field(None, alias="proto_eigrp")
    proto_emcon: int = Field(None, alias="proto_emcon")
    proto_encap: int = Field(None, alias="proto_encap")
    proto_esp: int = Field(None, alias="proto_esp")
    proto_etherip: int = Field(None, alias="proto_etherip")
    proto_fc: int = Field(None, alias="proto_fc")
    proto_fire: int = Field(None, alias="proto_fire")
    proto_ggp: int = Field(None, alias="proto_ggp")
    proto_gmtp: int = Field(None, alias="proto_gmtp")
    proto_gre: int = Field(None, alias="proto_gre")
    proto_hmp: int = Field(None, alias="proto_hmp")
    proto_i_nlsp: int = Field(None, alias="proto_i-nlsp")
    proto_iatp: int = Field(None, alias="proto_iatp")
    proto_ib: int = Field(None, alias="proto_ib")
    proto_icmp: int = Field(None, alias="proto_icmp")
    proto_idpr: int = Field(None, alias="proto_idpr")
    proto_idpr_cmtp: int = Field(None, alias="proto_idpr-cmtp")
    proto_idrp: int = Field(None, alias="proto_idrp")
    proto_ifmp: int = Field(None, alias="proto_ifmp")
    proto_igmp: int = Field(None, alias="proto_igmp")
    proto_igp: int = Field(None, alias="proto_igp")
    proto_il: int = Field(None, alias="proto_il")
    proto_ip: int = Field(None, alias="proto_ip")
    proto_ipcomp: int = Field(None, alias="proto_ipcomp")
    proto_ipcv: int = Field(None, alias="proto_ipcv")
    proto_ipip: int = Field(None, alias="proto_ipip")
    proto_iplt: int = Field(None, alias="proto_iplt")
    proto_ipnip: int = Field(None, alias="proto_ipnip")
    proto_ippc: int = Field(None, alias="proto_ippc")
    proto_ipv6: int = Field(None, alias="proto_ipv6")
    proto_ipv6_frag: int = Field(None, alias="proto_ipv6-frag")
    proto_ipv6_icmp: int = Field(None, alias="proto_ipv6-icmp")
    proto_ipv6_no: int = Field(None, alias="proto_ipv6-no")
    proto_ipv6_opts: int = Field(None, alias="proto_ipv6-opts")
    proto_ipv6_route: int = Field(None, alias="proto_ipv6-route")
    proto_ipx_n_ip: int = Field(None, alias="proto_ipx-n-ip")
    proto_irtp: int = Field(None, alias="proto_irtp")
    proto_isis: int = Field(None, alias="proto_isis")
    proto_iso_ip: int = Field(None, alias="proto_iso-ip")
    proto_iso_tp4: int = Field(None, alias="proto_iso-tp4")
    proto_kryptolan: int = Field(None, alias="proto_kryptolan")
    proto_l2tp: int = Field(None, alias="proto_l2tp")
    proto_larp: int = Field(None, alias="proto_larp")
    proto_leaf_1: int = Field(None, alias="proto_leaf-1")
    proto_leaf_2: int = Field(None, alias="proto_leaf-2")
    proto_llc: int = Field(None, alias="proto_llc")
    proto_lldp: int = Field(None, alias="proto_lldp")
    proto_merit_inp: int = Field(None, alias="proto_merit-inp")
    proto_mfe_nsp: int = Field(None, alias="proto_mfe-nsp")
    proto_mhrp: int = Field(None, alias="proto_mhrp")
    proto_micp: int = Field(None, alias="proto_micp")
    proto_mobile: int = Field(None, alias="proto_mobile")
    proto_mtp: int = Field(None, alias="proto_mtp")
    proto_mux: int = Field(None, alias="proto_mux")
    proto_narp: int = Field(None, alias="proto_narp")
    proto_netblt: int = Field(None, alias="proto_netblt")
    proto_nsfnet_igp: int = Field(None, alias="proto_nsfnet-igp")
    proto_nvp: int = Field(None, alias="proto_nvp")
    proto_ospf: int = Field(None, alias="proto_ospf")
    proto_pgm: int = Field(None, alias="proto_pgm")
    proto_pim: int = Field(None, alias="proto_pim")
    proto_pipe: int = Field(None, alias="proto_pipe")
    proto_pnni: int = Field(None, alias="proto_pnni")
    proto_pri_enc: int = Field(None, alias="proto_pri-enc")
    proto_prm: int = Field(None, alias="proto_prm")
    proto_ptp: int = Field(None, alias="proto_ptp")
    proto_pup: int = Field(None, alias="proto_pup")
    proto_pvp: int = Field(None, alias="proto_pvp")
    proto_qnx: int = Field(None, alias="proto_qnx")
    proto_rdp: int = Field(None, alias="proto_rdp")
    proto_rsvp: int = Field(None, alias="proto_rsvp")
    proto_rtcp: int = Field(None, alias="proto_rtcp")
    proto_rtp: int = Field(None, alias="proto_rtp")
    proto_rvd: int = Field(None, alias="proto_rvd")
    proto_sat_expak: int = Field(None, alias="proto_sat-expak")
    proto_sat_mon: int = Field(None, alias="proto_sat-mon")
    proto_sccopmce: int = Field(None, alias="proto_sccopmce")
    proto_scps: int = Field(None, alias="proto_scps")
    proto_sctp: int = Field(None, alias="proto_sctp")
    proto_sdrp: int = Field(None, alias="proto_sdrp")
    proto_secure_vmtp: int = Field(None, alias="proto_secure-vmtp")
    proto_sep: int = Field(None, alias="proto_sep")
    proto_skip: int = Field(None, alias="proto_skip")
    proto_sm: int = Field(None, alias="proto_sm")
    proto_smp: int = Field(None, alias="proto_smp")
    proto_snp: int = Field(None, alias="proto_snp")
    proto_sprite_rpc: int = Field(None, alias="proto_sprite-rpc")
    proto_sps: int = Field(None, alias="proto_sps")
    proto_srp: int = Field(None, alias="proto_srp")
    proto_st2: int = Field(None, alias="proto_st2")
    proto_stp: int = Field(None, alias="proto_stp")
    proto_sun_nd: int = Field(None, alias="proto_sun-nd")
    proto_swipe: int = Field(None, alias="proto_swipe")
    proto_tcf: int = Field(None, alias="proto_tcf")
    proto_tcp: int = Field(None, alias="proto_tcp")
    proto_tlsp: int = Field(None, alias="proto_tlsp")
    proto_tp: int = Field(None, alias="proto_tp++")
    proto_trunk_1: int = Field(None, alias="proto_trunk-1")
    proto_trunk_2: int = Field(None, alias="proto_trunk-2")
    proto_ttp: int = Field(None, alias="proto_ttp")
    proto_udp: int = Field(None, alias="proto_udp")
    proto_udt: int = Field(None, alias="proto_udt")
    proto_unas: int = Field(None, alias="proto_unas")
    proto_uti: int = Field(None, alias="proto_uti")
    proto_vines: int = Field(None, alias="proto_vines")
    proto_visa: int = Field(None, alias="proto_visa")
    proto_vmtp: int = Field(None, alias="proto_vmtp")
    proto_vrrp: int = Field(None, alias="proto_vrrp")
    proto_wb_expak: int = Field(None, alias="proto_wb-expak")
    proto_wb_mon: int = Field(None, alias="proto_wb-mon")
    proto_wsn: int = Field(None, alias="proto_wsn")
    proto_xnet: int = Field(None, alias="proto_xnet")
    proto_xns_idp: int = Field(None, alias="proto_xns-idp")
    proto_xtp: int = Field(None, alias="proto_xtp")
    proto_zero: int = Field(None, alias="proto_zero")
    state_ACC: int = Field(None, alias="state_ACC")
    state_CLO: int = Field(None, alias="state_CLO")
    state_CON: int = Field(None, alias="state_CON")
    state_ECO: int = Field(None, alias="state_ECO")
    state_ECR: int = Field(None, alias="state_ECR")
    state_FIN: int = Field(None, alias="state_FIN")
    state_INT: int = Field(None, alias="state_INT")
    state_MAS: int = Field(None, alias="state_MAS")
    state_MHR: int = Field(None, alias="state_MHR")
    state_NNS: int = Field(None, alias="state_NNS")
    state_NRS: int = Field(None, alias="state_NRS")
    state_PAR: int = Field(None, alias="state_PAR")
    state_REQ: int = Field(None, alias="state_REQ")
    state_RSP: int = Field(None, alias="state_RSP")
    state_RST: int = Field(None, alias="state_RST")
    state_TST: int = Field(None, alias="state_TST")
    state_TXD: int = Field(None, alias="state_TXD")
    state_URF: int = Field(None, alias="state_URF")
    state_URFIL: int = Field(None, alias="state_URFIL")
    state_URH: int = Field(None, alias="state_URH")
    state_URHPRO: int = Field(None, alias="state_URHPRO")
    state_URN: int = Field(None, alias="state_URN")
    state_URP: int = Field(None, alias="state_URP")
    state_no: int = Field(None, alias="state_no")
    service_: int = Field(None, alias="service_-")
    service_0: int = Field(None, alias="service_0")
    service_dhcp: int = Field(None, alias="service_dhcp")
    service_dns: int = Field(None, alias="service_dns")
    service_ftp: int = Field(None, alias="service_ftp")
    service_ftp_data: int = Field(None, alias="service_ftp-data")
    service_http: int = Field(None, alias="service_http")
    service_irc: int = Field(None, alias="service_irc")
    service_pop3: int = Field(None, alias="service_pop3")
    service_radius: int = Field(None, alias="service_radius")
    service_smtp: int = Field(None, alias="service_smtp")
    service_snmp: int = Field(None, alias="service_snmp")
    service_ssh: int = Field(None, alias="service_ssh")
    service_ssl: int = Field(None, alias="service_ssl")

    @staticmethod
    def from_dataframe(row: pd.Series) -> dict:
        return {
            "dur": float(row['dur']),
            "sbytes": float(row['sbytes']),
            "dbytes": float(row['dbytes']),
            "sttl": float(row['sttl']),
            "dttl": float(row['dttl']),
            "sloss": float(row['sloss']),
            "dloss": float(row['dloss']),
            "sload": float(row['sload']),
            "dload": float(row['dload']),
            "spkts": float(row['spkts']),
            "dpkts": float(row['dpkts']),
            "swin": float(row['swin']),
            "dwin": float(row['dwin']),
            "stcpb": float(row['stcpb']),
            "dtcpb": float(row['dtcpb']),
            "smeansz": float(row['smeansz']),
            "dmeansz": float(row['dmeansz']),
            "trans_depth": float(row['trans_depth']),
            "res_bdy_len": float(row['res_bdy_len']),
            "sjit": float(row['sjit']),
            "djit": float(row['djit']),
            "sintpkt": float(row['sintpkt']),
            "dintpkt": float(row['dintpkt']),
            "tcprtt": float(row['tcprtt']),
            "synack": float(row['synack']),
            "ackdat": float(row['ackdat']),
            "is_sm_ips_ports": int(row['is_sm_ips_ports']),
            "ct_state_ttl": int(row['ct_state_ttl']),
            "ct_flw_http_mthd": int(row['ct_flw_http_mthd']),
            "is_ftp_login": int(row['is_ftp_login']),
            "ct_ftp_cmd": int(row['ct_ftp_cmd']),
            "proto_3pc": int(row['proto_3pc']),
            "proto_a/n": int(row['proto_a/n']),
            "proto_aes-sp3-d": int(row['proto_aes-sp3-d']),
            "proto_any": int(row['proto_any']),
            "proto_argus": int(row['proto_argus']),
            "proto_aris": int(row['proto_aris']),
            "proto_arp": int(row['proto_arp']),
            "proto_ax.25": int(row['proto_ax.25']),
            "proto_bbn-rcc": int(row['proto_bbn-rcc']),
            "proto_bna": int(row['proto_bna']),
            "proto_br-sat-mon": int(row['proto_br-sat-mon']),
            "proto_cbt": int(row['proto_cbt']),
            "proto_cftp": int(row['proto_cftp']),
            "proto_chaos": int(row['proto_chaos']),
            "proto_compaq-peer": int(row['proto_compaq-peer']),
            "proto_cphb": int(row['proto_cphb']),
            "proto_cpnx": int(row['proto_cpnx']),
            "proto_crtp": int(row['proto_crtp']),
            "proto_crudp": int(row['proto_crudp']),
            "proto_dcn": int(row['proto_dcn']),
            "proto_ddp": int(row['proto_ddp']),
            "proto_ddx": int(row['proto_ddx']),
            "proto_dgp": int(row['proto_dgp']),
            "proto_egp": int(row['proto_egp']),
            "proto_eigrp": int(row['proto_eigrp']),
            "proto_emcon": int(row['proto_emcon']),
            "proto_encap": int(row['proto_encap']),
            "proto_esp": int(row['proto_esp']),
            "proto_etherip": int(row['proto_etherip']),
            "proto_fc": int(row['proto_fc']),
            "proto_fire": int(row['proto_fire']),
            "proto_ggp": int(row['proto_ggp']),
            "proto_gmtp": int(row['proto_gmtp']),
            "proto_gre": int(row['proto_gre']),
            "proto_hmp": int(row['proto_hmp']),
            "proto_i-nlsp": int(row['proto_i-nlsp']),
            "proto_iatp": int(row['proto_iatp']),
            "proto_ib": int(row['proto_ib']),
            "proto_icmp": int(row['proto_icmp']),
            "proto_idpr": int(row['proto_idpr']),
            "proto_idpr-cmtp": int(row['proto_idpr-cmtp']),
            "proto_idrp": int(row['proto_idrp']),
            "proto_ifmp": int(row['proto_ifmp']),
            "proto_igmp": int(row['proto_igmp']),
            "proto_igp": int(row['proto_igp']),
            "proto_il": int(row['proto_il']),
            "proto_ip": int(row['proto_ip']),
            "proto_ipcomp": int(row['proto_ipcomp']),
            "proto_ipcv": int(row['proto_ipcv']),
            "proto_ipip": int(row['proto_ipip']),
            "proto_iplt": int(row['proto_iplt']),
            "proto_ipnip": int(row['proto_ipnip']),
            "proto_ippc": int(row['proto_ippc']),
            "proto_ipv6": int(row['proto_ipv6']),
            "proto_ipv6-frag": int(row['proto_ipv6-frag']),
            "proto_ipv6-icmp": int(row['proto_ipv6-icmp']),
            "proto_ipv6-no": int(row['proto_ipv6-no']),
            "proto_ipv6-opts": int(row['proto_ipv6-opts']),
            "proto_ipv6-route": int(row['proto_ipv6-route']),
            "proto_ipx-n-ip": int(row['proto_ipx-n-ip']),
            "proto_irtp": int(row['proto_irtp']),
            "proto_isis": int(row['proto_isis']),
            "proto_iso-ip": int(row['proto_iso-ip']),
            "proto_iso-tp4": int(row['proto_iso-tp4']),
            "proto_kryptolan": int(row['proto_kryptolan']),
            "proto_l2tp": int(row['proto_l2tp']),
            "proto_larp": int(row['proto_larp']),
            "proto_leaf-1": int(row['proto_leaf-1']),
            "proto_leaf-2": int(row['proto_leaf-2']),
            "proto_llc": int(row['proto_llc']),
            "proto_lldp": int(row['proto_lldp']),
            "proto_merit-inp": int(row['proto_merit-inp']),
            "proto_mfe_nsp": int(row['proto_mfe-nsp']),
            "proto_mhrp": int(row['proto_mhrp']),
            "proto_micp": int(row['proto_micp']),
            "proto_mobile": int(row['proto_mobile']),
            "proto_mtp": int(row['proto_mtp']),
            "proto_mux": int(row['proto_mux']),
            "proto_narp": int(row['proto_narp']),
            "proto_netblt": int(row['proto_netblt']),
            "proto_nsfnet-igp": int(row['proto_nsfnet-igp']),
            "proto_nvp": int(row['proto_nvp']),
            "proto_ospf": int(row['proto_ospf']),
            "proto_pgm": int(row['proto_pgm']),
            "proto_pim": int(row['proto_pim']),
            "proto_pipe": int(row['proto_pipe']),
            "proto_pnni": int(row['proto_pnni']),
            "proto_pri-enc": int(row['proto_pri-enc']),
            "proto_prm": int(row['proto_prm']),
            "proto_ptp": int(row['proto_ptp']),
            "proto_pup": int(row['proto_pup']),
            "proto_pvp": int(row['proto_pvp']),
            "proto_qnx": int(row['proto_qnx']),
            "proto_rdp": int(row['proto_rdp']),
            "proto_rsvp": int(row['proto_rsvp']),
            "proto_rtcp": int(row['proto_rtcp']),
            "proto_rtp": int(row['proto_rtp']),
            "proto_rvd": int(row['proto_rvd']),
            "proto_sat-expak": int(row['proto_sat-expak']),
            "proto_sat-mon": int(row['proto_sat-mon']),
            "proto_sccopmce": int(row['proto_sccopmce']),
            "proto_scps": int(row['proto_scps']),
            "proto_sctp": int(row['proto_sctp']),
            "proto_sdrp": int(row['proto_sdrp']),
            "proto_secure-vmtp": int(row['proto_secure-vmtp']),
            "proto_sep": int(row['proto_sep']),
            "proto_skip": int(row['proto_skip']),
            "proto_sm": int(row['proto_sm']),
            "proto_smp": int(row['proto_smp']),
            "proto_snp": int(row['proto_snp']),
            "proto_sprite-rpc": int(row['proto_sprite-rpc']),
            "proto_sps": int(row['proto_sps']),
            "proto_srp": int(row['proto_srp']),
            "proto_st2": int(row['proto_st2']),
            "proto_stp": int(row['proto_stp']),
            "proto_sun_nd": int(row['proto_sun-nd']),
            "proto_swipe": int(row['proto_swipe']),
            "proto_tcf": int(row['proto_tcf']),
            "proto_tcp": int(row['proto_tcp']),
            "proto_tlsp": int(row['proto_tlsp']),
            "proto_tp": int(row['proto_tp++']),
            "proto_trunk-1": int(row['proto_trunk-1']),
            "proto_trunk-2": int(row['proto_trunk-2']),
            "proto_ttp": int(row['proto_ttp']),
            "proto_udp": int(row['proto_udp']),
            "proto_udt": int(row['proto_udt']),
            "proto_unas": int(row['proto_unas']),
            "proto_uti": int(row['proto_uti']),
            "proto_vines": int(row['proto_vines']),
            "proto_visa": int(row['proto_visa']),
            "proto_vmtp": int(row['proto_vmtp']),
            "proto_vrrp": int(row['proto_vrrp']),
            "proto_wb-expak": int(row['proto_wb-expak']),
            "proto_wb-mon": int(row['proto_wb-mon']),
            "proto_wsn": int(row['proto_wsn']),
            "proto_xnet": int(row['proto_xnet']),
            "proto_xns-idp": int(row['proto_xns-idp']),
            "proto_xtp": int(row['proto_xtp']),
            "proto_zero": int(row['proto_zero']),
            "state_ACC": int(row['state_ACC']),
            "state_CLO": int(row['state_CLO']),
            "state_CON": int(row['state_CON']),
            "state_ECO": int(row['state_ECO']),
            "state_ECR": int(row['state_ECR']),
            "state_FIN": int(row['state_FIN']),
            "state_INT": int(row['state_INT']),
            "state_MAS": int(row['state_MAS']),
            "state_MHR": int(row['state_MHR']),
            "state_NNS": int(row['state_NNS']),
            "state_NRS": int(row['state_NRS']),
            "state_PAR": int(row['state_PAR']),
            "state_REQ": int(row['state_REQ']),
            "state_RSP": int(row['state_RSP']),
            "state_RST": int(row['state_RST']),
            "state_TST": int(row['state_TST']),
            "state_TXD": int(row['state_TXD']),
            "state_URF": int(row['state_URF']),
            "state_URFIL": int(row['state_URFIL']),
            "state_URH": int(row['state_URH']),
            "state_URHPRO": int(row['state_URHPRO']),
            "state_URN": int(row['state_URN']),
            "state_URP": int(row['state_URP']),
            "state_no": int(row['state_no']),
            "service_-": int(row['service_-']),
            "service_0": int(row['service_0']),
            "service_dhcp": int(row['service_dhcp']),
            "service_dns": int(row['service_dns']),
            "service_ftp": int(row['service_ftp']),
            "service_ftp-data": int(row['service_ftp-data']),
            "service_http": int(row['service_http']),
            "service_irc": int(row['service_irc']),
            "service_pop3": int(row['service_pop3']),
            "service_radius": int(row['service_radius']),
            "service_smtp": int(row['service_smtp']),
            "service_snmp": int(row['service_snmp']),
            "service_ssh": int(row['service_ssh']),
            "service_ssl": int(row['service_ssl'])
        }

