from django.apps import AppConfig

import logging
import warnings
import joblib
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

class PacketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'packet'
    
    def ready(self) -> None:
        PipelineFactory().initialize(L1_model_path='./ai-model/L1_model.pkl',
                                      L2_model_path='./ai-model/L2_model.pkl',
                                      L3_1_model_path='./ai-model/L3_1_model.pkl',
                                      L3_2_model_path='./ai-model/L3_2_model.pkl',
                                      L3_3_model_path='./ai-model/L3_3_model.pkl',
                                      L3_4_model_path='./ai-model/L3_4_model.pkl')

        return super().ready()
    
class PipelineFactory():
    _instance = None

    @classmethod
    def initialize(cls, **kwargs):
        if cls._instance is None:
            cls._instance = Pipeline(**kwargs)
    
    @classmethod
    def get_instance(cls):
        return cls._instance

class Pipeline():
    def __init__(self,
                 L1_model_path: str,
                 L2_model_path: str,
                 L3_1_model_path: str,
                 L3_2_model_path: str,
                 L3_3_model_path: str,
                 L3_4_model_path: str):
        self.L1_model = joblib.load(L1_model_path)
        self.L2_model = joblib.load(L2_model_path)
        self.L3_1_model = joblib.load(L3_1_model_path)
        self.L3_2_model = joblib.load(L3_2_model_path)
        self.L3_3_model = joblib.load(L3_3_model_path)
        self.L3_4_model = joblib.load(L3_4_model_path)
        self.column_names = [
            'dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'sloss', 'dloss', 'sload', 'dload', 'spkts', 'dpkts',
            'swin', 'dwin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz', 'trans_depth', 'res_bdy_len', 'sjit', 'djit',
            'sintpkt', 'dintpkt', 'tcprtt', 'synack', 'ackdat', 'is_sm_ips_ports', 'ct_state_ttl', 'ct_flw_http_mthd',
            'is_ftp_login', 'ct_ftp_cmd', 'proto_3pc', 'proto_a/n', 'proto_aes-sp3-d', 'proto_any', 'proto_argus',
            'proto_aris', 'proto_arp', 'proto_ax.25', 'proto_bbn-rcc', 'proto_bna', 'proto_br-sat-mon', 'proto_cbt',
            'proto_cftp', 'proto_chaos', 'proto_compaq-peer', 'proto_cphb', 'proto_cpnx', 'proto_crtp', 'proto_crudp',
            'proto_dcn', 'proto_ddp', 'proto_ddx', 'proto_dgp', 'proto_egp', 'proto_eigrp', 'proto_emcon', 'proto_encap',
            'proto_esp', 'proto_etherip', 'proto_fc', 'proto_fire', 'proto_ggp', 'proto_gmtp', 'proto_gre', 'proto_hmp',
            'proto_i-nlsp', 'proto_iatp', 'proto_ib', 'proto_icmp', 'proto_idpr', 'proto_idpr-cmtp', 'proto_idrp',
            'proto_ifmp', 'proto_igmp', 'proto_igp', 'proto_il', 'proto_ip', 'proto_ipcomp', 'proto_ipcv', 'proto_ipip',
            'proto_iplt', 'proto_ipnip', 'proto_ippc', 'proto_ipv6', 'proto_ipv6-frag', 'proto_ipv6-icmp', 'proto_ipv6-no',
            'proto_ipv6-opts', 'proto_ipv6-route', 'proto_ipx-n-ip', 'proto_irtp', 'proto_isis', 'proto_iso-ip',
            'proto_iso-tp4', 'proto_kryptolan', 'proto_l2tp', 'proto_larp', 'proto_leaf-1', 'proto_leaf-2', 'proto_llc',
            'proto_lldp', 'proto_merit-inp', 'proto_mfe-nsp', 'proto_mhrp', 'proto_micp', 'proto_mobile', 'proto_mtp',
            'proto_mux', 'proto_narp', 'proto_netblt', 'proto_nsfnet-igp', 'proto_nvp', 'proto_ospf', 'proto_pgm',
            'proto_pim', 'proto_pipe', 'proto_pnni', 'proto_pri-enc', 'proto_prm', 'proto_ptp', 'proto_pup', 'proto_pvp',
            'proto_qnx', 'proto_rdp', 'proto_rsvp', 'proto_rtcp', 'proto_rtp', 'proto_rvd', 'proto_sat-expak',
            'proto_sat-mon', 'proto_sccopmce', 'proto_scps', 'proto_sctp', 'proto_sdrp', 'proto_secure-vmtp', 'proto_sep',
            'proto_skip', 'proto_sm', 'proto_smp', 'proto_snp', 'proto_sprite-rpc', 'proto_sps', 'proto_srp', 'proto_st2',
            'proto_stp', 'proto_sun-nd', 'proto_swipe', 'proto_tcf', 'proto_tcp', 'proto_tlsp', 'proto_tp++',
            'proto_trunk-1', 'proto_trunk-2', 'proto_ttp', 'proto_udp', 'proto_udt', 'proto_unas', 'proto_uti',
            'proto_vines', 'proto_visa', 'proto_vmtp', 'proto_vrrp', 'proto_wb-expak', 'proto_wb-mon', 'proto_wsn',
            'proto_xnet', 'proto_xns-idp', 'proto_xtp', 'proto_zero', 'state_ACC', 'state_CLO', 'state_CON', 'state_ECO',
            'state_ECR', 'state_FIN', 'state_INT', 'state_MAS', 'state_MHR', 'state_NNS', 'state_NRS', 'state_PAR',
            'state_REQ', 'state_RSP', 'state_RST', 'state_TST', 'state_TXD', 'state_URF', 'state_URFIL', 'state_URH',
            'state_URHPRO', 'state_URN', 'state_URP', 'state_no', 'service_-', 'service_0', 'service_dhcp', 'service_dns',
            'service_ftp', 'service_ftp-data', 'service_http', 'service_irc', 'service_pop3', 'service_radius',
            'service_smtp', 'service_snmp', 'service_ssh', 'service_ssl']
        self.nist_categories = [
            'BENIGN', 'PORTSCAN', 'RECONNAISSANCE', 'WEB_ATTACK_BRUTE_FORCE', 'WEB_ATTACK_XSS',
            'WEB_ATTACK_SQL_INJECTION', 'HEARTBLEED', 'EXPLOITS', 'FUZZERS', 'FTP_PATATOR', 'SSH_PATATOR',
            'BACKDOOR', 'BOT', 'SHELLCODE', 'WORMS', 'INFILTRATION', 'DOS_SLOWHTTPTEST',
            'DDOS', 'DOS', 'DOS_GOLDENEYE', 'DOS_HULK', 'DOS_SLOWLORIS', 'GENERIC', 'ANALYSIS']

    def run(self, input: dict) -> str:
        values = [input.get(column_name, 0.0) for column_name in self.column_names]
        data = pd.DataFrame([values], columns=self.column_names)
        
        # L1 모델 결과 보기
        L1_y_pred = self.L1_model.predict(data)
        logging.debug(f'Layer 1 Result is {L1_y_pred}')
        
        # L1 모델 분기처리 및 최종 결과 출력
        if (L1_y_pred == 0):
            return self.nist_categories[0]

        # L1 데이터 전처리
        L1_y_data = pd.DataFrame({'attack_category': L1_y_pred})
        malicious_indices = L1_y_data[L1_y_data['attack_category'] != 0].index
        L2_X_test = data.iloc[malicious_indices]

        # L2 모델 결과 보기
        L2_y_pred = self.L2_model.predict(L2_X_test)
        logging.debug(f'Layer 2 Result is {L2_y_pred}')

        # L2 데이터 전처리
        L3_y_test = data.iloc[malicious_indices]

        # L3 모델 분기처리 및 결과 보기
        category = L2_y_pred[0]
        if category == 0:
            return self.nist_categories[0]
        elif category == 1:
            L3_y_pred = self.L3_1_model.predict(L3_y_test)
        elif category == 2:
            L3_y_pred = self.L3_2_model.predict(L3_y_test)
        elif category == 3:
            L3_y_pred = self.L3_3_model.predict(L3_y_test)
        elif category == 4:
            L3_y_pred = self.L3_4_model.predict(L3_y_test)
        
        logging.debug(f'Layer 3 Result is {L3_y_pred}')
        logging.debug(f'Final Result is {self.nist_categories[L3_y_pred[0]]}')
        
        return self.nist_categories[L3_y_pred[0]]
