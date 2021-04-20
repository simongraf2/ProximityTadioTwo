signalStength = 0
radio.set_group(1)

def on_received_number(receivedNumber):
    global signalStength
    signalStength = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    led.plot_bar_graph(Math.map(signalStength, -95, -42, 0, 9), 9)
radio.on_received_number(on_received_number)


def on_forever():
    radio.send_number(1)
    pause(100)
basic.forever(on_forever)
