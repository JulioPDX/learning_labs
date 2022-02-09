END=3
for ((i=1;i<=END;i++)); do
    cp clab-bgp/R$i/config/config.json configs/R$i.json
done