alert tcp 18.221.219.4/24 any -> 172.31.69.25/24 21 (msg:"Bruteforce"; sid:1000002)

alert tcp 18.219.211.138/24 any -> 172.31.69.25/24 80 (msg:"DdoS"; detection_filter: track by_src, count 300, seconds 1; sid:1000001)

alert http 18.218.115.60/24 any -> 172.31.69.28/24 80 (msg:"WebAttack"; http_method; content:"POST"; http_uri; content:"DVWA/login.php"; sid:1000003)

alert http 172.31.69.28/24 any -> 18.219.211.138/24 8080 (msg:"Botnet"; sid:1000004)
