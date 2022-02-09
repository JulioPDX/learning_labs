END=8
for ((i=1;i<=END;i++)); do
    cp clab-bgp/R$i/flash/startup-config solution3/R$i.conf
done