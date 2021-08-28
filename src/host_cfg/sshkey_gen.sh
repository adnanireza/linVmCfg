if [ ! -f ~/.ssh/id_ecdsa.pub ]; then
    echo "Public key does not exist. Will create pair..."
    ssh-keygen -t ecdsa -b 384 -C "adnanireza@yahoo.com"
fi
