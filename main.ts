let signalStength = 0
radio.setGroup(1)
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    signalStength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    led.plotBarGraph(Math.map(signalStength, -95, -42, 0, 9), 9)
})
basic.forever(function on_forever() {
    radio.sendNumber(1)
    pause(100)
})
