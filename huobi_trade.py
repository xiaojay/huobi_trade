import huobi

email = "your email"
password = "your password"

if __name__ == '__main__':
    client = huobi.Huobi(email, password)
    client.buy(3, 3)
    client.sell(3, 3)
    pass
