#Dictionary Filtering Based on Conditions
electronic_devices = {
    "Accer": 10,
    "HP": 5,
    "Apple": 30,
    "Lenovo": 15  
}
sustainable_devices = {device: quantity for device, quantity in electronic_devices.items() if quantity > 10}
print("Sustainability of Electronic Devices:", sustainable_devices)
