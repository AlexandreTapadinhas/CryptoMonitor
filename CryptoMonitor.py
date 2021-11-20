import tkinter as tk
import requests

def getPrice(symbols):
    priceDict = {}
    for sym in symbols:
        pass
    
    price = 0
    url = 'https://api.coinstats.app/public/v1/coins?skip=0&currency=EUR'
    payload = {}
    headers = {}
    response = requests.get(url).json()
    #print(response['coins'])

    for coin in response['coins']:
        if (coin['symbol'] in symbols):
            priceDict[coin['id']] = coin['price']

    return priceDict
    

def screen(dict_prices):
    canvas = tk.Tk()
    #canvas.geometry("400x500")
    canvas.title("Crypto Monitor")

    f1 = ("poppins", 24, "bold")
    f2 = ("poppins", 18, "normal")

    label = tk.Label(canvas, text="Crypto Currencies prices", font = f2)
    label.pack(pady = 20)

    for key, value in dict_prices.items():
        label_aux = tk.Label(canvas, font=f2, borderwidth=5)
        label_aux.config(text='%s : %f €'%(key.capitalize(),float(value)))
        label_aux.pack(pady = 10)

    canvas.mainloop()



if __name__ == "__main__":
    print("CryptoMonitor")
    symList = ['BTC', 'ETH', 'ADA', 'DOGE', 'SOL']
    prices = getPrice(symList)

    for key, value in prices.items():
        print(key.capitalize(), " : ", value)

    screen(prices)
