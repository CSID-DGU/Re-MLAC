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
    def from_dataframe(dataframe: pd.DataFrame):
        return {
            "dur": float(dataframe['dur']),
            "sbytes": float(dataframe['sbytes']),
            "dbytes": float(dataframe['dbytes']),
            "sttl": float(dataframe['sttl']),
            "dttl": float(dataframe['dttl']),
            "sloss": float(dataframe['sloss']),
            "dloss": float(dataframe['dloss']),
            "sload": float(dataframe['sload']),
            "dload": float(dataframe['dload']),
            "spkts": float(dataframe['spkts']),
            "dpkts": float(dataframe['dpkts']),
            "swin": float(dataframe['swin']),
            "dwin": float(dataframe['dwin']),
            "stcpb": float(dataframe['stcpb']),
            "dtcpb": float(dataframe['dtcpb']),
            "smeansz": float(dataframe['smeansz']),
            "dmeansz": float(dataframe['dmeansz']),
            "trans_depth": float(dataframe['trans_depth']),
            "res_bdy_len": float(dataframe['res_bdy_len']),
            "sjit": float(dataframe['sjit']),
            "djit": float(dataframe['djit']),
            "sintpkt": float(dataframe['sintpkt']),
            "dintpkt": float(dataframe['dintpkt']),
            "tcprtt": float(dataframe['tcprtt']),
            "synack": float(dataframe['synack']),
            "ackdat": float(dataframe['ackdat']),
            "is_sm_ips_ports": int(dataframe['is_sm_ips_ports']),
            "ct_state_ttl": int(dataframe['ct_state_ttl']),
            "ct_flw_http_mthd": int(dataframe['ct_flw_http_mthd']),
            "is_ftp_login": int(dataframe['is_ftp_login']),
            "ct_ftp_cmd": int(dataframe['ct_ftp_cmd']),
            "proto_3pc": int(dataframe['proto_3pc']),
            "proto_a/n": int(dataframe['proto_a/n']),
            "proto_aes-sp3-d": int(dataframe['proto_aes-sp3-d']),
            "proto_any": int(dataframe['proto_any']),
            "proto_argus": int(dataframe['proto_argus']),
            "proto_aris": int(dataframe['proto_aris']),
            "proto_arp": int(dataframe['proto_arp']),
            "proto_ax.25": int(dataframe['proto_ax.25']),
            "proto_bbn-rcc": int(dataframe['proto_bbn-rcc']),
            "proto_bna": int(dataframe['proto_bna']),
            "proto_br-sat-mon": int(dataframe['proto_br-sat-mon']),
            "proto_cbt": int(dataframe['proto_cbt']),
            "proto_cftp": int(dataframe['proto_cftp']),
            "proto_chaos": int(dataframe['proto_chaos']),
            "proto_compaq-peer": int(dataframe['proto_compaq-peer']),
            "proto_cphb": int(dataframe['proto_cphb']),
            "proto_cpnx": int(dataframe['proto_cpnx']),
            "proto_crtp": int(dataframe['proto_crtp']),
            "proto_crudp": int(dataframe['proto_crudp']),
            "proto_dcn": int(dataframe['proto_dcn']),
            "proto_ddp": int(dataframe['proto_ddp']),
            "proto_ddx": int(dataframe['proto_ddx']),
            "proto_dgp": int(dataframe['proto_dgp']),
            "proto_egp": int(dataframe['proto_egp']),
            "proto_eigrp": int(dataframe['proto_eigrp']),
            "proto_emcon": int(dataframe['proto_emcon']),
            "proto_encap": int(dataframe['proto_encap']),
            "proto_esp": int(dataframe['proto_esp']),
            "proto_etherip": int(dataframe['proto_etherip']),
            "proto_fc": int(dataframe['proto_fc']),
            "proto_fire": int(dataframe['proto_fire']),
            "proto_ggp": int(dataframe['proto_ggp']),
            "proto_gmtp": int(dataframe['proto_gmtp']),
            "proto_gre": int(dataframe['proto_gre']),
            "proto_hmp": int(dataframe['proto_hmp']),
            "proto_i-nlsp": int(dataframe['proto_i-nlsp']),
            "proto_iatp": int(dataframe['proto_iatp']),
            "proto_ib": int(dataframe['proto_ib']),
            "proto_icmp": int(dataframe['proto_icmp']),
            "proto_idpr": int(dataframe['proto_idpr']),
            "proto_idpr-cmtp": int(dataframe['proto_idpr-cmtp']),
            "proto_idrp": int(dataframe['proto_idrp']),
            "proto_ifmp": int(dataframe['proto_ifmp']),
            "proto_igmp": int(dataframe['proto_igmp']),
            "proto_igp": int(dataframe['proto_igp']),
            "proto_il": int(dataframe['proto_il']),
            "proto_ip": int(dataframe['proto_ip']),
            "proto_ipcomp": int(dataframe['proto_ipcomp']),
            "proto_ipcv": int(dataframe['proto_ipcv']),
            "proto_ipip": int(dataframe['proto_ipip']),
            "proto_iplt": int(dataframe['proto_iplt']),
            "proto_ipnip": int(dataframe['proto_ipnip']),
            "proto_ippc": int(dataframe['proto_ippc']),
            "proto_ipv6": int(dataframe['proto_ipv6']),
            "proto_ipv6-frag": int(dataframe['proto_ipv6-frag']),
            "proto_ipv6-icmp": int(dataframe['proto_ipv6-icmp']),
            "proto_ipv6-no": int(dataframe['proto_ipv6-no']),
            "proto_ipv6-opts": int(dataframe['proto_ipv6-opts']),
            "proto_ipv6-route": int(dataframe['proto_ipv6-route']),
            "proto_ipx-n-ip": int(dataframe['proto_ipx-n-ip']),
            "proto_irtp": int(dataframe['proto_irtp']),
            "proto_isis": int(dataframe['proto_isis']),
            "proto_iso-ip": int(dataframe['proto_iso-ip']),
            "proto_iso-tp4": int(dataframe['proto_iso-tp4']),
            "proto_kryptolan": int(dataframe['proto_kryptolan']),
            "proto_l2tp": int(dataframe['proto_l2tp']),
            "proto_larp": int(dataframe['proto_larp']),
            "proto_leaf-1": int(dataframe['proto_leaf-1']),
            "proto_leaf-2": int(dataframe['proto_leaf-2']),
            "proto_llc": int(dataframe['proto_llc']),
            "proto_lldp": int(dataframe['proto_lldp']),
            "proto_merit-inp": int(dataframe['proto_merit-inp']),
            "proto_mhrp": int(dataframe['proto_mhrp']),
            "proto_micp": int(dataframe['proto_micp']),
            "proto_mobile": int(dataframe['proto_mobile']),
            "proto_mtp": int(dataframe['proto_mtp']),
            "proto_mux": int(dataframe['proto_mux']),
            "proto_narp": int(dataframe['proto_narp']),
            "proto_netblt": int(dataframe['proto_netblt']),
            "proto_nsfnet-igp": int(dataframe['proto_nsfnet-igp']),
            "proto_nvp": int(dataframe['proto_nvp']),
            "proto_ospf": int(dataframe['proto_ospf']),
            "proto_pgm": int(dataframe['proto_pgm']),
            "proto_pim": int(dataframe['proto_pim']),
            "proto_pipe": int(dataframe['proto_pipe']),
            "proto_pnni": int(dataframe['proto_pnni']),
            "proto_pri-enc": int(dataframe['proto_pri-enc']),
            "proto_prm": int(dataframe['proto_prm']),
            "proto_ptp": int(dataframe['proto_ptp']),
            "proto_pup": int(dataframe['proto_pup']),
            "proto_pvp": int(dataframe['proto_pvp']),
            "proto_qnx": int(dataframe['proto_qnx']),
            "proto_rdp": int(dataframe['proto_rdp']),
            "proto_rsvp": int(dataframe['proto_rsvp']),
            "proto_rtcp": int(dataframe['proto_rtcp']),
            "proto_rtp": int(dataframe['proto_rtp']),
            "proto_rvd": int(dataframe['proto_rvd']),
            "proto_sat-expak": int(dataframe["proto_sat-expak"]),
            "proto_sat-mon": int(dataframe["proto_sat-mon"]),
            "proto_sccopmce": int(dataframe["proto_sccopmce"]),
            "proto_scps": int(dataframe["proto_scps"]),
            "proto_sctp": int(dataframe["proto_sctp"]),
            "proto_sdrp": int(dataframe["proto_sdrp"]),
            "proto_secure-vmtp": int(dataframe["proto_secure-vmtp"]),
            "proto_sep": int(dataframe["proto_sep"]),
            "proto_skip": int(dataframe["proto_skip"]),
            "proto_sm": int(dataframe["proto_sm"]),
            "proto_smp": int(dataframe["proto_smp"]),
            "proto_snp": int(dataframe["proto_snp"]),
            "proto_sprite-rpc": int(dataframe["proto_sprite-rpc"]),
            "proto_sps": int(dataframe["proto_sps"]),
            "proto_srp": int(dataframe["proto_srp"]),
            "proto_st2": int(dataframe["proto_st2"]),
            "proto_stp": int(dataframe["proto_stp"]),
            "proto_sun-nd": int(dataframe["proto_sun-nd"]),
            "proto_swipe": int(dataframe["proto_swipe"]),
            "proto_tcf": int(dataframe["proto_tcf"]),
            "proto_tcp": int(dataframe["proto_tcp"]),
            "proto_tlsp": int(dataframe["proto_tlsp"]),
            "proto_tp++": int(dataframe["proto_tp++"]),
            "proto_trunk-1": int(dataframe["proto_trunk-1"]),
            "proto_trunk-2": int(dataframe["proto_trunk-2"]),
            "proto_ttp": int(dataframe["proto_ttp"]),
            "proto_udp": int(dataframe["proto_udp"]),
            "proto_udt": int(dataframe["proto_udt"]),
            "proto_unas": int(dataframe["proto_unas"]),
            "proto_uti": int(dataframe["proto_uti"]),
            "proto_vines": int(dataframe["proto_vines"]),
            "proto_visa": int(dataframe["proto_visa"]),
            "proto_vmtp": int(dataframe["proto_vmtp"]),
            "proto_vrrp": int(dataframe["proto_vrrp"]),
            "proto_wb-expak": int(dataframe["proto_wb-expak"]),
            "proto_wb-mon": int(dataframe["proto_wb-mon"]),
            "proto_wsn": int(dataframe["proto_wsn"]),
            "proto_xnet": int(dataframe["proto_xnet"]),
            "proto_xns-idp": int(dataframe["proto_xns-idp"]),
            "proto_xtp": int(dataframe["proto_xtp"]),
            "proto_zero": int(dataframe["proto_zero"]),
            "state_ACC": int(dataframe["state_ACC"]),
            "state_CLO": int(dataframe["state_CLO"]),
            "state_CON": int(dataframe["state_CON"]),
            "state_ECO": int(dataframe["state_ECO"]),
            "state_ECR": int(dataframe["state_ECR"]),
            "state_FIN": int(dataframe["state_FIN"]),
            "state_INT": int(dataframe["state_INT"]),
            "state_MAS": int(dataframe["state_MAS"]),
            "state_MHR": int(dataframe["state_MHR"]),
            "state_NNS": int(dataframe["state_NNS"]),
            "state_NRS": int(dataframe["state_NRS"]),
            "state_PAR": int(dataframe["state_PAR"]),
            "state_REQ": int(dataframe["state_REQ"]),
            "state_RSP": int(dataframe["state_RSP"]),
            "state_RST": int(dataframe["state_RST"]),
            "state_TST": int(dataframe["state_TST"]),
            "state_TXD": int(dataframe["state_TXD"]),
            "state_URF": int(dataframe["state_URF"]),
            "state_URFIL": int(dataframe["state_URFIL"]),
            "state_URH": int(dataframe["state_URH"]),
            "state_URHPRO": int(dataframe["state_URHPRO"]),
            "state_URN": int(dataframe["state_URN"]),
            "state_URP": int(dataframe["state_URP"]),
            "state_no": int(dataframe["state_no"]),
            "service_-": int(dataframe["service_-"]),
            "service_0": int(dataframe["service_0"]),
            "service_dhcp": int(dataframe["service_dhcp"]),
            "service_dns": int(dataframe["service_dns"]),
            "service_ftp": int(dataframe["service_ftp"]),
            "service_ftp-data": int(dataframe["service_ftp-data"]),
            "service_http": int(dataframe["service_http"]),
            "service_irc": int(dataframe["service_irc"]),
            "service_pop3": int(dataframe["service_pop3"]),
            "service_radius": int(dataframe["service_radius"]),
            "service_smtp": int(dataframe["service_smtp"]),
            "service_snmp": int(dataframe["service_snmp"]),
            "service_ssh": int(dataframe["service_ssh"]),
            "service_ssl": int(dataframe["service_ssl"])
        }
